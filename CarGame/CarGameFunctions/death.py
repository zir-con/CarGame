from os import system, name
from time import sleep


def clear():
    if name == 'nt':
        _ = system('cls')

    else:
        _ = system('clear')


def speedDeath():
    print('you\'re driving very quickly, but it seems fine...')
    sleep(2)
    print('suddenly a deer runs across the road and you swerve to avoid it...')
    sleep(3)
    print('you go over the kerb, the car flips 3 times..')
    sleep(2)
    print('it stops when a tree impacts the side, bending the metal')
    print('and splintering the plastic firmly into your right shoulder and ribs...')
    sleep(4)
    print('there is burning pain for almost 8 minutes..')
    sleep(2)
    print('then everything starts to go numb, little by little...')
    sleep(5)
    print('it starts to become difficult to open your eyes')
    sleep(3)
    print('then difficult to breathe')
    sleep(2)
    print('you cough to make it easier to breathe...')
    sleep(1)
    print('but it only brings more pain and darkness...')
    print('the darkness envelops you and you close your eyes, never to open them again...')


def catchUpDeath():
    print('you turn around and see, they\'re getting closer')
    sleep(2)
    print('there are multiple bangs behind you, your car screeches off the road and collides with something')
    sleep(3)
    print('you see a deep flash of red cover the windscreen but it soon becomes difficult to hold your head up')
    sleep(3)
    print('...')
    sleep(1)
    print('then everything begins to go dark...')
    sleep(2)
    print('forever...')


def fuelDeath():
    print('the car sputters and comes to a stop, you\'re out of fuel.')
    print('you hurriedly get out of the car, but then realise there\'s no help to be found')
    sleep(1)
    print('an engine drives up behind you...')
    print('it\'s a black sedan, 2 men get out and a bag is thrown over your head')


