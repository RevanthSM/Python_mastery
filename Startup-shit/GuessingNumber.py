import random
a = random.randint(1,6)
print(int(a))
for i in range(1,6):
    guess = int(input('Guess the number:'))
    if guess>a:
        print('Guess lower number')
    elif guess<a:
        print('Guess higher number')
    elif(guess == a):
        print("Your guess is correct!")
        break
    else:
        continue