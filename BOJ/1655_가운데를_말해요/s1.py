import sys
sys.stdin = open('input.txt')

n = int(input())
temp = []
for i in range(n):
    temp.append(int(input()))
    temp.sort()
    length = len(temp)
    if length % 2 == 0:
        print(temp[length-1])
    else:
        print(temp[length])