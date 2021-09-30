
# importing some useful functions

from os import system, name
from sys import exit
from time import sleep

from CarGameFunctions.DifAndConf import ok
from CarGameFunctions.IntroSequence import intro1
from CarGameFunctions.IntroSequence import intro2
from CarGameFunctions.LoadingSequence import loading
from CarGameFunctions.death import catchUpDeath
from CarGameFunctions.death import fuelDeath
from CarGameFunctions.death import speedDeath
from CarGameFunctions.options import options


def clear():
    if name == 'nt':
        _ = system('cls')

    else:
        _ = system('clear')


fuelValue = int(100)
enemyDistance = int(200)
currentSpeed = int(50)
distanceToFinish = int(0)
enemySpeed = int(0)
devMode = 'false'
play = 'yes'
maxspeed = 101
minspeed = 0
# important initial values for game balancing


loading()

while play == 'yes':
    print("please select a difficulty, \"easy\", \"normal\", or \"hard\"")
    dif: str = input()
    while dif == "easy" or "medium" or "hard":
        if dif == "easy":
            enemySpeed = int(30)
            distanceToFinish = int(1000)
            enemyDistance = int(200)
            break
        elif dif == "normal":
            enemySpeed = int(50)
            distanceToFinish = int(2500)
            enemyDistance = int(200)
            break
        elif dif == "hard":
            enemySpeed = int(70)
            distanceToFinish = int(5000)
            enemyDistance = int(200)
            break
        else:
            print("critical error")
            exit()
    else:
        print('please try again, please use lowercase')

    intro1()
    print('the enemy moves at ', enemySpeed, ' kph')
    print('and you need to go', distanceToFinish, ' kilometres')
    intro2()

    yn = input()

    if yn == 'quit':
        quit()
    elif yn == 'dev' or 'devmode':
        devMode = 'true'
        ok()
    else:
        ok()

    while distanceToFinish >= 0 and enemyDistance >= 0 and fuelValue >= 0:
        print('what next')
        game = input()
        if game == 'help':

            options()
            while devMode == 'true':

                print('fuel value is: ', fuelValue)
                print('enemy distance is: ', enemyDistance)
                print('enemy speed is: ', enemySpeed)
                print('distance to finish is: ', distanceToFinish)
                print('current speed is: ', currentSpeed)
                break

        elif game == 'checkcar':
            print('you get out and check, your car has got ', fuelValue, ' fuel left')
            enemyDistance -= 20
            while devMode == 'true':

                print('fuel value is: ', fuelValue)
                print('enemy distance is: ', enemyDistance)
                print('enemy speed is: ', enemySpeed)
                print('distance to finish is: ', distanceToFinish)
                print('current speed is: ', currentSpeed)
                break

        elif game == 'fuel':
            print('you fuel your vehicle and it is reset to 100 fuel')
            fuelValue = 100
            enemyDistance -= 50
            while devMode == 'true':

                print('fuel value is: ', fuelValue)
                print('enemy distance is: ', enemyDistance)
                print('enemy speed is: ', enemySpeed)
                print('distance to finish is: ', distanceToFinish)
                print('current speed is: ', currentSpeed)
                break
        elif game == 'quit':
            print('you quit the game')
            exit()
        elif game == 'checkdistances':
            print('the enemy is ', enemyDistance, 'km away')
            print('and you still need to go ', distanceToFinish, 'km')
            while devMode == 'true':

                print('fuel value is: ', fuelValue)
                print('enemy distance is: ', enemyDistance)
                print('enemy speed is: ', enemySpeed)
                print('distance to finish is: ', distanceToFinish)
                print('current speed is: ', currentSpeed)
                break
        elif game == 'speed':
            while devMode == 'true':
                print('fuel value is: ', fuelValue)
                print('enemy distance is: ', enemyDistance)
                print('enemy speed is: ', enemySpeed)
                print('distance to finish is: ', distanceToFinish)
                print('current speed is: ', currentSpeed)
                break
            print('how fast would you like to go? (0-100)')
            currentSpeed = input()

        # first lot of commands, explained below

        elif game == 'drive':
            if maxspeed > int(currentSpeed) > minspeed:
                print('you drive for an hour or so at ', currentSpeed, ' mph')
                fuelValue -= int(currentSpeed) / 2
                distanceToFinish -= int(currentSpeed)
                enemyDistance -= int(enemySpeed)
                enemyDistance += int(currentSpeed)
                while devMode == 'true':
                    print('fuel value is: ', fuelValue)
                    print('enemy distance is: ', enemyDistance)
                    print('enemy speed is: ', enemySpeed)
                    print('distance to finish is: ', distanceToFinish)
                    print('current speed is: ', currentSpeed)
                    break

            # drives the car
            elif int(currentSpeed) >= maxspeed:
                speedDeath()
                print('do you want to play again? yes/no')
                play = input()
                break
                # tells the user they died from going too fast
            else:
                print('you chose an invalid number, please make sure you chose a positive, whole integer')
        else:
            print('unknown command')
        # standard error message
    else:
        if distanceToFinish < 1:
            print('You breathe a sigh of relief...')
            sleep(1)
            print('You finally made it.')
            sleep(1)
            print('do you want to play again? yes/no')
            play = input()

        elif enemyDistance < 1:
            catchUpDeath()
            print('do you want to play again? yes/no')
            play = input()

            # this displays the user dying from being caught up to
        elif fuelValue < 1:
            fuelDeath()
            print('do you want to play again? yes/no')
            play = input()

        # this displays the user dying from running out of fuel
else:
    exit()
