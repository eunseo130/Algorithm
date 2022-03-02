N, M, K = map(int, input().split())
numbers = list(map(int, input().split()))
numbers.sort(reverse=True)
result = 0
if K >= M:
    result = numbers[0] * M
else:
    while M >= 0:
        result += numbers[0] * K
        M = M-K