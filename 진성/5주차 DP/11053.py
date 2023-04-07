N = int(input())
sequence = list(map(int, input().split()))

dp = [1] * N

for i in range(1, N):
    for j in range(i): # for each dp
        if sequence[i] > sequence[j]: # 만약 i번째 수가 j번째 수보다 크다면, dp[j]의 longest보다 하나 더 크게 할 수 있다.
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))



"""
iteration을 돌며, 현재 index i가 maximum increasing subsequence의 max가 되게 한다.
i 이전의 값들로 세워진 dp의 값을 참조하며, 얘가 걔보다 크면, 그 이전보다도 모두 큰게 된다. 그러니 + 1한 값으로 현재 dp값을 업데이트
"""