import sys
sys.stdin = open('input.txt')

n, k = map(int, input().split())

numbers = list(range(1, n+1))
result = []

while numbers:
    for i in range(k-1):
        numbers.append(numbers.pop(0))
    result.append(numbers.pop(0))
print('<', end='')
for i in range(len(result)-1):
    print(result[i], end=', ')
print(result[n-1], end='')
print('>', end='')