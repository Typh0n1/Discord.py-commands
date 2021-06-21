# Bans member from server 
@commands.check(is_it_me)

async def ban(ctx,member : discord.Member, *, reason=None):
    await member.ban(reason=reason)
    await ctx.send(f'{member.mention} has been banned. ')
