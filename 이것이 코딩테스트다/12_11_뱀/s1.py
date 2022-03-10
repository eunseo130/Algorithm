n = int(input())
k = int(input())
board = [[0] * n for _ in range(n)]
for i in range(k):
    r, c = map(int, input().split())
    board[c][r] = 1
l = int(input())
snake = []
for j in range(l):
    sec, dir = input().split()
    snake.append([sec, dir])
    