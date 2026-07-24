from discord_webhook import DiscordWebhook, DiscordEmbed

from bot.config import DISCORD_WEBHOOK
from bot.models.post import Post


def send_post(post: Post):
    webhook = DiscordWebhook(url=DISCORD_WEBHOOK)

    embed = DiscordEmbed(
        title=post.title,
        description=post.body[:4000] if post.body else "",
        url=post.url,
    )

    if post.thumbnail:
        embed.set_thumbnail(url=post.thumbnail)

    if post.images:
        embed.set_image(url=post.images[0])

    footer = post.source.upper()

    if post.author:
        footer += f" • {post.author}"

    embed.set_footer(text=footer)

    webhook.add_embed(embed)
    webhook.execute()
