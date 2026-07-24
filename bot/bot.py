from bot.services.discord import send_post
from bot.state import exists, add


class Bot:
    def __init__(self, modules):
        self.modules = modules

    def run(self):
        total_new = 0

        for module in self.modules:
            posts = module.fetch()

            for post in posts:
                if exists(post.source, post.id):
                    continue

                send_post(post)
                add(post.source, post.id)

                total_new += 1

        print(f"\nFinished. Sent {total_new} new posts.")
