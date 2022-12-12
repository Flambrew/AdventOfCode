import os

f = open('3_Rucksack_Reorganization\\input.txt', 'r')

ls = ' abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

group_size = 3
group = []
tally = 0


def check_match():
    for c in group[0]:
        matching = 0
        for elf in group:
            if c in elf:
                matching += 1
        if matching == group_size:
            return ls.index(c)


for s in f:
    group += [s[0:len(s)-1]]
    if len(group) == group_size:
        tally += check_match()
        group = []

print(tally)

f.close()
