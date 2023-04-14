from collections import defaultdict
import sys

class FlaskSimulator:
    ds = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    def __init__(self, flask, S, X, Y, N):
        self.n = N
        self.s = S
        self.x = X - 1
        self.y = Y - 1
        self.flask = flask
        self.leaves = defaultdict(set)
        # construct basic starts
        for r in range(N):
            for c in range(N):
                if self.flask[r][c]:
                    self.leaves[self.flask[r][c]].add((r, c))
        self.ordered = list(sorted(self.leaves.keys()))
    
    def simulate(self):
        for _ in range(self.s):
            for virus in self.ordered:
                self.spread(virus)
        return self.flask[self.x][self.y]

    def spread(self, virus):
        # leaf is the outermost position
        new_leaves = set()
        for leaf in self.leaves[virus]: 
            x, y = leaf
            for d in self.ds:
                dx, dy = d
                nx, ny = x + dx, y + dy
                if 0 <= nx < self.n and 0 <= ny < self.n and not self.flask[nx][ny]:
                    new_leaves.add((nx, ny))
                    self.flask[nx][ny] = virus
        self.leaves[virus] = new_leaves                

def solve():
    input = sys.stdin.readline
    N, K = tuple(map(int, input().split()))
    flask = []
    for _ in range(N):
        flask.append(list(map(int, input().split())))
    
    S, X, Y = tuple(map(int, input().split()))
    fs = FlaskSimulator(flask, S, X, Y, N)
    print(fs.simulate())

solve()
