# Sorting을 하자
# 작은 것 부터, 작다면 키로당 가치가 큰 것부터
#from heapq import heappush, heappop

from pprint import pprint
N, K = tuple(map(int, input().split()))

things = []

for _ in range(N):
    w, k = tuple(map(int, input().split()))
    data = (w, k)
    things.append(data)

dp = [[0] * (N + 1) for _ in range(K+1)]

for cur_weight in range(1, K+1):
    for i in range(1, N+1):
        w, v = things[i-1]
        if cur_weight >= w:
            dp[cur_weight][i] = max(dp[cur_weight][i-1], dp[cur_weight-w][i-1] + v)
        else:
            dp[cur_weight][i] = dp[cur_weight][i-1]


max_val = 0
for r in range(len(dp)):
    for c in range(len(dp[0])):
        if max_val < dp[r][c]:
            max_val = dp[r][c]

#pprint(dp)
print(max_val)

"""
for i in range(1, N+1):
    value, weight = things[i-1]
    value = -value
    # Measure the max when included
    for k in range(2):
        candidates_included = []
        for j in range(i):
                w, v = dp[j]
                if w + weight <= K:
                    heappush(candidates_included, (-(v + value), w+weight))
            v_i, w_i = heappop(candidates_included)
            v_i = -v_i
            if dp[i-1][1] >= v_i:
                dp[i] = dp[i-1]
            else:
                dp[i] = (w_i, v_i)

max_val = 0
for _, value in dp:
    if value > max_val:
        max_val = value

print(max_val)

"""


