import mysql.connector 


)


mydb = mysql.connector.connect(

  host="",

  user="",

  password="",

  database=""

)

@bot.command()
@commands.check(is_it_me)
async def local(ctx,arg):

    try:

        mycursor = mydb.cursor()

        embedlocaldb = discord.Embed(title="", color=0x000000)

        sql="SELECT * FROM change1 WHERE change2 LIKE "+"'%"+arg+"%'"+";"  # change1 with mysql table, change2 with table field name 

        mycursor.execute(sql)

        result=mycursor.fetchall()

        embedlocaldb.add_field(name="Found:", value=result[0],inline=False)

        await ctx.send(embed=embedlocaldb)

        return

    except:
        
        embedlocaldb = discord.Embed(title="", color=0x000000)
        await ctx.send(embed=embedlocaldb)
