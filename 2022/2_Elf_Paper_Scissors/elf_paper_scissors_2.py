import os

f = open('2_Elf_Paper_Scissors\\input.txt', 'r')

options = 'X  Y  Z'
move = {'Z': ' CAB', 'Y':  ' ABC', 'X': ' BCA'}

tally = 0

for s in f:
    tally += options.index(s[2])
    tally += move[s[2]].index(s[0])

print(tally)

f.close()