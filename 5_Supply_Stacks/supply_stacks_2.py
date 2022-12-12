import os

f = open('5_Supply_Stacks\\input.txt', 'r')

stacks = [] 

####### STACK PARSING #######

line_offsets = [0]
offset_temp = 0
stack_end = -1

for s in f:
    line_offsets.append(len(s) + offset_temp)
    offset_temp += len(s)
    stack_end += 1
    if s[0] == ' ':
        for i in range(int(s[len(s) - 3])):
            stacks.append([])
        break

for i in range(stack_end):
    f.seek(line_offsets[stack_end - 1 - i])
    for j, ch in enumerate(f.readline()):
        if j % 4 == 1 and ch != ' ':
            stacks[(j - 1) // 4].append(ch)

####### SUPPLY MOVING #######

def move(n, a, b):
    stacks[b - 1] += (stacks[a - 1][len(stacks[a - 1]) - n:len(stacks[a - 1])])
    stacks[a - 1] = (stacks[a - 1][0:len(stacks[a - 1]) - n])

f.seek(line_offsets.pop())

for s in f:
    if (s[0] == 'm'):
        n = int(s[s.index('e') + 2:s.index('f') - 1])
        a = int(s[s.index('r') + 4:s.index('t') - 1])
        b = int(s[s.index('t') + 3:len(s) - 1])
        move(n, a, b)

####### STACK TOP READING #######

for ls in stacks:
    print(ls.pop(), end= '')

f.close()