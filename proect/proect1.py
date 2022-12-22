import discord
import random 
from discord_components import DiscordComponents,Button,ButtonStyle

def read_file(file_name):
    file=open(file_name,"r",encoding="UTF-8")
    list_file=file.read().split("\n")
    file.close()
    return random.choice(list_file)

client=discord.Client()

@client.event
async def on_message(message):
    if message.content.startswith("привет"):
        await message.channel.send(read_file("proect/priv.txt"))
    elif message.content.startswith("как дела?"):
        await message.channel.send(read_file("proect/cac.txt"))
    elif message.content.startswith("мне вообще это надо ?") :
        await message.channel.send("да!")
    elif message.content.startswith("/help"):
        await message.author.send("все мои команды :3\n /cn-вызывает панель кнопок отвечающих за вопрос'чем заняться на выходных'\nигры-эта кнопка выдаст рандомную игру\nаниме-выдвёт рандомное из понравившихся автору аниме\nдоставка еды-выдаст ссылку где можно заказать поесть\nразвличение-даст пример как можно себя занять\nсоветы от автора-совет от автора") 
    elif message.content.startswith("/cn"):
        await message.channel.send (
            embed=discord.Embed(title="нажимай на любую->"),
            components=[
                Button(style=ButtonStyle.green,label="игры"),
                Button(style=ButtonStyle.grey,label="аниме"),  
                Button(style=ButtonStyle.red,label="доставка еды"),  
                Button(style=ButtonStyle.grey,label="развлечение"),  
                Button(style=ButtonStyle.green,label="советы от автра"),
            ]
        )

        r=await client.wait_for("button_click")
        if r.component.label=="игры":
            await r.respond(content=read_file("proect/igr.txt"))
        if r.component.label=="аниме":
            await r.respond(content=read_file("proect/film.txt"))
        if r.component.label=="доставка еды":
            await r.respond(content=read_file("proect/eat.txt"))
        if r.component.label=="развлечение":
            await r.respond(content=read_file("proect/igre.txt"))
        if r.component.label=="советы от автора":
            await r.respond(content=read_file("proect/awtor.txt"))

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




client.run("MTA1NDc5MzgwOTA1OTM5NzY5Mg.GvJcuv.1Hw8EjBowGYeuOsR8mEhDGNRhG-nkbFEs8J9EU")
