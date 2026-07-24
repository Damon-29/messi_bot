from bot.modules.rss import RSSModule
from bot.state import exists, add


def main():
    rss = RSSModule("https://feeds.feedburner.com/TheHackersNews")

    posts = rss.fetch()

    new_posts = 0

    for post in posts:
        if exists("rss", post.id):
            continue

        from bot.services.discord import send_post

        send_post(post)

        add("rss", post.id)
        new_posts += 1

    print(f"\nFound {new_posts} new posts.")


if __name__ == "__main__":
    main()
