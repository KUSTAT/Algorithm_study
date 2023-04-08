N = int(input())
storage = list(map(int, input().split()))

dp = [0] * (N + 1)
dp[1] = storage[0]

for i in range(2, N+1):
    dp[i] = max(dp[i-2] + storage[i-1], dp[i-1])

print(max(dp))