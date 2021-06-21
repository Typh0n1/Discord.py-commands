# Clears specified amount of messages
@bot.command()
@commands.check(is_it_me)

async def clear(ctx, amount=5):
    await ctx.channel.purge(limit=amount)
