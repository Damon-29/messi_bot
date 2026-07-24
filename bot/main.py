from bot.modules.rss import RSSModule
from bot.state import exists, add
from bot.services.discord import send_post


def main():
    rss = RSSModule("https://feeds.feedburner.com/TheHackersNews")

    posts = rss.fetch()

    new_posts = 0

    for post in posts:
        if exists("rss", post.id):
            print(f"⏩ Skipping: {post.title}")
            continue

        print(f"📨 Sending: {post.title}")

        send_post(post)
        add("rss", post.id)
        new_posts += 1

    print(f"\n✅ Found {new_posts} new posts.")


if __name__ == "__main__":
    main()
