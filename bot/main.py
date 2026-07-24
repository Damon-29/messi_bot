from bot.bot import Bot
from bot.config import CONFIG
from bot.modules.rss import RSSModule


def main():
    modules = []

    for feed in CONFIG.get("rss", []):
        modules.append(
            RSSModule(
                url=feed["url"]
            )
        )

    bot = Bot(modules)
    bot.run()


if __name__ == "__main__":
    main()
