from bot.state import exists, add

MODULE = "reddit"
POST_ID = "12345"

if exists(MODULE, POST_ID):
    print("Already exists.")
else:
    print("New post.")
    add(MODULE, POST_ID)
