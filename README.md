# 每日 AI 论文工作流

从 Hugging Face Daily Papers 和 arXiv 拉当天论文，按 arXiv ID 交叉去重，打分后写出 Markdown 列表和 RSS。

不依赖第三方包。AlphaSignal、TLDR 没有稳定公开接口，所以没有硬爬；社区筛选用 HF 点赞代替。

仓库：https://github.com/liu-zhengdong/paper-digest

RSS（阅读器直接订这个）：

https://raw.githubusercontent.com/liu-zhengdong/paper-digest/main/output/feed.xml

列表：

https://github.com/liu-zhengdong/paper-digest/blob/main/output/digest.md

## 跑一次

```bash
python3 digest.py
```

产物：

- `output/digest.md` 人读列表
- `output/feed.xml` RSS 2.0
- `output/papers.json` 去重后的结构化结果

## 排序

HF 上榜 +8，arXiv 新进 +1，多一个来源 +3，HF 赞每票 +0.5（封顶 40），兴趣词每命中 +2（封顶 4 个）。`config.json` 里的 `exclude` 会压掉非 HF 论文。

默认只保留「上了 HF」或「命中兴趣词」的论文，最多 `top_n` 篇。这样 RSS 不是 arXiv 消防栓。

## 改兴趣

编辑 `config.json` 的 `interests` / `exclude` / `arxiv_categories` / `top_n`。兴趣词用英文，因为摘要几乎都是英文；写太宽（只写 `model`）会把过滤打废。

## 每天自动跑

GitHub Actions 每天 00:15 UTC 跑一次，把 `output/` 推回 `main`。阅读器订 raw 链接即可，不用单独开 Pages。
