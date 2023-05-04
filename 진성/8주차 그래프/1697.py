from collections import deque

queue = deque()

N, K = tuple(map(int, input().split()))

queue.append(N)
visited = [-1] * 100001
visited[N] = 0

while queue:
    position = queue.popleft()
    
    if position == K:
        print(visited[position])
        break
    
    for pos in [position * 2, position + 1, position - 1]:
        # if next position is within range and not visited
        if 0 <= pos <= 100000 and visited[pos] == -1:
            queue.append(pos)
            visited[pos] = visited[position] + 1

"""
5 17
4
"""