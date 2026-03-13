from __future__ import annotations

import requests

from app.models import NewsItem


def process_news(
    item: NewsItem,
    api_key: str,
    api_base: str,
    model: str,
) -> NewsItem:
    if not api_key:
        item.title_zh = item.title
        item.summary_zh = item.summary or "暂无摘要"
        return item

    prompt = f"""
请把下面科技新闻处理成中文：
1. 输出一个简洁自然的中文标题
2. 输出一到两句中文摘要
3. 不要夸张，不要营销口吻
4. 不要输出多余解释

原始标题：
{item.title}

原始摘要：
{item.summary}
"""

    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
    }

    payload = {
        "model": model,
        "messages": [
            {
                "role": "system",
                "content": "你是科技新闻编辑助手，擅长准确翻译和简要总结。",
            },
            {
                "role": "user",
                "content": prompt,
            },
        ],
        "temperature": 0.2,
    }

    try:
        resp = requests.post(
            f"{api_base.rstrip('/')}/chat/completions",
            headers=headers,
            json=payload,
            timeout=30,
        )
        resp.raise_for_status()
        data = resp.json()
        text = data["choices"][0]["message"]["content"].strip()

        parts = [p.strip(" -：:\n") for p in text.splitlines() if p.strip()]
        if len(parts) >= 2:
            item.title_zh = parts[0]
            item.summary_zh = " ".join(parts[1:])
        else:
            item.title_zh = item.title
            item.summary_zh = text
    except Exception:
        item.title_zh = item.title
        item.summary_zh = item.summary or "暂无摘要"

    return item
