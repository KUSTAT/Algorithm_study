import heapq
import sys

class Pictures:
    def __init__(self, max_size):
        self.candidates = []
        self.current = set()
        self.m = max_size
        self.time = 0
        # [적은 추천, 오래된 시간 time, 학생]

    def recommend(self, student):
        self.time += 1
        # 없는 학생 추천
        if student not in self.current:
            # eviction
            if len(self.candidates) == self.m:
                _, __, evict = heapq.heappop(self.candidates)
                self.current.remove(evict)
            # else
            heapq.heappush(self.candidates, [1, self.time, student])
            self.current.add(student)
        # 있는 학생 추천
        else:
            for elem in self.candidates:
                if elem[2] == student:
                    elem[0] += 1
                    break
            heapq.heapify(self.candidates)

    def final(self):
        ans = []
        for e in self.candidates:
            ans.append(e[2])
        ans = sorted(ans)
        ans = [str(a) for a in ans]
        print(' '.join(ans))



def solve():
    input = sys.stdin.readline
    N = int(input())
    p = Pictures(N)
    m = int(input())
    rec_info = list(map(int, input().split()))
    for info in rec_info:
        p.recommend(info)
    
    p.final()

solve()