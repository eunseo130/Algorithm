s = input()
curr = int(s[0])
for i in range(1, len(s)):
    if curr == 0:
        curr += int(s[i])
    elif s[i] == 0 or s[i] == 1:
        curr += int(s[i])
    else:
        curr *= int(s[i])
print(curr)