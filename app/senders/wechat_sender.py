import os
import requests


def send_wechat(msg):
    webhook = os.getenv("WECHAT_WEBHOOK")
    if not webhook:
        print("WECHAT_WEBHOOK not set")
        return

    data = {
        "msgtype": "markdown",
        "markdown": {"content": msg},
    }

    requests.post(webhook, json=data, timeout=15)
