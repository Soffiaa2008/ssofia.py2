import random

greetings=["Привет","Здравствуй","Приветствую"]
affairs=["отлично","хорошо","нормально","плохо","так себе","пойдет"]

isHello=False
isAffairs=False

while True:

    message=input("я:").lower()
    
    if message =="привет":
        if  not isHello:
            print("бот: "+ random.choice(greetings))
            isHello=True
        else:
            print("бот:уже здоровались!")
        


    if message =="как дела?" and isHello:
        if not isAffairs:
            print("бот: "+ random.choice(affairs))
            isAffairs=True
        else:
            print("бот:уже спрашивал!")
    elif  not isHello   :
        print("бот:а поздоророваться:(")
















