import feedparser

from bot.models.post import Post
from bot.modules.base import BaseModule


class RSSModule(BaseModule):
    def __init__(self, url: str):
        self.url = url

    def fetch(self):
        feed = feedparser.parse(self.url)

        posts = []

        for entry in feed.entries:
            posts.append(
                Post(
                    id=entry.id if "id" in entry else entry.link,
                    source="rss",
                    title=entry.title,
                    url=entry.link,
                    body=entry.summary if "summary" in entry else "",
                    timestamp=entry.published if "published" in entry else "",
                )
            )

        return posts
