import sys
sys.stdin = open("input.txt")
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    numbers = []
    for _ in range(N):
        numbers.append(int(input()))
    numbers.sort()

    print(round(sum(numbers)/N))
    print(numbers[N//2])
    print(max(numbers)-min(numbers))
    