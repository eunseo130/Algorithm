import sys
sys.stdin = open('input.txt')
n = int(input())
stack = []
answer = []
flag = 0
temp = 1
for i in range(n):
    num = int(input())
    while temp <= num:
        stack.append(temp)
        answer.append('+')
        temp += 1
    if stack[-1] == num:
        stack.pop()
        answer.append('-')
    else:
        print('NO')
        flag = 1
        break
if flag == 0:
    for j in answer:
        print(j)