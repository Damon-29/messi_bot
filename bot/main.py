from bot.bot import Bot
from bot.modules.rss import RSSModule


def main():
    bot = Bot(
        modules=[
            RSSModule("https://feeds.feedburner.com/TheHackersNews"),
        ]
    )

    bot.run()


if __name__ == "__main__":
    main()
