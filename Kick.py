# Kicks member from server
@commands.check(is_it_me)

async def kick(ctx, member : discord.Member, *, reason=None):
    await member.kick(reason=reason)
    
    
    

class DurationConverter(commands.Converter):
    
    async def convert(self, ctx, argument):
        amount = argument[:-1]
        unit = argument[-1]
        
        if amount.isdigit() and unit in ['s', 'm']:
            return (int(amount), unit)
        
        raise commands.BadArgument(message='Not a vaild duration')
