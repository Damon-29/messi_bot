from bot.models.post import Post
from bot.services.discord import send_post


def main():
    post = Post(
        id="1",
        source="reddit",
        title="🚀 Personal Bot Test",
        body="If you're seeing this embed, the formatter works perfectly.",
        url="https://github.com/",
        author="ChatGPT",
        thumbnail="https://github.githubassets.com/images/modules/logos_page/GitHub-Mark.png",
    )

    send_post(post)


if __name__ == "__main__":
    main()
