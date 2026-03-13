import feedparser

RSS_LIST = [
    "https://feeds.feedburner.com/TechCrunch",
    "https://rss.nytimes.com/services/xml/rss/nyt/Technology.xml",
]


def fetch_news():
    items = []

    for url in RSS_LIST:
        feed = feedparser.parse(url)

        for entry in feed.entries[:5]:
            items.append(
                {
                    "title": entry.title,
                    "summary": getattr(entry, "summary", ""),
                    "link": entry.link,
                    "source": getattr(feed.feed, "title", url),
                }
            )

    return items
