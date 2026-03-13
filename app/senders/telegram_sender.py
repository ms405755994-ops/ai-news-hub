from __future__ import annotations

import requests


def send_telegram(token: str, chat_id: str, message: str) -> None:
    if not token or not chat_id:
        print("TELEGRAM_TOKEN 或 TELEGRAM_CHAT_ID 未配置，跳过 Telegram 发送")
        return

    url = f"https://api.telegram.org/bot{token}/sendMessage"
    payload = {
        "chat_id": chat_id,
        "text": message,
        "disable_web_page_preview": False,
    }

    resp = requests.post(url, data=payload, timeout=15)
    resp.raise_for_status()
