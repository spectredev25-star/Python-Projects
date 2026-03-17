foods = []
prices= []
quit = False
total = 0

def get_food():
    while True:
        food = input('ENTER NAME OF FOOD: ')
        if food.lower() == 'q':
            quit()
        else:
            return food


def get_price():
    while True:
        price = input('ENTER PRICE: ')
        if price.isdigit():
            price = float(price)
            break
        else:
            print('PRICE MUST BE A NUMBER.')
    return price



def main():
    while quit != True:
        food = get_food()
        price = get_price()
        foods.append(food)
        prices.append(price)
        total = sum(prices)
    for food in foods:
        for price in prices:
            print(f'{food} COSTS ${prices}')

if __name__ == '__main__':
    main()