import sys
import heapq
sys.stdin = open('input.txt')

n = int(input())
left_heap, right_heap = [], []
for i in range(n):
    num = int(sys.stdin.readline())

    if len(left_heap) == len(right_heap):
        heapq.heappush(left_heap, -num)
    else:
        heapq.heappush(right_heap, num)
    
    if right_heap and right_heap[0] < -left_heap[0]:
        left = heapq.heappop(left_heap)
        right = heapq.heappop(right_heap)

        heapq.heappush(left_heap, -right)
        heapq.heappush(right_heap, -left)
    
    print(-left_heap[0])