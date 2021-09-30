
from os import system, name
from time import sleep


def clear():
    if name == 'nt':
        _ = system('cls')

    else:
        _ = system('clear')


def intro1():
    print('They\'re coming for you, you need to get away...')
    sleep(2)
    print('You will need to maintain the fuel of your car, your speed')
    print('and also the distance away from the people trying to catch you...')
    sleep(6)
    print('Your fuel value begins at 100')


def intro2():
    sleep(6)
    print('You will need to refuel your car and check speed and levels etc.')
    print('this will take a precious turn in which your enemy can catch up')
    print('the maximum speed available is 100mph...')
    sleep(10)
    print('let me remind you that a commands list can be displayed by typing "help"')
    sleep(3)
    print('Your available commands are:')
    sleep(0.2)
    print('fuel (fuel the car)')
    sleep(0.2)
    print('checkcar (check fuel lv)')
    sleep(0.2)
    print('checkdistances (display distance to finish and distance from enemy')
    sleep(0.2)
    print('speed (set speed 1-100 reccomended)')
    sleep(0.2)
    print('enditnow (exit the game)')
    sleep(0.2)
    print('drive(drive at your set pace)')
    sleep(1)
    print('...')
    sleep(2)
    print('...')
    sleep(1)
    print('good luck, type anything to continue, or "quit" to quit')
