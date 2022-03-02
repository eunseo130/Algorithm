n, m, k = map(int, input().split())
numbers = list(map(int, input().split()))

numbers.sort()
first = numbers[n-1]
second = numbers[n-2]

count = int(m / (k+1)) * k
count += m % (k+1)

result = 0
result += (count) * first
result += (m-count) * second

print(result)