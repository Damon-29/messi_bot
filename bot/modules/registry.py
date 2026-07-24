from bot.modules.rss import RSSModule


def load_modules(config):
    modules = []

    for feed in config.get("rss", []):
        modules.append(
            RSSModule(
                url=feed["url"]
            )
        )

    return modules
