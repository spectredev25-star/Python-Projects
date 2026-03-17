#temperature converter

UNITS = ['K','C']


def get_temp():
    while True:
        temp = input('TEMPERATURE: ')
        if temp.isdigit():
            temp = int(temp)
            break
        else:
            print('TEMPERATURE MUST BE A VALID NUMBER!!!')
    return temp

def get_unit():
    while True:
        unit = input('K or C: ')
        if unit.upper() in UNITS:
            break
        else:
            print('UNIT MUST BE EITHER K OR C: ')
    return unit

def main():
    temp = get_temp()
    unit = get_unit()

    if unit.upper() == 'C':
        temp += 273
    else:
        temp -= 273
    print(f'{temp} {unit.upper()}')

if __name__ == '__main__':
    main()