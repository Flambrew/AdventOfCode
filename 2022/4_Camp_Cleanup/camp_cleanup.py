import os

f = open('4_Camp_Cleanup\\input.txt', 'r')

tally = 0
tallyB = 0

for s_ in f:
    s = s_.strip().split(',')
    a = int(s[0].split('-')[0])
    b = int(s[0].split('-')[1])
    c = int(s[1].split('-')[0])
    d = int(s[1].split('-')[1])

    if (a >= c and b <= d) or (a <= c and b >= d):
        tally += 1

    if d >= a >= c or d >= b >= c or a <= c <= b or a <= d <= b:
        tallyB += 1
        
print(f'{tally} {tallyB}')

f.close()