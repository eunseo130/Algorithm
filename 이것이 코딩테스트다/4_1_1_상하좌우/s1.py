N = int(input())
dir = list(input().split())
start = [1, 1]
for i in dir:
    if i == 'R':
        if start[1] + 1 <= N:
            start[1] += 1
    elif i == 'L':
        if start[1] - 1 >= 1:
            start[1] -= 1
    elif i == 'U':
        if start[0] - 1 >= 1:
            start[0] -= 1
    elif i == 'D':
        if start[0] + 1 <= N:
            start[0] += 1
for j in start:
    print(j, end=" ")