import random
import os
import datetime


def cls():
    if (os.name == 'nt'):
        os.system('cls')
    else:
        os.system('clear')


def menu():
    cls()
    print('Welcome to my little project.')
    print('[1] Generate first poem')
    print('Poem about mask and feelings.')
    print('[2] Generate second poem')
    print('Poem changing with the seasons.')
    print('[E] Exit')
    odp = input('Wanna select an option?')
    if (odp == '1'):
        firstpoem()
    elif (odp == '2'):
        secondpoem()
    elif (odp == 'E' or odp == 'e'):
        pass
    else:
        print('Nonexistent option.')
        input('Press any key to continue...')
        menu()


def firstpoem():
    firstline = ['maska opadła', 'maska wraca', 'maska skruszała']
    secondline = ['zagubione ciało', 'zagubione serce', 'zagubiony umysł']
    thirdline = ['milknie i zanika', 'krzyczy w ciszy', 'cieszy się bólem']

    a = int(random.uniform(0, 3))
    b = int(random.uniform(0, 3))
    c = int(random.uniform(0, 3))

    print(firstline[a])
    print(secondline[b])
    print(thirdline[c])

    input('Press any key to continue...')
    menu()


def secondpoem():
    firstline = ['pierwsze kwiaty wiśni -', 'pierwsze płatki śniegu -', 'pierwsze złote liście -', 'słońce parzące twarz -']
    secondline = ['wyglądam za okno', 'otwieram drzwi', 'podlewam kwiaty', 'czytając powieść']
    thirdline = ['myślę o wczoraj', 'myślę o jutrze', 'myślę o nim', 'myślę o domu']

    day = datetime.datetime.now().day
    month = datetime.datetime.now().month
    if (month > 3 and month < 6):
        a = 0
    if ((month == 3 and day >= 21) or (month == 6 and day < 22)):
        a = 0
    if (month > 12 and month < 3):
        a = 1
    if ((month == 12 and day >= 22) or (month == 3 and day < 21)):
        a = 1
    if (month > 9 and month < 12):
        a = 2
    if ((month == 9 and day >= 23) or (month == 12 and day < 22)):
        a = 2
    if (month > 6 and month < 9):
        a = 3
    if ((month == 6 and day >= 22) or (month == 9 and day < 23)):
        a = 3

    b = int(random.uniform(0, 4))
    c = int(random.uniform(0, 4))

    print(firstline[a])
    print(secondline[b])
    print(thirdline[c])

    input('Press any key to continue...')
    menu()


menu()