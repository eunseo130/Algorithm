import sys
sys.stdin = open('input.txt')

from sys import stdin
n = int(stdin.readline().rstrip())

for i in range(n):
    answer = 'YES'
    temp = stdin.readline().rstrip()
    stack = []
    for j in range(len(temp)):
        if temp[j] == '(':
            stack.append(temp[j])
        elif temp[j] == ')' and stack:
            stack.pop()
        elif temp[j] == ')' and len(stack) == 0:
            answer = 'NO'
            break
    if len(stack) != 0:
        answer = 'NO'
    print(answer)
    