# Temp Bans a member from server 
@bot.command()

async def tempban(ctx, member: commands.MemberConverter, duration: DurationConverter):
    
    multiplier = {'s': 1, 'm': 60}
    amount, unit = duration
    
    await ctx.guild.ban(member)
    await ctx.send (f'{member} has been banned for {amount}{unit}.')
    await asyncio.sleep(amount * multiplier[unit])
    await ctx.guild.unban(member)
    await ctx.guild.unban(f'{member} has been unbaned.')
