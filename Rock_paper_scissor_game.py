#!/bin/python3

from random import randint

while 1:
    player = input('rock(r), paper(p), scisson(s)?')

    if player == 'E' or player == 'e':
        print('ok Bye')
        break

    elif player != 'r' and player != 'p' and player != 's':
        print('Invalid Entry')
        print("")
        # break


    else:

        print(player, 'vs', end=' ')

        # computers turn

        chosen = randint(1, 3)
        # print(chosen)

        if chosen == 1:
            computer = 'r'

        elif chosen == 2:
            computer = 'p'

        else:
            computer = 's'

        ppoints = 0
        cpoints = 0

        print(computer)

        if player == computer:
            print('*****DRAW*****')
            print("")


        elif player == 'r' and computer == 'p':
            print('You lose')
            cpoints = cpoints + 1
            print('You:', ppoints, 'Computer:', cpoints)
            print("")

        elif player == 'r' and computer == 's':
            print('You Win')
            ppoints = ppoints + 1
            print('You:', ppoints, 'Computer:', cpoints)
            print("")


        elif player == 'p' and computer == 'r':
            print('You Win')
            ppoints = ppoints + 1
            print('You:', ppoints, 'Computer:', cpoints)
            print("")


        elif player == 'p' and computer == 's':
            print('You lose')
            print("")
            cpoints = cpoints + 1
            print('You:', ppoints, 'Computer:', cpoints)
            print("")


        elif player == 's' and computer == 'r':
            print('You lose')
            cpoints = cpoints + 1
            print('You:', ppoints, 'Computer:', cpoints)
            print("")


        elif player == 's' and computer == 'p':
            print('You Win')
            ppoints = ppoints + 1
            print('You:', ppoints, 'Computer:', cpoints)
            print("")
