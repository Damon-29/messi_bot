from bot.bot import Bot
from bot.config import CONFIG
from bot.modules.registry import load_modules


def main():
    modules = load_modules(CONFIG)

    bot = Bot(modules)
    bot.run()


if __name__ == "__main__":
    main()
