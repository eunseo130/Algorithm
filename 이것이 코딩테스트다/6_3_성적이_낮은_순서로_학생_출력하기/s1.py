n = int(input())
lst = {}
for i in range(n):
    name, score = input().split()
    lst[name] = int(score)

sorted_lst = sorted(lst.items())

for i in sorted_lst:
    print(i[0], end=' ')