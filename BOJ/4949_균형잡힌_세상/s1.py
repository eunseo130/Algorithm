import sys
sys.stdin = open('input.txt')
while True:
    sentence = input()
    if sentence == '.':
        break
    temp = []
    answer = 'yes'
    for char in sentence:
        if char == '(' or char == '[':
            temp.append(char)
        elif char == ')':
            if len(temp) != 0 and temp[-1] == '(':
                temp.pop()
            else:
                answer = 'no'
                break
        elif char == ']':
            if len(temp) != 0 and temp[-1] == '[':
                temp.pop()
            else:
                answer = 'no'
                break
    if len(temp) == 0:
        print(answer)
    else:
        print('no')