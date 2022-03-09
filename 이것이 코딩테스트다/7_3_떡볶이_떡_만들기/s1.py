n, m = map(int, input().split())
rice = list(map(int, input().split()))
rice.sort(reverse=True)
cur = 0

for i in range(len(rice)):
    cur = rice[i]
    total = 0
    for j in range(len(rice)):
        if rice[j] - cur > 0:   
            total += rice[j] - cur
    if total == m:
        break
print(cur)