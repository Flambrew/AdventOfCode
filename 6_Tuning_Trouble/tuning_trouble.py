import os

f = open('6_Tuning_Trouble\\input.txt', 'r')

s = f.read()

def find_marker(length):
    mark = []
    for i, ch in enumerate(s):
        mark += ch
        if len(mark) > length:
            mark.pop(0)
        list_lead = ''
        for a in mark:
            if a not in list_lead:
                list_lead += a
        if len(list_lead) == length:
            return [''.join(mark), i + 1]

print(find_marker(4))
print(find_marker(14))

f.close()