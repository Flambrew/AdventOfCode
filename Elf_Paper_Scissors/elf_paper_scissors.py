import os

f = open('Elf_Paper_Scissors\\input.txt', 'r')

tally = 0
options = ' XYZ'


def calcscore(a, b):
    if a == 'X':
        if b == 'A':
            return 3
        elif b == 'B':
            return 0
        else:
            return 6
    elif a == 'Y':
        if b == 'A':
            return 6
        elif b == 'B':
            return 3
        else:
            return 0
    else:
        if b == 'A':
            return 0
        elif b == 'B':
            return 6
        else:
            return 3


for s in f:
    tally += options.index(s[2]) + calcscore(s[2], s[0])

print(tally)

f.close()