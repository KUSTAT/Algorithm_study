X = int(input())
dp = [0] * (X+1)
division = {2, 3, 5}

for i in range(2, X+1):
    candidates = []
    candidates.append(dp[i-1] + 1) # 1 더하는 경우의 수
    for d in division:
        if i % d == 0:
            candidates.append(dp[i//d] + 1) # 나눠지는 경우
    dp[i] = min(candidates) # 위 중 가능한 최소값으로 초기화

print(dp)