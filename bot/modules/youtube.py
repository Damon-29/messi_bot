import feedparser

from bot.models.post import Post
from bot.modules.base import BaseModule


class YouTubeModule(BaseModule):
    def __init__(self, channel_id: str):
        self.url = (
            f"https://www.youtube.com/feeds/videos.xml?channel_id={channel_id}"
        )

    def fetch(self):
        feed = feedparser.parse(self.url)

        posts = []

        for entry in feed.entries:
            thumbnail = ""

            if "media_thumbnail" in entry:
                thumbnail = entry.media_thumbnail[0]["url"]

            posts.append(
                Post(
                    id=entry.yt_videoid,
                    source="youtube",
                    title=entry.title,
                    url=entry.link,
                    body=entry.summary,
                    author=entry.author,
                    timestamp=entry.published,
                    thumbnail=thumbnail,
                )
            )

        return posts
