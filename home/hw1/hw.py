import random
HANGMANPICS = ['''

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

def displayBoard(HANGMANPICS, missedletters, correctLetters,secretWord):
    print(HANGMANPICS[len(missedLetters)])
    print()

    print('Неправильные буквы:', end=' ')
    for letter in missedLetters:
        print(letter, end=' ')
    print()

    blanks = '_'*len(secretWord)

    for i in  range(len(secretWord)):
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
        if len(guess) != 1:
            print('Ваша буква:')
        elif guess in alreadyGuessed:
            print ('Вы уже пробовали эту букву. Выберите другую')
        elif guess not in 'ёйцукенгшщзхъфывапролджэячсмитьбю':
            print('Пожалуйста, введите букву кириллицы')
        else:
            return guess

def playAgain():
    print('Хотите попробовать еще раз? ("Да" или "Нет")')
    return input().lower().startswith('д')

print("Выберите одну из 3 тем:"
          "рок-группы (одно слово на русском; для выбора темы наберите цифру 1)"
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
missedLetters = ''
correctLetters = ''
secretWord = getRandomWord(words)
print('Ваше слово состоит из ', len(secretWord), 'букв. У вас есть 6 попыток.')
gameIsDone = False

while True:
    displayBoard(HANGMANPICS, missedLetters, correctLetters, secretWord)

    guess = getGuess(missedLetters+correctLetters)

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
        missedLetters = missedLetters+guess

        if len(missedLetters) == len(HANGMANPICS) - 1:
            displayBoard(HANGMANPICS, missedLetters, correctLetters, secretWord)
            print('У вас не осталось попыток!\n После '+str(len(missedLetters))+' ошибок и '+str(len(correctLetters))+'угаданных букв. Загаданное слово:'+secretWord+'"')
            gameIsDone = True

    if gameIsDone:
        if playAgain():
            missedLetters = ''
            correctLetters = ''
            gameIsDone = False
            secretWord = getRandomWord(words)
        else:
            break

