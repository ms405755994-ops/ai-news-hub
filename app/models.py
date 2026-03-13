from dataclasses import dataclass
from typing import Optional

@dataclass
class NewsItem:
    source: str
    title: str
    summary: str
    link: str
    published_at: str = ""
    title_zh: Optional[str] = None
    summary_zh: Optional[str] = None
