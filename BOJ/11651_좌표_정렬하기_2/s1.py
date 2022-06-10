import sys
sys.stdin = open('input.txt')
n = int(input())
spots = []
for _ in range(n):
    spot = list(map(int, input().split()))
    spots.append(spot)
spots.sort(key = lambda x:(x[1], x[0]))
for i in range(len(spots)):
    for j in range(2):
        print(spots[i][j], end=" ")
    print()
