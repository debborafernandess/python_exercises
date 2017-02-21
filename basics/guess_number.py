import random

secretNumber = random.randint(1, 20)
print('I am thingking of a number between 1 and 20')

for guessesTaken in range(1, 7):
    print('Take a guess')
    guess = int(input())

    if guess < secretNumber:
      print('Your guess is to low')
    elif guess > secretNumber:
      print('Your guess is to high')
    else:
      break

if guess == secretNumber:
  print('You find me in ' + str(guessesTaken) + ' guesses!')
else:
  print('I was ' + str(secretNumber) + ' better lucky another time!')
