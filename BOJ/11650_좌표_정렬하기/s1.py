import sys
sys.stdin = open('input.txt')

n = int(sys.stdin.readline().strip())
spots = []
for i in range(n):
    spots.append(list(map(int, sys.stdin.readline().split())))
spots.sort(key=lambda x: (x[0], x[1]))
for j in spots:
    print(j[0], j[1])