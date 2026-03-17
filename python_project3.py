#rock paper scissors game

import random
choices = ['r','p','s']
emojis = {
    'r':'🥌',
    's':'✂',
    'p':'📃',
}
quit = False

def get_computerChoice():
    computer_choice = random.choice(choices)
    return computer_choice

def get_userChoice():
    user_choice = input('PAPER,SCISSORS,ROCK(p,s,r): ').lower()
    while True:
        if user_choice in choices:
            break
        else:
            print('ENTER A VALID INPUT(p,s,r)')
    return user_choice



def displayChoice(computer_choice,user_choice):
    print(f'COMPUTER CHOSE:{emojis[computer_choice]}')
    print(f'YOU CHOSE:{emojis[user_choice]}')

def match_choice(computer_choice,user_choice):
    if computer_choice == user_choice:
        print('IT IS A TIE')
    elif (computer_choice == 'r' and user_choice == 's') or (computer_choice == 'p' and user_choice == 'r') or (computer_choice == 's' and user_choice == 'p'):
        print('COMPUTER WINS')
    else:
        print('YOU WON!!!')


while quit != True:
    computer_choice = get_computerChoice()
    user_choice = get_userChoice()
    displayChoice(computer_choice,user_choice)
    match_choice(computer_choice,user_choice)

    response = input('WANT TO PLAY AGAIN*(y/n): ')
    if response.lower() == 'n':
        break