from collections import deque

n = int(input())
cards = []
for i in range(n):
    cards.append(i+1)
cards = deque(cards)
while True:
    if len(cards) == 1:
        break
    cards.popleft()
    cards.append(cards.popleft())
print(cards[0])