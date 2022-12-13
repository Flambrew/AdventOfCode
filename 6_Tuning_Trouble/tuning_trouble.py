import os

f = open('6_Tuning_Trouble\\input.txt', 'r')

s = f.read()

mark = []

for ch in s:
    mark += ch
    if len(mark) == 5:
        mark.pop(0)

    

print(mark)


f.close()