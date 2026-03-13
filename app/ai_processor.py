import os
import requests

API_KEY = os.getenv("OPENAI_API_KEY")
MODEL = os.getenv("OPENAI_MODEL", "gpt-4o-mini")


def process_news(item):
    prompt = f"""
请把下面科技新闻翻译并总结成中文。

标题:
{item["title"]}

摘要:
{item["summary"]}

请输出：
1. 中文标题
2. 一句话中文总结
"""

    if not API_KEY:
        item["ai"] = item["title"]
        return item

    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json",
    }

    data = {
        "model": MODEL,
        "messages": [{"role": "user", "content": prompt}],
        "temperature": 0.2,
    }

    try:
        r = requests.post(
            "https://api.openai.com/v1/chat/completions",
            headers=headers,
            json=data,
            timeout=30,
        )
        r.raise_for_status()
        result = r.json()
        item["ai"] = result["choices"][0]["message"]["content"].strip()
    except Exception:
        item["ai"] = item["title"]

    return item
