n, m = map(int, input().split())
min_value = 0
result = 0
for i in range(n):
    numbers = list(map(int, input().split()))
    result = max(min_value, min(numbers))
print(result)