import sys
sys.stdin = open('input.txt')
T = int(sys.stdin.readline().rstrip())
for tc in range(1, T+1):
    doc = list(map(int, sys.stdin.readline().split()))
    