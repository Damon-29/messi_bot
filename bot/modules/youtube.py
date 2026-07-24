from bot.modules.rss import RSSModule


class YouTubeModule(RSSModule):
    def __init__(self, channel_id: str):
        url = f"https://www.youtube.com/feeds/videos.xml?channel_id={channel_id}"

        super().__init__(
            url=url,
            source="youtube",
        )
