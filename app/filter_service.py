from __future__ import annotations

from app.models import NewsItem
from app.storage import has_sent


def filter_items(items: list[NewsItem], db_path: str, max_items: int) -> list[NewsItem]:
    seen_titles: set[str] = set()
    result: list[NewsItem] = []

    for item in items:
        title_key = item.title.strip().lower()
        if not item.title or not item.link:
            continue
        if title_key in seen_titles:
            continue
        if has_sent(db_path, item.link):
            continue

        seen_titles.add(title_key)
        result.append(item)

        if len(result) >= max_items:
            break

    return result
