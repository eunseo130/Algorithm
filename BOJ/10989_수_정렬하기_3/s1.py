import sys
sys.stdin = open('input.txt')
n = int(sys.stdin.readline())
numbers = [0] * 10001
for i in range(n):
    numbers[int(sys.stdin.readline().rstrip())] += 1
for j in range(10001):
    if numbers[j] != 0:
        for k in range(numbers[j]):
            print(j)