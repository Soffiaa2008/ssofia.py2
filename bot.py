import random

greetings=["Привет","Здравствуй","Приветствую"]
affairs=["отлично","хорошо","нормально","плохо","так себе","пойдет"]
plans=["поесть","поспать","никаких","мне лень что либо делать)","прогуляться"]
isHello=False
isAffairs=False
isPlans=False
while True:

    message=input("я:").lower()
    
    if message =="привет":
        if  not isHello:
            print("бот: "+ random.choice(greetings))
            isHello=True
        else:
            print("бот:уже здоровались!")
        
    if  not isHello :
        print("бот:а поздоророваться:(")

    if message =="как дела?" and isHello:
        if not isAffairs:
            print("бот: "+ random.choice(affairs))
            isAffairs=True
        else:
            print("бот:уже спрашивал!")




    if message =="какие планы?" and isHello:
        if not isPlans:
            print("бот: "+ random.choice(plans))
            isPlans=True
        else:
            print("бот: я уже говорил тебе!")


















