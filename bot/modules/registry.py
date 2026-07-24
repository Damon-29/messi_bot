from bot.modules.rss import RSSModule
from bot.modules.youtube import YouTubeModule


def load_modules(config):
    modules = []

    for feed in config.get("rss", []):
        modules.append(
            RSSModule(
                url=feed["url"]
            )
        )

    for channel in config.get("youtube", []):
        modules.append(
            YouTubeModule(channel)
        )

    return modules
