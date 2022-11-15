from time import sleep 
from random import choice

def timer (n):
    for i in range(n,-1,-1):
        sleep(1)
        print(i)


words =["яблоко","персик","банан","клубника"]
while True:
    word= choice(words)
    first=word[0]
    last=word[len(word)-1]
    print("угадай слово")
    print("первая буква-"+first)
    print("последняя буква-"+last)
    print("длина слова-"+str(len(word)))
    timer(5)
    ans=input("ответ->")
    timer(3)
    if word==ans:
        print("отлично,ты угадал")
        break
    else:
        print("жаль,ты не угадал")
