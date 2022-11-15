while True:
    word= "яблоко"
    print("угадай слово : я****о . Подсказка->это фрукт")
    ans=input("ответ->")
    if word==ans:
        print("отлично,ты угадал")
        break
    else:
        print("жаль,ты не угадал")