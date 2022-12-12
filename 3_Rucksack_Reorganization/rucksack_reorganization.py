import os

f = open('Rucksack_Reorganization\\input.txt', 'r')

ls = ' abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

tally = 0

for s in f:
    a = s[0:int(len(s)/2)]
    b = s[int(len(s)/2):len(s) - 1]
    for c in a:
        if c in b:
            tally += ls.index(c)
            break

print(tally)

f.close()