N, M = tuple(map(int, input().split()))
currencies = []
for _ in range(N):
    currencies.append(int(input()))

# 작은것부터 sort
currencies = sorted(currencies)

dp = [30000] * (M+1)
dp[0] = 0 # 0원을 만들 방법 0가지

for goal in range(1, M+1):
    for currency in currencies:
        if goal - currency >= 0 and dp[goal-currency] != 30000:
            dp[goal] = min(dp[goal-currency] + 1, dp[goal]) # 현재 값 또는 그 이전 + 1값보다 큰지 업데이트

if dp[M] == 30000:
    print(-1)
else:
    print(dp[M])