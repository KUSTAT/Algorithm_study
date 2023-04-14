from itertools import combinations
import copy

class LabSimulator:
    ds = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    def __init__(self, lab, twos, walls, N, M):
        self.n = N
        self.m = M
        self.lab = lab
        self.twos = twos
        for wall in walls:
            r, c = wall
            self.lab[r][c] = 1
    
    def simulate(self):
        cnt = 0
        for two in self.twos:
            self.spread(two)
        for r in range(self.n):
            for c in range(self.m):
                cnt += not self.lab[r][c] # if safe
        return cnt

    def spread(self, pos):
        for d in self.ds:
            x, y = pos
            dx, dy = d
            nx, ny = x + dx, y + dy
            if 0 <= nx < self.n and 0 <= ny < self.m and not self.lab[nx][ny]:
                self.lab[nx][ny] = 2
                self.spread((nx, ny))


def solve():
    N, M = tuple(map(int, input().split()))
    lab = []
    for _ in range(N):
        lab.append(list(map(int, input().split())))
    zeros = []
    twos = []
    for r in range(N):
        for c in range(M):
            if lab[r][c] == 0:
                zeros.append((r, c))
            if lab[r][c] == 2:
                twos.append((r, c))
    safe = 0
    for walls in combinations(zeros, 3):
        ls = LabSimulator(copy.deepcopy(lab), twos, walls, N, M)
        safe = max(safe, ls.simulate())
    print(safe)

solve()