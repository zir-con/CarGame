from os import system, name
from time import sleep


def clear():
    if name == 'nt':
        _ = system('cls')

    else:
        _ = system('clear')


def ok():
    clear()
    sleep(1)
    print('you get a call, all it says is "they\'re coming for you", then the line goes dead')
    sleep(4)
    print('you hurry outside and grab a few fuel canisters and drive away')
    sleep(3)
    currentSpeed = 50
    print('you leave the house and are driving at ', currentSpeed, 'kph')
    sleep(3)
