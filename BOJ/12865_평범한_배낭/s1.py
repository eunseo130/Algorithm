import sys
sys.stdin = open('input.txt')

n, max_weight = map(int, input().split())
temp = [0] * (max_weight + 1)
for i in range(n):
    w, v = map(int, input().split())
    for j in range(max_weight, w-1, -1):
        temp[j] = max(temp[j], temp[j-w]+v)
print(temp[max_weight])