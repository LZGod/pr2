import random
PICS = ['''

    +---+
    |   |
        |
        |
        |
        |
=========''','''

    +---+
    |   |
    O   |
        |
        |
        |
=========''','''

    +---+
    |   |
    O   |
    |   |
        |
        |
=========''','''

    +---+
    |   |
    O   |
   /|   |
        |
        |
=========''','''

    +---+
    |   |
    O   |
   /|\  |
        |
        |
=========''','''

    +---+
    |   |
    O   |
   /|\  |
   /    |
        |
=========''','''

    +---+
    |   |
    O   |
   /|\  |
   / \  |
        |
=========''']

def get_data(file_name):
    with open(file_name, encoding = "utf-8") as f:
        w = f.read()
        words = w.split()
    return words

def getRandomWord(wordList):
    wordIndex = random.randint(0, len(wordList) - 1)
    return wordList[wordIndex]

def displayBoard(PICS, wrongletters, correctLetters, secretWord):
    print(PICS[len(wrongLetters)])
    print()

    print('Неправильные буквы:', end=' ')
    for letter in wrongLetters:
        print(letter, end=' ')
    print()

    blanks = '_'*len(secretWord)

    for i in range(len(secretWord)):
        if secretWord[i] in correctLetters:
            blanks = blanks[:i] + secretWord[i] + blanks[i+1:]

    for letter in blanks: 
        print(letter, end=' ')
    print()

def getGuess(alreadyGuessed):
    while True:
        print('Введите букву')
        guess = input()
        guess = guess.lower()
        if len(guess) == 1:
            print('Ваша буква:', guess)
        elif guess in alreadyGuessed:
            print ('Вы уже пробовали эту букву. Выберите другую')
        elif guess not in 'ёйцукенгшщзхъфывапролджэячсмитьбю':
            print('Пожалуйста, введите букву кириллицы')
        else:
            return guess

def playAgain():
    print('Хотите попробовать еще раз? ("да" или "нет")')
    return input().lower().startswith('д')

if __name__ == '__main__':
    nam = ''
    print("Выберите одну из 3 тем:"
          "рок-группы (одно слово на русском, без артиклей; для выбора темы наберите цифру 1)"
          "режиссеры (фамилия на русском; для выбора темы наберите цифру 2)"
          "индейцы (племя на русском; для выбора темы наберите цифру 3)")
    i = input()
    if i == '1':
        nam = "roc.txt"
    elif i == '2':
        nam = "dir.txt"
    elif i == '3':
        nam = "ind.txt"
    words = get_data(nam) 
    print('В И С Е Л И Ц А')
    wrongLetters = ''
    correctLetters = '' 
    secretWord = getRandomWord(words)
    gameIsDone = False

    while True:
        displayBoard(PICS, wrongLetters, correctLetters, secretWord)
        
        guess = getGuess(wrongLetters+correctLetters)
        if guess in secretWord:
            correctLetters = correctLetters + guess
            foundAllLetters = True
            for i in range(len(secretWord)):
                if secretWord[i] not in correctLetters:
                    foundAllLetters = False
                    break
                if foundAllLetters:
                    print('Было загадано слово "'+secretWord+'"! Вы победили!')
                    gameIsDone = True
        else:
            wrongLetters = wrongLetters+guess
            if len(wrongLetters) == len(PICS) - 1:
                displayBoard(PICS, wrongLetters, correctLetters, secretWord)
                print('У вас не осталось попыток!\nПосле '+str(len(wrongLetters))+' ошибок и '+str(len(correctLetters))+'угаданных букв. Загаданное слово:'+secretWord+'"')
                gameIsDone = True

        if gameIsDone:
            if playAgain():
                wrongLetters = ''
                correctLetters = ''
                gameIsDone = False
                secretWord = getRandomWord(words)
        else:
            break
    
