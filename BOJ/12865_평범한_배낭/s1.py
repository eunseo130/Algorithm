import sys
sys.stdin = open('input.txt')

n, max_weight = map(int, input().split())
temp = [0] * (max_weight + 1)
lst = []
for i in range(n):
    w, v = map(int, input().split())
    lst.append([w, v])
lst.sort()
