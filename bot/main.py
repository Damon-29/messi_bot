from bot.modules.rss import RSSModule


def main():
    rss = RSSModule("https://feeds.feedburner.com/TheHackersNews")

    posts = rss.fetch()

    print(f"Fetched {len(posts)} posts\n")

    for post in posts[:5]:
        print(post.title)
        print(post.url)
        print("-" * 50)


if __name__ == "__main__":
    main()
