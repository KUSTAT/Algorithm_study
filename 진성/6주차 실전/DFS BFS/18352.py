# input 속도 때매 못풀고 있었음.... sys를 잘 쓰자.

from collections import defaultdict, deque
import sys

def solve():
    input = sys.stdin.readline
    N, M, K, X = tuple(map(int, input().split()))
    graph = defaultdict(list)
    for _ in range(M):
        s, d = input().split()
        graph[s].append(d)
    
    queue = deque([(str(X), 0)])
    visited = set([str(X)])
    answer = []
    while queue:
        node, distance = queue.popleft()
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                node_di = distance + 1
                if node_di == K:
                    answer.append(int(neighbor))
                else:
                    queue.append((neighbor, node_di))
    if not answer:
        print(-1)
    else:
        answer = sorted(answer)
        for a in answer:
            print(a)

solve()