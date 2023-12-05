import os

f = open('1_Elf_Calories\\input.txt', 'r')

cals = 0
top_cals = [0, 0, 0]

for s in f:
    if s.strip().isdigit():
        cals += int(s)
    else:
        if cals >= min(top_cals):
            top_cals[top_cals.index(min(top_cals))] = cals
        cals = 0

print(f'{top_cals}: {sum(top_cals)}')

f.close()