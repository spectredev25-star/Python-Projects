import time

def get_my_time():
    while True:
        my_time = input('ENTER TIME IN SECONDS: ')
        if my_time.isdigit():
            my_time = int(my_time)
            break
        else:
            print('INPUT A VALID NUMBER')
    return my_time

def main():
    my_time = get_my_time()
    for i in range(my_time,0,-1):
        hr = int(i / 3600)
        mn = int(i / 60) % 60
        sc = i % 60
        print(f'{hr:02}:{mn:02}:{sc:02}')
        time.sleep(1)

if __name__ == '__main__':
    main()