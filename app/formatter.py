def format_wechat(items):
    lines = ["# 今日AI科技新闻", ""]

    for i, item in enumerate(items, 1):
        lines.append(f"{i}. **{item['source']}**")
        lines.append(f"> {item['ai']}")
        lines.append(f"> [原文]({item['link']})")
        lines.append("")

    return "\n".join(lines)


def format_telegram(items):
    lines = ["今日 AI 新闻", ""]

    for i, item in enumerate(items, 1):
        lines.append(f"{i}. {item['ai']}")
        lines.append(item["link"])
        lines.append("")

    return "\n".join(lines)
