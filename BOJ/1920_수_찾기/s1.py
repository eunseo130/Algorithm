import sys
sys.stdin = open('input.txt')

from collections import Counter
from sys import stdin

n = int(stdin.readline().rstrip())
numbers = list(map(int, stdin.readline().split()))

m = int(stdin.readline().rstrip())
test = list(map(int, stdin.readline().split()))

count = Counter(numbers)

for i in range(m):
    if test[i] in count:
        print(1)
    else:
        print(0)
