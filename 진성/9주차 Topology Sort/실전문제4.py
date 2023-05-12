# 303
from collections import deque
import copy

v = int(input())

indegree = [0] * v
graph = [[] for _ in range(v)]

time = [0] * v

for i in range(v):
    data = tuple(map(int, input().split()))
    time[i] = data[0]
    for dest in data[1:-1]:
        indegree[dest-1] += 1
        graph[dest-1].append(i)

def topology_sort():
    result = copy.deepcopy(time)
    q = deque()

    for i in range(v):
        if indegree[i] == 0:
            q.append(i)
    
    while q:
        current = q.popleft()
        for i in graph[current]:
            result[i] = max(result[i], result[current] + time[i]) # 이미 한 번 계산되었거나, 이전 선수과목 시간에 + 시간이거나
            indegree[i] -= 1
            if indegree[i] == 0:
                q.append(i)
    
    for i in range(v):
        print(result[i])

topology_sort()