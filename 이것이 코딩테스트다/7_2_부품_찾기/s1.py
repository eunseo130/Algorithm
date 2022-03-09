n = int(input())
store = list(map(int, input().split()))
m = int(input())
customer = list(map(int, input().split()))
answer = ['no'] * m

for i in range(m):
    for j in range(n):
        if store[j] == customer[i]:
            answer[i]='yes'
            break

for k in answer:
    print(k, end=' ')