import os
from discord.ext import commands
from dotenv import load_dotenv
import urllib.request
import json

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
KEY = 'AIzaSyCDGzmR0EfiNkOnnlnbWE-kyqRsfUTnDlo'

bot = commands.Bot(command_prefix='!') #Prefijo del bot

@bot.command(name='subs') #Funcion que mostrara los suscriptores de un canal de Youtube que le pasemos como parametro
async def subscriptores(ctx,username):
    data = urllib.request.urlopen("https://www.googleapis.com/youtube/v3/channels?part=statistics&forUsername=" + username + "&key=" + KEY).read()
    subs = json.loads(data)["items"][0]["statistics"]["subscriberCount"]
    response = username + " tiene " + "{:,d}".format(int(subs)) + " suscriptores!"
    await ctx.send(response)

bot.run(TOKEN)