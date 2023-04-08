N = int(input())

dp = [0] * (N+1)

dp[1] = 1 # 1*2 타일 경우의 수 1가지

for i in range(2, N+1):
    dp[i] = (dp[i-1] + 2 * dp[i-2]) % 796796

print(dp[N])

"""

  1 2 3 sum
0 0 0 0   0
1 1 0 0   1
2 1 1 1   3
3 3 1 1   5
4 5 3 3  11

정리하면 dp[i] = dp[i-1] + dp[i-2] + dp[i-2]
"""