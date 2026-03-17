#adddres book

contacts = []
contact = {}

options = '''
1).ADD A CONTACT
2).EDIT A CONTACT
3).DISPLAY ALL CONTACT
 4).QUIT
'''

print('SPECTRE SIMPLE ADDRESS BOOK')

def getChoice():
    while True:
        choice = input('WHAT OPERATION WOULD YOU LIKE TO PERFORM ON THE ADDRESS BOOK? ')
        if choice.isdigit():
            choice = int(choice)
            break
        else:
            print(f'{choice} NOT A VALID DIGIT')
    return choice


def addContact():
    while True:
        name = input('NAME: ')
        number = input('NUMBER: ')
        if number.isdigit():
            number = int(number)
            contact['NAME'] = name.upper()
            contact['NUMBER'] = number
            contacts.append(contact)
            break
        else:
            print('INVALID NUMBER.')
    return contact

def editContact():
    while True:
        edit_contact = input('WHICH ADDRESS DO YOU WANT TO EDIT: ')
        if edit_contact.isdigit():
            edit_contact = int(edit_contact)
            break
        else:
            print('INPUT THE INDEX OF THE CONTACT')
    return edit_contact

while True:
    print(options)
    choice = getChoice()
    if choice == 1:
        contact = addContact()
    elif choice == 2:
        for contact in contacts:
            print(contact)
        edit_contact = editContact()
        if edit_contact in contact.value():
            edited_contact = input('NEW NUMBER:')

    elif choice == 3:
        for contact in contacts:
            for key,value in contact.items():
                print(f'{key}:{value}')
    elif choice ==4:
        break
    else:
        print('NUMBER MUST BE FROM 1 TO 0')
