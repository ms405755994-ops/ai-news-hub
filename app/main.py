from app.freshrss_client import fetch_news
from app.ai_processor import process_news
from app.formatter import format_wechat, format_telegram
from app.senders.wechat_sender import send_wechat
from app.senders.telegram_sender import send_telegram


def main():
    items = fetch_news()

    if not items:
        print("no news")
        return

    processed = []
    for item in items:
        processed.append(process_news(item))

    wechat_msg = format_wechat(processed)
    telegram_msg = format_telegram(processed)

    send_wechat(wechat_msg)
    send_telegram(telegram_msg)


if __name__ == "__main__":
    main()
