s = input()
alpha = []
num = []
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
for i in range(len(s)):
    if s[i] not in numbers:
        alpha.append(ord(s[i]))
    else:
        num.append(s[i])
alpha.sort()
num.sort()
for j in alpha:
    print(chr(j), end='')
total = 0
for k in num:
    total += int(k)
print(total, end='')