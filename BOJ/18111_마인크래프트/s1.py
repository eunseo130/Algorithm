import sys
sys.stdin = open('input.txt')
n, m, b = map(int, sys.stdin.readline().split())
ground = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
height = 0
ans = 987654321
for i in range(257):
    max = 0
    min = 0
    for j in range(n):
        for k in range(m):
            if ground[j][k] < i:
                min += (i - ground[j][k])
            else:
                max += (ground[j][k] - i)
    if max + b >= min:
        if min + (max * 2) <= ans:
            ans = min + (max * 2)
            height = i
print(ans, height)