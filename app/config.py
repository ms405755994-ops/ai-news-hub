from __future__ import annotations

import os
from dataclasses import dataclass
from pathlib import Path

from dotenv import load_dotenv


ROOT_DIR = Path(__file__).resolve().parent.parent
load_dotenv(ROOT_DIR / ".env")


@dataclass
class Settings:
    freshrss_base_url: str
    freshrss_username: str
    freshrss_api_password: str
    openai_api_key: str
    openai_api_base: str
    openai_model: str
    telegram_token: str
    telegram_chat_id: str
    wechat_webhook: str
    sqlite_path: str
    max_items: int
    hours_back: int


def get_settings() -> Settings:
    return Settings(
        freshrss_base_url=os.getenv("FRESHRSS_BASE_URL", "").strip(),
        freshrss_username=os.getenv("FRESHRSS_USERNAME", "").strip(),
        freshrss_api_password=os.getenv("FRESHRSS_API_PASSWORD", "").strip(),
        openai_api_key=os.getenv("OPENAI_API_KEY", "").strip(),
        openai_api_base=os.getenv("OPENAI_API_BASE", "https://api.openai.com/v1").strip(),
        openai_model=os.getenv("OPENAI_MODEL", "gpt-4o-mini").strip(),
        telegram_token=os.getenv("TELEGRAM_TOKEN", "").strip(),
        telegram_chat_id=os.getenv("TELEGRAM_CHAT_ID", "").strip(),
        wechat_webhook=os.getenv("WECHAT_WEBHOOK", "").strip(),
        sqlite_path=os.getenv("SQLITE_PATH", "data/news.db").strip(),
        max_items=int(os.getenv("MAX_ITEMS", "8")),
        hours_back=int(os.getenv("HOURS_BACK", "24")),
    )
