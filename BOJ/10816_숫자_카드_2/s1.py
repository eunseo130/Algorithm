import sys
sys.stdin = open('input.txt')

from collections import Counter
from sys import stdin

n = stdin.readline().rstrip()
cards = list(map(int, stdin.readline().split()))

m = stdin.readline().rstrip()
result = list(map(int, stdin.readline().split()))

count = Counter(cards)

for i in range(len(result)):
    if result[i] in count:
        print(count[result[i]], end=' ')
    else:
        print(0, end=' ')
