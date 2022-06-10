import sys
sys.stdin = open('input.txt')
T = int(sys.stdin.readline().rstrip())
for tc in range(1, T+1):
    n, m = map(int, input().split())
    priority = list(map(int, input().split()))
    index = [i for i in range(n)]
    index[m] = 'target'
    cnt = 0

    while priority:
        if priority[0] == max(priority):
            cnt += 1
            if index[0] == 'target':
                print(cnt)
                break
            priority.pop(0)
            index.pop(0)
        else:
            priority.append(priority.pop(0))
            index.append(index.pop(0))
