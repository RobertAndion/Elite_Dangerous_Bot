from discord.ext import commands
class Greetings(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None

    @commands.Cog.listener()
    async def on_member_join(self, member):
        channel = member.guild.system_channel
        if channel is not None:
            await channel.send('Welcome {0.mention}.'.format(member))

    @commands.command()
    async def hello(self, ctx, *, member: discord.Member = None):
        """Says hello"""
        member = member or ctx.author
        if self._last_member is None or self._last_member.id != member.id:
            await ctx.send('Hello {0.name}~'.format(member))
        else:
            await ctx.send('Hello {0.name}... This feels familiar.'.format(member))
        self._last_member = member

    @commands.command(name = 'kick', aliases = ['boot'],description="Used by admins to kick members") #working kick command
    @commands.has_permissions(ban_members=True, kick_members=True)
    async def kick_user(self,ctx, member : discord.Member, *, reason =None):
        await member.kick(reason=reason)
        await ctx.channel.send(member.display_name + " was kicked.")