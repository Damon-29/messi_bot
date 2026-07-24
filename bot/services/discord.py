from discord_webhook import DiscordWebhook

from bot.config import DISCORD_WEBHOOK


def send_message(message: str):
    webhook = DiscordWebhook(
        url=DISCORD_WEBHOOK,
        content=message
    )

    webhook.execute()
