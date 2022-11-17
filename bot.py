import random

greetings=["Привет","Здравствуй","Приветствую"]
affairs=["отлично","хорошо","нормально","плохо","так себе","пойдет"]

while True:

    message=input("я:").lower()
    
    if message =="привет":
        print("бот: "+ random.choice(greetings))
    elif message =="как дела?":
        print("бот: "+ random.choice(affairs))
















