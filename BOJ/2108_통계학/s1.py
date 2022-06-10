import sys
sys.stdin = open("input.txt")
from collections import Counter
N = int(sys.stdin.readline().rstrip())
numbers = []
for _ in range(N):
    numbers.append(int(sys.stdin.readline().rstrip()))
numbers.sort()
cnt = Counter(numbers).most_common(2)
print(round(sum(numbers)/N))
print(numbers[N//2])
if len(numbers) > 1:
    if cnt[0][1] == cnt[1][1]:
        print(cnt[1][0])
    else:
        print(cnt[0][0])
else:
    print(cnt[0][0])
print(max(numbers)-min(numbers))
