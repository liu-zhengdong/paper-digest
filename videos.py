#!/usr/bin/env python3
"""Daily Agent-usage YouTube digest.

Pulls the no-Shorts playlist feed for each channel, filters broad channels
by keyword, dedupes by video id, and writes Markdown + RSS.
"""

from __future__ import annotations

import json
import time
import xml.etree.ElementTree as ET
from datetime import datetime, timedelta, timezone
from email.utils import format_datetime
from html import escape
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen

ROOT = Path(__file__).resolve().parent
OUT = ROOT / "output"
CONFIG_PATH = ROOT / "videos.config.json"
UA = "agent-video-digest/1.0"
ATOM = "http://www.w3.org/2005/Atom"
YT = "http://www.youtube.com/xml/schemas/2015"
MEDIA = "http://search.yahoo.com/mrss/"
NS = {"a": ATOM, "yt": YT, "media": MEDIA}


def load_config() -> dict:
    with CONFIG_PATH.open(encoding="utf-8") as f:
        return json.load(f)


def http_get(url: str) -> bytes:
    req = Request(url, headers={"User-Agent": UA, "Accept": "application/atom+xml"})
    with urlopen(req, timeout=40) as resp:
        return resp.read()


def longform_playlist(channel_id: str) -> str:
    return "UULF" + channel_id[2:]


def hits(text: str, keywords: list[str]) -> list[str]:
    low = text.lower()
    return [k for k in keywords if k.lower() in low]


def fetch_channel(channel: dict, cfg: dict) -> list[dict]:
    playlist = longform_playlist(channel["id"])
    url = f"https://www.youtube.com/feeds/videos.xml?playlist_id={playlist}"
    try:
        raw = http_get(url)
    except (HTTPError, URLError, TimeoutError) as exc:
        print(f"[yt] {channel['name']} failed: {exc}")
        return []
    root = ET.fromstring(raw)
    cutoff = datetime.now(timezone.utc) - timedelta(hours=cfg.get("lookback_hours", 168))
    keywords = cfg.get("keywords") or []
    videos = []
    for entry in root.findall("a:entry", NS):
        vid = entry.findtext("yt:videoId", default="", namespaces=NS)
        if not vid:
            continue
        published = entry.findtext("a:published", default="", namespaces=NS)
        try:
            stamp = datetime.fromisoformat(published.replace("Z", "+00:00"))
        except ValueError:
            continue
        if stamp < cutoff:
            continue
        title = " ".join((entry.findtext("a:title", default="", namespaces=NS) or "").split())
        group = entry.find("media:group", NS)
        description = ""
        if group is not None:
            description = " ".join((group.findtext("media:description", default="", namespaces=NS) or "").split())
        matched = hits(f"{title} {description}", keywords)
        if channel.get("mode") == "keyword" and not matched:
            continue
        videos.append(
            {
                "id": vid,
                "title": title,
                "summary": description[:500],
                "published": published,
                "channel": channel["name"],
                "mode": channel.get("mode") or "all",
                "hits": matched,
                "url": f"https://www.youtube.com/watch?v={vid}",
            }
        )
    print(f"[yt] {channel['name']}: {len(videos)}")
    return videos


def rank(videos: list[dict], cfg: dict) -> list[dict]:
    merged: dict[str, dict] = {}
    for video in videos:
        merged.setdefault(video["id"], video)
    ranked = []
    for video in merged.values():
        score = 2 if video.get("mode") == "all" else 0
        score += min(len(video.get("hits") or []), 4)
        ranked.append({**video, "score": score})
    ranked.sort(key=lambda v: (v.get("published") or ""), reverse=True)
    ranked.sort(key=lambda v: -v["score"])
    return ranked[: cfg.get("top_n", 40)]


def rfc822(value: str) -> str:
    try:
        stamp = datetime.fromisoformat((value or "").replace("Z", "+00:00"))
    except ValueError:
        stamp = datetime.now(timezone.utc)
    if stamp.tzinfo is None:
        stamp = stamp.replace(tzinfo=timezone.utc)
    return format_datetime(stamp)


def write_markdown(videos: list[dict], cfg: dict) -> None:
    now = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    lines = [
        f"# {cfg['feed_title']}",
        "",
        f"生成时间：{now}  ·  共 {len(videos)} 条（近 {cfg.get('lookback_hours', 168) // 24} 天，已去 Shorts、按视频 ID 去重）",
        "",
        "专注频道全收，泛 AI 频道只留标题或简介命中关键词的。关键词在 `videos.config.json`。",
        "",
    ]
    for i, video in enumerate(videos, 1):
        matched = ", ".join(video.get("hits") or []) or "-"
        summary = video.get("summary") or ""
        if len(summary) > 280:
            summary = summary[:280].rsplit(" ", 1)[0] + "…"
        lines += [
            f"## {i}. {video['title']}",
            "",
            f"- 频道：{video['channel']}  ·  分数：{video['score']}  ·  命中：{matched}",
            f"- 链接：{video['url']}",
            "",
            summary,
            "",
        ]
    (OUT / "videos.md").write_text("\n".join(lines), encoding="utf-8")


def write_rss(videos: list[dict], cfg: dict) -> None:
    now = format_datetime(datetime.now(timezone.utc))
    items = []
    for video in videos:
        matched = ", ".join(video.get("hits") or []) or "-"
        desc = (
            f"<p><b>{escape(video['channel'])}</b> · score {video['score']} · hits {escape(matched)}</p>"
            f"<p>{escape(video.get('summary') or '')}</p>"
        )
        items.append(
            "\n".join(
                [
                    "    <item>",
                    f"      <title>{escape(video['title'])}</title>",
                    f"      <link>{video['url']}</link>",
                    f"      <guid isPermaLink=\"true\">{video['url']}</guid>",
                    f"      <pubDate>{rfc822(video.get('published') or '')}</pubDate>",
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
    (OUT / "videos.xml").write_text(xml, encoding="utf-8")


def main() -> None:
    cfg = load_config()
    OUT.mkdir(parents=True, exist_ok=True)
    videos = []
    for channel in cfg.get("channels") or []:
        videos.extend(fetch_channel(channel, cfg))
        time.sleep(0.3)
    ranked = rank(videos, cfg)
    (OUT / "videos.json").write_text(
        json.dumps({"generated_at": datetime.now(timezone.utc).isoformat(), "count": len(ranked), "videos": ranked}, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
    write_markdown(ranked, cfg)
    write_rss(ranked, cfg)
    print(f"[done] {len(videos)} raw -> {len(ranked)} published")


if __name__ == "__main__":
    main()
