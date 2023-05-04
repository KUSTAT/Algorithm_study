## 도시분할계획
"""
MST를 먼저 찾고
그 중 가장 큰 간선 하나를 끊어버린다
"""
import sys
import heapq

input = sys.stdin.readline

N, M = tuple(map(int, input().split()))
group = [i for i in range(N)]

def parent(x, group):
    if group[x] != x:
        group[x] = parent(group[x], group)
    return group[x]


pq = []
for _ in range(M):
    h1, h2, cost = tuple(map(int, input().split()))
    heapq.heappush(pq, (cost, h1-1, h2-1))
    #pq.append((cost, h1-1, h2-1))

#pq = sorted(pq)
# Kruskal
total = 0
num_edge = 0
#for cost, h1, h2 in pq:
while pq:
    cost, h1, h2 = heapq.heappop(pq)
    if h1 > h2:
        H, h = h1, h2
    else:
        H, h = h2, h1

    ph = parent(h, group)
    pH = parent(H, group)

    if ph != pH:
        group[pH] = ph
        num_edge += 1
        total += cost
        
    if num_edge == N-2:
        break

print(total)
