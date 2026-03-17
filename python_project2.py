# number guessing game

# import random module
import random
secret_num = random.randint(1,100)
running = True

while running:
    try:
        guess_num = int(input('Guess a number between 1 and 100: '))
    except ValueError:
        print('INVALID INPUT,ENTER A VALID DIGIT')
        continue
    if guess_num > secret_num:
        print('TOO HIGH!!!')
        continue
    elif guess_num < secret_num:
        print('TOO LOW!!!')
        continue
    elif guess_num == secret_num:
        print('CONGRATULATIONS!!!,YOU GUESSED THE NUMBER')
        running = False

