class Bot:
    def __init__(self, modules):
        self.modules = modules

    def run(self):
        total_new = 0

        for module in self.modules:
            print(f"\nChecking {module.__class__.__name__}...")

            posts = module.fetch()

            print(f"Fetched {len(posts)} posts")

            for post in posts:
                if exists(post.source, post.id):
                    continue

                print(f"Sending: {post.title}")

                send_post(post)
                add(post.source, post.id)

                total_new += 1

        print(f"\nFinished. Sent {total_new} new posts.")
