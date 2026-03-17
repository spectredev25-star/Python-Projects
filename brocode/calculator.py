#CALCULATOR PROGRAM

print('===A MINI CALCULATOR BY SPECTRE===')

OPERATORS = ['+','-','/','*']

#FUNCTION TO GET FIRST NUMBER
def get_first_num():
    while True:
        num1 = input('FIRST NUMBER: ')
        if num1.isdigit():
            num1 = float(num1)
            break
        else:
            print('ENTER A VALID NUMBER')
    return num1

#FUNCTION TO GET OPERATOR
def get_operator():
    while True:
        operator = input('OPERATOR(+,-,*,/): ')
        if operator not in OPERATORS:
            print('OPERATORS MUST BE EITHER + OR - OR * OR /')
        else:
            break
    return operator

#FUCTION TO GET SECOND NUMBER 
def get_second_num():
    while True:
        num2 = input('SECOND NUMBER: ')
        if num2.isdigit():
            num2 = float(num2)
            break
        else:
            print('ENTER A VALID NUMBER')
    return num2


def main():
    num1 = get_first_num()
    operator = get_operator()
    num2 = get_second_num()
    result_statement = f'{num1} {operator} {num2}'
    print(result_statement)
    if operator == '+':
        result = num1 + num2
    elif operator == '-':
        result = num1 - num2
    elif operator == '*':
        result = num1 * num2
    elif operator == '/':
        result = num1 / num2
    else:
        print('INVALID REQUEST')
    print(result)

if __name__ == '__main__':
    main()