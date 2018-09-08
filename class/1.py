import random
letters = 'abcdefghijklmnopqrstuvwxyz'
alp = [i for i in letters]
letter = random.choice(alp)
ind = alp.index(letter) + 1
while True:
    print("Букву мне. Английскую. Пожалуйста.")
    a = input()
    if a in alp:
        if a == letter:
            print("Успех.")
            break
        elif a != letter:
            index = alp.index(a) + 1
            if index < ind:
                print("Правее.")
                continue
            else:
                print("Левее.")
                continue
    else:
        print("Миссия провалена.")
        continue




