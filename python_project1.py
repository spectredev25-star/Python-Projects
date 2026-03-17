# basic python dice rolling program

#import random module
import random 
quit = False

#loop while user choice is not n
while quit != True:
    choice = input('Roll the dice?(y/n): ')
    if choice.lower() == 'y':
        num1 = random.randint(1,6)
        num2 = random.randint(1,10)
        print(f'You rolled {num1} and {num2}')
        continue
    elif choice.lower() == 'n':
        print('Thanks for playing!')
        quit == True
        break
    else:
        print('INVALID CHOICE!!!')


