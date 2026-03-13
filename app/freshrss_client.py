from __future__ import annotations

import requests
import feedparser

from app.models import NewsItem


def _normalize_base_url(base_url: str) -> str:
    return base_url.rstrip("/")


def fetch_from_freshrss_rss(base_url: str, max_items: int = 8) -> list[NewsItem]:
    """
    兜底模式：直接读取 FreshRSS 输出的 RSS。
    常见格式：
    https://your-domain.example.com/i/?a=rss
    """
    if not base_url:
        return []

    rss_url = base_url
    feed = feedparser.parse(rss_url)

    items: list[NewsItem] = []
    for entry in getattr(feed, "entries", [])[:max_items]:
        items.append(
            NewsItem(
                source=getattr(feed.feed, "title", "FreshRSS"),
                title=getattr(entry, "title", "").strip(),
                summary=getattr(entry, "summary", "").strip(),
                link=getattr(entry, "link", "").strip(),
                published_at=getattr(entry, "published", "").strip(),
            )
        )
    return items


def fetch_news(
    base_url: str,
    username: str,
    api_password: str,
    max_items: int = 8,
) -> list[NewsItem]:
    """
    当前先使用 FreshRSS 暴露出来的 RSS 地址。
    如果你后面确认了自己实例的 API 形式，再升级到专用 API。
    """
    del username, api_password
    return fetch_from_freshrss_rss(base_url=base_url, max_items=max_items)
