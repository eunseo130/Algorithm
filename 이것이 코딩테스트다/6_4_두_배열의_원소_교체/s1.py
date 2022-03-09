from re import S


n, k = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

A.sort()
B.sort(reverse=True)

a = 0

for i in range(k):
    A[i] = a
    A[i] = B[i]
    B[i] = a

print(sum(A))