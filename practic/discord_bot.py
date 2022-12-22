# from discord.ext import commands

import discord
import random 
from discord_components import DiscordComponents,Button,ButtonStyle


# bot=commands.Bot(command_prefix="/")

client=discord.Client()

def read_file(file_name):
    file=open(file_name,"r",encoding="UTF-8")
    list_file=file.read().split("\n")
    file.close()
    return random.choice(list_file)

@client.event
async def on_message(message):
    if message.content.startswith("привет"):
        await message.channel.send(read_file("privet.txt"))
    elif message.content.startswith("покажи пейзаж"):
        await message.channel.send(read_file("pikcher.txt"))
    elif message.content.startswith("подбери картинку на рабочий стол"):
        await message.channel.send("https://www.google.ru/search?q=%D0%BA%D0%B0%D1%80%D1%82%D0%B8%D0%BD%D0%BA%D0%B8&tbm=isch&hl=ru&chips=q:%D0%BA%D0%B0%D1%80%D1%82%D0%B8%D0%BD%D0%BA%D0%B8,g_1:%D1%80%D0%B0%D0%B1%D0%BE%D1%87%D0%B8%D0%B9+%D1%81%D1%82%D0%BE%D0%BB:5ndx41kUi9c%3D&sa=X&ved=2ahUKEwjns97btur7AhWLp4sKHWZvDD8Q4lYoA3oECAEQKg&biw=1519&bih=656")
    elif message.content.startswith("где поесть?"):
        await message.channel.send(read_file("eat.txt"))
    elif message.content.startswith("завтра идти в школу?") or message.content.startswith("пойти гулять?"):
        await message.channel.send(read_file("answer..txt"))
    elif message.content.startswith("рандом число"):
        await message.channel.send(random.randint(0,100))
    elif message.content.startswith("/clear"):
        await message.channel.purge()
    elif message.content.startswith("/c25"):
        await message.channel.purge(limit=26)
    elif message.content.startswith("в лс"):
        await message.author.send("написал")
    elif message.content.startswith("пришли мне фото Дмитрия Масленникова"):
        await message.author.send(read_file("materials/photo"))
    elif message.content.startswith("пришли мне видео Дмитрия Масленникова"):
        await message.author.send(read_file("materials/videos"))
    elif message.content.startswith("пришли мне статьи про Дмитрия Масленникова"):
        await message.author.send(read_file("materials/articles"))
    elif message.content.startswith("/b"):
        await message.channel.send (
            embed=discord.Embed(title="нажимай на любую->"),
            components=[
                Button(style=ButtonStyle.red,label="google"),
                Button(style=ButtonStyle.grey,label="yandex"),  
                Button(style=ButtonStyle.green,label="wb"),  
                Button(style=ButtonStyle.blue,label="ozon"),  
                Button(style=ButtonStyle.red,label="pixel"),
            ]
        )
        r=await client.wait_for("button_click")
        if r.component.label=="google":
            await r.respond(content="https://www.google.com/")
        elif r.component.label=="yandex":
            await r.respond(content="https://www.yandex.com/")
        elif r.component.label=="wb":
            await r.respond(content="https://www.wildberries.ru/")
        elif r.component.label=="ozon":
            await r.respond(content="https://www.ozon.ru/")
        elif r.component.label=="pixel":
            await r.respond(content="https://clubpixel.ru/")


statuses=[
    discord.Status.dnd,
    discord.Status.do_not_disturb,
    discord.Status.invisible,
    discord.Status.idle,
    discord.Status.offline,
    discord.Status.online,
]

games=[
    "Minecraft",
    "GTA V",
    "Fortnite",
    "RDR 2",
    "CS:Go",
    "Sims 4",
]





@client.event
async def on_ready():
    DiscordComponents(client)
    print("бот готов служить")
    await client.change_presence(status=random.choice(statuses),activity=discord.Game(random.choice(games)))


client.run("MTA0OTcxODg5NTYwMDIyMjIwOA.GDhTtv.isEW2HtTscyRb3xzMRoBHGqW4cvUpBXGBC7vwU")
#@bot.command()
#async def hello(message):
    #await message.send("привет)")

#@bot.command()
#async def help_me(message):
    #await message.send("чем могу быть полезна?")

#@bot.command()
#async def all_commands(message):
    #await message.send("вот->\n /hello-приветсвие \n /help_me-вызов помощи")

#@bot.command()
#async def search (message):
    #await message.send("https://www.google.ru/")

#@bot.command()
#async def play (message):
    #await message.send("https://kanobu.ru/games/pc/popular/?ysclid=lbcftaptsu72864571")

#@bot.command()
#async def eat (message):
    #await message.send("https://www.delivery-club.ru/?ysclid=lbcfvf9ox7981240563")

#bot.run("MTA0OTcxODg5NTYwMDIyMjIwOA.GDhTtv.isEW2HtTscyRb3xzMRoBHGqW4cvUpBXGBC7vwU")

