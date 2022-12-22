import telebot 
from random import choice
import wikipedia

wikipedia.set_lang("ru")
line=2



token="5902139674:AAHZsYlr-fGmSpjVzFlTYcOBBWxo8jxOxUA"
bot=telebot.TeleBot(token)

@bot.message_handler(commands=["hello"])
def sendMessage(mess):
    bot.reply_to(mess,"привет)")

@bot.message_handler(commands=["helloger"])
def sendMessage(mess):
    bot.reply_to(mess,"Hallo")

@bot.message_handler(commands=["hellofranc"])
def sendMessage(mess):
    bot.reply_to(mess,"salut")

@bot.message_handler(commands=["getImage"])
def getImage(mess):
    bot.send_photo("")
#    bot.reply_to(mess,"https://yandex.ru/images/search?text=%D0%BA%D1%83%D1%80%D1%81%D0%B5%D0%B4%D1%8D%D0%BC%D0%BE%D0%B4%D0%B6%D0%B8&from=tabbar&pos=6&img_url=http%3A%2F%2Fpbs.twimg.com%2Fmedia%2FEjPi2bmXgAUpJ8h.jpg&rpt=simage&lr=10923")

@bot.message_handler(commands=["help"])
def sendHelp(mess):
    bot.reply_to(mess,"существующие команды: \n /hello-приветствие;\n/getImage-выдаёт картинки;\n/hoppy-раскажет о моих увлечениях;\n/helloger-на немецком скажет привет;\n/hellofranc-скажет на французском привет")

@bot.message_handler(commands=["hoppy"])
def sendHppy(mess):
    bot.reply_to(mess,"у меня мало увлечений:(\nно я очень люблю рисовать и програмировать:)")

@bot.message_handler(commands=["getAudio"])
def getAudio(mess):
    bot.send_audio(mess.chat.id,audio=open("0eb24fcad1bffed.mp3","rb"))

@bot.message_handler(commands=["support"])
def buttons(message):
    markup=telebot.types.ReplyKeyboardMarkup()
    b1=telebot.types.KeyboardButton("завис комп")
    b2=telebot.types.KeyboardButton("где купить комп?")
    b3=telebot.types.KeyboardButton("вещи для компа")
    b4=telebot.types.KeyboardButton("факты")
    b5=telebot.types.KeyboardButton("игры")
    
    
    b6=telebot.types.KeyboardButton("короткие заметки")
    b7=telebot.types.KeyboardButton("средние заметки")
    b8=telebot.types.KeyboardButton("длинные заметки")
    
    markup.add(b1)
    markup.add(b2)
    markup.add(b3)
    markup.add(b4)
    markup.add(b5)

    markup.add(b6)
    markup.add(b7)
    markup.add(b8)

    bot.send_message(message.chat.id,"что случилось?",reply_markup=markup)


def readFile(message,fileName):
        file=open(fileName,"r",encoding="UTF-8")
        listFile=file.read().split("\n")
        file.close()
        bot.reply_to(message,choice(listFile))





@bot.message_handler(func=lambda m:True)
def dialog(message):
    global line
    if message.text.lower() == "привет":
        readFile(message,"greetings.txt")
    elif message.text.lower() == "в какой магазин пойти?":
        readFile(message,"magaz.txt")
    elif message.text.lower() == "что делаешь?":
        readFile(message,"chto.txt")
    elif message.text=="завис комп":
        readFile(message,"comp.txt")
    elif message.text=="где купить комп?":
        readFile(message,"byecomp.txt")
    elif message.text=="вещи для компа":
        readFile(message,"byev.txt")
    elif message.text=="факты":
        readFile(message,"play.txt")
    elif message.text=="игры":
        readFile(message,"ugry.txt")

    elif message.text=="короткие заметки":
        bot.reply_to(message,"настройка принята)")
        line=2
    elif message.text=="средние заметки":
        bot.reply_to(message,"настройка принята)")
        line=4
    elif message.text=="длинные заметки":
        bot.reply_to(message,"настройка принята)")
        line=10
    else:
        try:
            bot.send_message(message.chat.id,wikipedia.summary(message.text, sentences=line))
        except:
            bot.send_message(message.chat.id,"инфа не найдена")

    
@bot.message_handler(commands=["getImage"])
def getImage(mess):
    bot.send_photo(mess.chat.id, photo=open("malenikov-min."))



bot.polling()