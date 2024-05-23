# Random module and import
# Hangman game
import random
HANGMANPICS = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']
answer = random.randint(1,10)
# print(answer)
i = 0
while(i<=6):
    
    guess = int(input('Guess the number:'))

    if guess == answer:
        print('Its correct you won!')
        break
    else:
        print(HANGMANPICS[i])
        i+=1
        print("Sorry wrong guess!")
    if (i==7):
        print("And you lost!")