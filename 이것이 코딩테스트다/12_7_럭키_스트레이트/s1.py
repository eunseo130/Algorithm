n = input()
s = len(n) // 2
total1 = 0
total2 = 0
for i in range(s):
    total1 += int(n[i])
for j in range(s, len(n)):
    total2 += int(n[j])

if total1 == total2:
    print('LUCKY')
else:
    print('READY')