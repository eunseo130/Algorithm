import sys
sys.stdin = open('input.txt')
n, m = map(int, input().split())
tree = list(map(int, input().split()))

start, end = 0, max(tree)

while start <= end:
    mid = (start + end) // 2
    ans = 0
    for i in tree:
        if i > mid:
            ans += i - mid
    if ans >= m:
        start = mid + 1
    else:
        end = mid -1
print(end)