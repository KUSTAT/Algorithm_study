from bisect import bisect_left
import sys

def solve():
    input = sys.stdin.readline
    N = int(input())
    total = list(map(int, input().split()))
    minus_dex = bisect_left(total, 0)
    if minus_dex == 0: # all plus
        print(total[0], total[1])
        return
    elif minus_dex == N: # all minus
        print(total[-2], total[-1])
        return
    else:
        min = 1000000001
        duo = None
        for i in range(len(total)-1):
            dex = bisect_left(total, -total[i])
            for candidate in {i+1, dex-1, dex}:
                # 자기 자신을 지목한 경우, 이전 index는 이미 돌았고
                # 다음 index는 이미 고려될 예정, continue
                if candidate == i:
                    continue
                # 이 안에 없는 경우, 그냥 젤 큰놈이랑 더한다
                if candidate == len(total):
                    candidate -= 1
                val = abs(total[i] + total[candidate])
                if val < min:
                    min = val
                    duo = sorted([total[i], total[candidate]])
                    if val == 0:
                        print(duo[0], duo[1])
                        return
        print(duo[0], duo[1])

solve()
# 4
# -90 1 2 100
# 1 2