@bot.event
async def on_ready():
    """
    Displays Bot information.
    """
    print(
        f"---\n Logged in as: {bot.user.name} : {bot.user.id}\n----\n My current prefix is: .\n----"
    )
    await bot.change_presence(
        activity=discord.Game(
            name=f"Hi, my names {bot.user.name},\nUse . to interact with me!"
        )
    )  # This changes the bots activity
