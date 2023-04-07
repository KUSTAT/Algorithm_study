from collections import deque

def bfs(N, K):
    visited = [0] * 100001
    queue = deque()
    queue.append(N)

    


N, K = tuple(map(int, input().split()))

if N >= K:
    print(N-K)

else:

