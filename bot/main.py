from bot.state import has_post, add_post

POST_ID = "reddit_123"

if has_post(POST_ID):
    print("Already posted.")
else:
    print("New post.")
    add_post(POST_ID)
