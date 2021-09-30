from os import system, name
from time import sleep


def clear():
    if name == 'nt':
        _ = system('cls')

    else:
        _ = system('clear')


def options():
    print('you think to yourself about your available options at this point...')
    sleep(2)
    print('you could')
    sleep(0.2)
    print('fuel')
    sleep(0.2)
    print('checkcar')
    sleep(0.2)
    print('checkdistances')
    sleep(0.2)
    print('speed')
    sleep(0.2)
    print('quit')
    sleep(1)
    print('drive')
    print('...')
    sleep(1)
    print('yeah..that seems about right, what next')
