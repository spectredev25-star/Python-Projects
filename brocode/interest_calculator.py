def get_principle():
    while True:
        principle = input('INPUT PRINCIPAL: ')
        if principle.isdigit():
            principle = float(principle)
            if principle <= 0:
                print('PRINCIPLE MUST BE GREATER THAN 0.')
            else:
                break
        else:
            print('ENTER A VALID NUMBER')
    return principle

def get_time():
    while True:
        time = input('INPUT TIME: ')
        if time.isdigit():
            time = int(time)
            if time <= 0:
                print('TIME MUST BE GREATER THAN 0.')
            else:
                break
        else:
            print('ENTER A VALID NUMBER')
    return time
    

def get_rate():
    while True:
        rate = input('INPUT RATE: ')
        if rate.isdigit():
            rate = int(rate)
            if rate <= 0:
                print('RATE MUST BE GREATER THAN 0.')
            else:
                break
        else:
            print('ENTER A VALID NUMBER')
    return rate

def main():
    principle = get_principle()
    rate = get_rate()
    time = get_time()

    interest = (principle * rate *time)/100
    amount = principle + interest
    print(f'INTESERT TO BE PAID IS ${interest} AND AMOUNT TO BE PAID IS {amount}')

if __name__ == '__main__':
    main()