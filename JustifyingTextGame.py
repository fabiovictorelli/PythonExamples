# Starting with a * in the middle of a Field, go random to the border
# fabiovictorelli@gmail.com
# Mon Aug 22 16:22:11 EDT 2022

import random
Star = "*"
SizeOfField = 12


def printstar(position):
    #print('Printing Star at', position)
    PointAtRightofStar = SizeOfField - position
    print(Star.rjust(position, '.') + '.'.ljust(PointAtRightofStar, '.'))


Position = int(SizeOfField / 2)      # Starting in the middle
printstar(Position)

num = 0
while (Position > 1 and Position < SizeOfField):
    num += 1
    RandInt = random.randrange(1, SizeOfField)

    if (RandInt < Position):
        Position -= 1
    elif (RandInt > Position):
        Position += 1
    printstar(Position)

print(num, 'Times to reach the border')
