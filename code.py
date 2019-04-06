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
    print('First group of poems with fully randomized structure')
    print('[2] Generate second poem')
    print('Poem changing with the seasons.')
    print('[3] Generate third poem')
    print('Poem changing with the time of the day')
    print('[E] Exit')
    odp = input('Wanna select an option?')
    if (odp == '1'):
        firstpoem()
    elif (odp == '2'):
        secondpoem()
    elif (odp == '3'):
        thirdpoem()
    elif (odp == 'E' or odp == 'e'):
        pass
    else:
        print('Nonexistent option.')
        input('Press any key to continue...')
        menu()


def firstpoem():
    cls()
    
    firstLineFirst = ['maska opadła', 'maska wraca', 'maska skruszała']
    secondLineFirst = ['zagubione ciało', 'zagubione serce', 'zagubiony umysł']
    thirdLineFirst = ['milknie i zanika', 'krzyczy w ciszy', 'cieszy się bólem']

    one = [firstLineFirst, secondLineFirst, thirdLineFirst]

    firstLineSecond = ['na starość', 'w młodości', 'w sukni ślubnej']
    secondLineSecond = ['dokarmiam gołębie -', 'polubiłam balet - ', 'straciłam kochanka -']
    thirdLineSecond = ['taka kolej rzeczy','chyba warto tańczyć','długo szukałam celu']

    two = [firstLineSecond, secondLineSecond, thirdLineSecond]

    poems = [one, two]

    n = int(random.uniform(0, 2))

    a = int(random.uniform(0, 3))
    b = int(random.uniform(0, 3))
    c = int(random.uniform(0, 3))

    print(poems[n][0][a])
    print(poems[n][1][b])
    print(poems[n][2][c])

    input('Press any key to continue...')
    menu()


def secondpoem():
    cls()

    firstline = ['pierwsze kwiaty wiśni -', 'pierwsze płatki śniegu -', 'pierwsze złote liście -', 'słońce parzące twarz -']
    secondline = ['wyglądam za okno', 'otwieram drzwi', 'podlewam kwiaty', 'czytając powieść']
    thirdline = ['myślę o wczoraj', 'myślę o jutrze', 'myślę o nim', 'myślę o domu']

    day = datetime.datetime.now().day
    month = datetime.datetime.now().month

    # spring
    if (month > 3 and month < 6):
        a = 0
    if ((month == 3 and day >= 21) or (month == 6 and day < 22)):
        a = 0

    # winter
    if (month > 12 and month < 3):
        a = 1
    if ((month == 12 and day >= 22) or (month == 3 and day < 21)):
        a = 1

    # autumn
    if (month > 9 and month < 12):
        a = 2
    if ((month == 9 and day >= 23) or (month == 12 and day < 22)):
        a = 2

    # summer
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


def thirdpoem():
    cls()

    firstline = ['3-6', '6-10', '10-14', '14-18', '18-23', '23-03']
    secondline = [' ', ' ', ' ', ' ']
    thirdline = [' ', ' ', ' ', ' ']

    hour = datetime.datetime.now().hour
    minute = datetime.datetime.now().minute

    # 3-6
    if (hour > 3 and hour < 6):
        a = 0
    if ((hour == 3 and minute >= 00) or (hour == 5 and minute <= 59)):
        a = 0

    # 6-10
    if (hour > 6 and hour < 10):
        a = 1
    if ((hour == 6 and minute >= 00) or (hour == 9 and minute <= 59)):
        a = 1

    # 10-14
    if (hour > 10 and hour < 14):
        a = 2
    if ((hour == 10 and minute >= 00) or (hour == 13 and minute <= 59)):
        a = 2

    # 14-18
    if (hour > 14 and hour < 18):
        a = 3
    if ((hour == 14 and minute >= 00) or (hour == 17 and minute <= 59)):
        a = 3

    # 18-23
    if (hour > 18 and hour < 23):
        a = 4
    if ((hour == 18 and minute >= 00) or (hour == 22 and minute <= 59)):
        a = 4

    # 23-03
    if (hour > 23 and hour < 3):
        a = 5
    if ((hour == 23 and minute >= 00) or (hour == 2 and minute <= 59)):
        a = 5

    b = int(random.uniform(0, 4))
    c = int(random.uniform(0, 4))

    print(firstline[a])
    print(secondline[b])
    print(thirdline[c])

    input('Press any key to continue...')
    menu()


menu()