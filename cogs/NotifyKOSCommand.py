from discord.ext.commands import Bot, Cog, command, Context
import settings


class NotifyKOSCommand(Cog):
    bot: Bot

    def __init__(self, bot: Bot):
        self.bot = bot

    @command("notify-kos")
    async def notify_kos(self, ctx: Context):
        notify_role = ctx.guild.get_role(settings.KOS_NOTIFY_ROLE_ID)
        author_roles = ctx.author.roles

        author_have_notify_role = False
        for author_role in author_roles:
            if author_role.id == notify_role.id:
                author_have_notify_role = True
                break

        if author_have_notify_role:
            return ctx.reply(settings.LANGUAGE.ALREADY_HAVE_ROLE_MSG)

        await ctx.author.add_roles(notify_role)
        await ctx.reply(settings.LANGUAGE.ROLE_ADDED_MSG)


async def setup(bot: Bot):
    await bot.add_cog(NotifyKOSCommand(bot))
