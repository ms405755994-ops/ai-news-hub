from __future__ import annotations

import sqlite3
from pathlib import Path


def init_db(db_path: str) -> None:
    path = Path(db_path)
    path.parent.mkdir(parents=True, exist_ok=True)

    with sqlite3.connect(path) as conn:
        conn.execute(
            """
            CREATE TABLE IF NOT EXISTS sent_news (
                link TEXT PRIMARY KEY,
                sent_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
            """
        )
        conn.commit()


def has_sent(db_path: str, link: str) -> bool:
    if not link:
        return False

    with sqlite3.connect(db_path) as conn:
        row = conn.execute(
            "SELECT 1 FROM sent_news WHERE link = ? LIMIT 1",
            (link,),
        ).fetchone()
        return row is not None


def mark_sent(db_path: str, link: str) -> None:
    if not link:
        return

    with sqlite3.connect(db_path) as conn:
        conn.execute(
            "INSERT OR IGNORE INTO sent_news(link) VALUES (?)",
            (link,),
        )
        conn.commit()
