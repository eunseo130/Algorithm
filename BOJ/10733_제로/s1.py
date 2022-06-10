import sys
sys.stdin = open('input.txt')
k = int(sys.stdin.readline().rstrip())
numbers = []
for _ in range(k):
    temp = int(sys.stdin.readline().rstrip())
    if temp == 0:
        numbers.pop()
    else:
        numbers.append(temp)
print(sum(numbers))
