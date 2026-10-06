#!/usr/bin/env python3
"""Daily AI paper digest: fetch, dedupe, write Markdown + RSS.

Sources:
  - Hugging Face Daily Papers  https://huggingface.co/api/daily_papers
  - arXiv API                   https://export.arxiv.org/api/query

No third-party dependencies. Run: python3 digest.py
"""

from __future__ import annotations

import json
import re
import time
import xml.etree.ElementTree as ET
from datetime import datetime, timedelta, timezone
from email.utils import format_datetime
from html import escape
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.parse import urlencode
from urllib.request import Request, urlopen

ROOT = Path(__file__).resolve().parent
OUT = ROOT / "output"
CONFIG_PATH = ROOT / "config.json"
UA = "paper-digest/1.0 (daily research filter; mailto:local)"
ATOM = {"a": "http://www.w3.org/2005/Atom", "arxiv": "http://arxiv.org/schemas/atom"}


def load_config() -> dict:
    with CONFIG_PATH.open(encoding="utf-8") as f:
        return json.load(f)


def http_get(url: str, timeout: int = 60) -> bytes:
    req = Request(url, headers={"User-Agent": UA, "Accept": "*/*"})
    with urlopen(req, timeout=timeout) as resp:
        return resp.read()


def arxiv_id(value: str) -> str:
    value = (value or "").strip()
    value = value.replace("http://arxiv.org/abs/", "").replace("https://arxiv.org/abs/", "")
    value = value.split("v")[0] if re.search(r"v\d+$", value) else value
    match = re.search(r"(\d{4}\.\d{4,5})", value)
    return match.group(1) if match else value


def fetch_hf(cfg: dict) -> list[dict]:
    papers = []
    today = datetime.now(timezone.utc).date()
    for offset in range(cfg.get("hf_days", 2)):
        day = (today - timedelta(days=offset)).isoformat()
        qs = urlencode({"limit": cfg.get("hf_limit", 100), "date": day})
        url = f"https://huggingface.co/api/daily_papers?{qs}"
        try:
            payload = json.loads(http_get(url))
        except (HTTPError, URLError, TimeoutError, json.JSONDecodeError) as exc:
            print(f"[hf] {day} failed: {exc}")
            continue
        if not isinstance(payload, list):
            print(f"[hf] {day} unexpected payload")
            continue
        for row in payload:
            paper = row.get("paper") or {}
            pid = arxiv_id(paper.get("id") or "")
            if not pid:
                continue
            authors = [a.get("name") for a in paper.get("authors") or [] if a.get("name")]
            papers.append(
                {
                    "id": pid,
                    "title": (paper.get("title") or row.get("title") or "").replace("\n", " ").strip(),
                    "summary": (paper.get("summary") or row.get("summary") or "").replace("\n", " ").strip(),
                    "published": paper.get("publishedAt") or row.get("publishedAt") or "",
                    "authors": authors,
                    "upvotes": int(paper.get("upvotes") or 0),
                    "sources": ["huggingface"],
                    "hf_url": f"https://huggingface.co/papers/{pid}",
                    "arxiv_url": f"https://arxiv.org/abs/{pid}",
                    "pdf_url": f"https://arxiv.org/pdf/{pid}",
                }
            )
        print(f"[hf] {day}: {len(payload)}")
        time.sleep(0.4)
    return papers


def fetch_arxiv(cfg: dict) -> list[dict]:
    cats = cfg.get("arxiv_categories") or ["cs.AI", "cs.LG", "cs.CL"]
    query = " OR ".join(f"cat:{c}" for c in cats)
    qs = urlencode(
        {
            "search_query": query,
            "start": 0,
            "max_results": cfg.get("arxiv_max_results", 150),
            "sortBy": "submittedDate",
            "sortOrder": "descending",
        }
    )
    url = f"https://export.arxiv.org/api/query?{qs}"
    try:
        raw = http_get(url, timeout=90)
    except (HTTPError, URLError, TimeoutError) as exc:
        print(f"[arxiv] failed: {exc}")
        return []
    root = ET.fromstring(raw)
    cutoff = datetime.now(timezone.utc) - timedelta(hours=cfg.get("arxiv_lookback_hours", 48))
    papers = []
    for entry in root.findall("a:entry", ATOM):
        eid = entry.findtext("a:id", default="", namespaces=ATOM)
        pid = arxiv_id(eid)
        if not pid:
            continue
        updated = entry.findtext("a:updated", default="", namespaces=ATOM)
        published = entry.findtext("a:published", default=updated, namespaces=ATOM)
        try:
            stamp = datetime.fromisoformat(published.replace("Z", "+00:00"))
        except ValueError:
            stamp = datetime.now(timezone.utc)
        if stamp < cutoff:
            continue
        authors = [n.text for n in entry.findall("a:author/a:name", ATOM) if n.text]
        cats_found = [n.get("term") for n in entry.findall("a:category", ATOM) if n.get("term")]
        papers.append(
            {
                "id": pid,
                "title": " ".join((entry.findtext("a:title", default="", namespaces=ATOM) or "").split()),
                "summary": " ".join((entry.findtext("a:summary", default="", namespaces=ATOM) or "").split()),
                "published": published,
                "authors": authors,
                "upvotes": 0,
                "sources": ["arxiv"],
                "categories": cats_found,
                "hf_url": f"https://huggingface.co/papers/{pid}",
                "arxiv_url": f"https://arxiv.org/abs/{pid}",
                "pdf_url": f"https://arxiv.org/pdf/{pid}",
            }
        )
    print(f"[arxiv] kept {len(papers)} within lookback")
    return papers


def merge(groups: list[list[dict]]) -> list[dict]:
    merged: dict[str, dict] = {}
    for group in groups:
        for paper in group:
            pid = paper["id"]
            cur = merged.get(pid)
            if cur is None:
                merged[pid] = {**paper, "sources": list(paper.get("sources") or [])}
                continue
            for src in paper.get("sources") or []:
                if src not in cur["sources"]:
                    cur["sources"].append(src)
            cur["upvotes"] = max(cur.get("upvotes") or 0, paper.get("upvotes") or 0)
            if len(paper.get("summary") or "") > len(cur.get("summary") or ""):
                cur["summary"] = paper["summary"]
            if not cur.get("authors") and paper.get("authors"):
                cur["authors"] = paper["authors"]
            if paper.get("categories"):
                cur["categories"] = sorted(set(cur.get("categories") or []) | set(paper["categories"]))
            if paper.get("published") and (not cur.get("published") or paper["published"] < cur["published"]):
                cur["published"] = paper["published"]
    return list(merged.values())


def interest_hits(text: str, terms: list[str]) -> list[str]:
    low = text.lower()
    return [t for t in terms if t.lower() in low]


def score(paper: dict, cfg: dict) -> tuple[float, list[str], list[str]]:
    text = f"{paper.get('title', '')} {paper.get('summary', '')}"
    hits = interest_hits(text, cfg.get("interests") or [])
    blocked = interest_hits(text, cfg.get("exclude") or [])
    sources = paper.get("sources") or []
    value = 0.0
    if "huggingface" in sources:
        value += 8
    if "arxiv" in sources:
        value += 1
    value += min(paper.get("upvotes") or 0, 40) * 0.5
    value += max(0, len(sources) - 1) * 3
    value += min(len(hits), 4) * 2
    if blocked and "huggingface" not in sources:
        value -= 6
    return value, hits, blocked


def rank(papers: list[dict], cfg: dict) -> list[dict]:
    ranked = []
    for paper in papers:
        value, hits, blocked = score(paper, cfg)
        paper = {**paper, "score": round(value, 2), "hits": hits, "blocked": blocked}
        keep = "huggingface" in paper["sources"] or hits
        if blocked and "huggingface" not in paper["sources"]:
            keep = False
        if keep:
            ranked.append(paper)
    ranked.sort(key=lambda p: (-p["score"], -(p.get("upvotes") or 0), p.get("published") or ""))
    return ranked[: cfg.get("top_n", 30)]


def rfc822(value: str) -> str:
    try:
        stamp = datetime.fromisoformat((value or "").replace("Z", "+00:00"))
    except ValueError:
        stamp = datetime.now(timezone.utc)
    if stamp.tzinfo is None:
        stamp = stamp.replace(tzinfo=timezone.utc)
    return format_datetime(stamp)


def write_markdown(papers: list[dict], cfg: dict) -> None:
    now = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    lines = [
        f"# {cfg['feed_title']}",
        "",
        f"生成时间：{now}  ·  共 {len(papers)} 篇（已按 arXiv ID 去重）",
        "",
        "来源：Hugging Face Daily Papers + arXiv（cs.AI / cs.LG / cs.CL / cs.CV）。",
        "排序：HF 上榜、点赞、多源命中、兴趣词。兴趣词可在 `config.json` 改。",
        "",
    ]
    for i, paper in enumerate(papers, 1):
        authors = ", ".join(paper.get("authors") or []) or "unknown"
        sources = " + ".join(paper.get("sources") or [])
        hits = ", ".join(paper.get("hits") or []) or "-"
        summary = paper.get("summary") or ""
        if len(summary) > 420:
            summary = summary[:420].rsplit(" ", 1)[0] + "…"
        lines += [
            f"## {i}. {paper['title']}",
            "",
            f"- 分数：{paper['score']}  ·  HF 赞：{paper.get('upvotes') or 0}  ·  来源：{sources}",
            f"- 兴趣命中：{hits}",
            f"- 作者：{authors}",
            f"- 链接：[arXiv]({paper['arxiv_url']}) · [PDF]({paper['pdf_url']}) · [HF]({paper['hf_url']})",
            "",
            summary,
            "",
        ]
    (OUT / "digest.md").write_text("\n".join(lines), encoding="utf-8")


def write_rss(papers: list[dict], cfg: dict) -> None:
    now = format_datetime(datetime.now(timezone.utc))
    items = []
    for paper in papers:
        authors = ", ".join(paper.get("authors") or []) or "unknown"
        sources = ", ".join(paper.get("sources") or [])
        hits = ", ".join(paper.get("hits") or []) or "-"
        desc = (
            f"<p><b>score</b> {paper['score']} · <b>upvotes</b> {paper.get('upvotes') or 0} "
            f"· <b>sources</b> {escape(sources)} · <b>hits</b> {escape(hits)}</p>"
            f"<p>{escape(authors)}</p>"
            f"<p>{escape(paper.get('summary') or '')}</p>"
            f"<p><a href=\"{paper['pdf_url']}\">PDF</a> · "
            f"<a href=\"{paper['hf_url']}\">Hugging Face</a></p>"
        )
        items.append(
            "\n".join(
                [
                    "    <item>",
                    f"      <title>{escape(paper['title'])}</title>",
                    f"      <link>{paper['arxiv_url']}</link>",
                    f"      <guid isPermaLink=\"true\">{paper['arxiv_url']}</guid>",
                    f"      <pubDate>{rfc822(paper.get('published') or '')}</pubDate>",
                    f"      <description>{escape(desc)}</description>",
                    "    </item>",
                ]
            )
        )
    xml = "\n".join(
        [
            "<?xml version=\"1.0\" encoding=\"UTF-8\"?>",
            "<rss version=\"2.0\">",
            "  <channel>",
            f"    <title>{escape(cfg['feed_title'])}</title>",
            f"    <link>{escape(cfg['feed_link'])}</link>",
            f"    <description>{escape(cfg['feed_description'])}</description>",
            "    <language>zh-CN</language>",
            f"    <lastBuildDate>{now}</lastBuildDate>",
            *items,
            "  </channel>",
            "</rss>",
            "",
        ]
    )
    (OUT / "feed.xml").write_text(xml, encoding="utf-8")


def main() -> None:
    cfg = load_config()
    OUT.mkdir(parents=True, exist_ok=True)
    papers = merge([fetch_hf(cfg), fetch_arxiv(cfg)])
    ranked = rank(papers, cfg)
    (OUT / "papers.json").write_text(
        json.dumps({"generated_at": datetime.now(timezone.utc).isoformat(), "count": len(ranked), "papers": ranked}, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
    write_markdown(ranked, cfg)
    write_rss(ranked, cfg)
    print(f"[done] {len(papers)} unique -> {len(ranked)} published")
    print(f"[done] {OUT / 'digest.md'}")
    print(f"[done] {OUT / 'feed.xml'}")


if __name__ == "__main__":
    main()
