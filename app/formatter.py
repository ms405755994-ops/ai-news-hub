from __future__ import annotations

from app.models import NewsItem


def format_wechat(items: list[NewsItem]) -> str:
    lines = ["# 今日AI/科技新闻", ""]

    for idx, item in enumerate(items, start=1):
        title = item.title_zh or item.title
        summary = item.summary_zh or item.summary or "暂无摘要"
        lines.append(f"{idx}. **{title}**")
        lines.append(f"> 来源：{item.source}")
        lines.append(f"> {summary}")
        lines.append(f"> [查看原文]({item.link})")
        lines.append("")

    return "\n".join(lines)


def format_telegram(items: list[NewsItem]) -> str:
    lines = ["今日 AI / 科技新闻", ""]

    for idx, item in enumerate(items, start=1):
        title = item.title_zh or item.title
        summary = item.summary_zh or item.summary or "暂无摘要"
        lines.append(f"{idx}. {title}")
        lines.append(f"来源：{item.source}")
        lines.append(summary)
        lines.append(item.link)
        lines.append("")

    return "\n".join(lines)
