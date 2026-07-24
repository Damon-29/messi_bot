from bot.modules.rss import RSSModule


def main():
    module = RSSModule()

    posts = module.fetch()

    print(f"Fetched {len(posts)} posts")


if __name__ == "__main__":
    main()
