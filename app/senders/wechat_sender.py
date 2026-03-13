from __future__ import annotations

import requests


def send_wechat(webhook: str, message: str) -> None:
    if not webhook:
        print("WECHAT_WEBHOOK 未配置，跳过企业微信发送")
        return

    payload = {
        "msgtype": "markdown",
        "markdown": {
            "content": message,
        },
    }

    resp = requests.post(webhook, json=payload, timeout=15)
    resp.raise_for_status()

    result = resp.json()
    if result.get("errcode") != 0:
        raise RuntimeError(f"企业微信发送失败: {result}")
