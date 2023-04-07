N = int(input())
dp = [[0 for _ in range(10)] for _ in range(N)]
dp[0] = [0] + [1] * 9

for length in range(1, N):
    for digit in range(10):
        if digit == 0:
            dp[length][digit] = dp[length - 1][digit + 1]
        elif digit == 9:
            dp[length][digit] = dp[length - 1][digit - 1]
        else:
            dp[length][digit] = dp[length - 1][digit + 1] + dp[length - 1][digit - 1]

print(sum(dp[N-1]) % 1000000000)

"""
  1 2 3
0 0 1 1
1 1 1 3

2 1 2 3
3 1 2 4
4 1 2 4
5 1 2 4
6 1 2 4
7 1 2 4
8 1 2 4

9 1 1 2

Length n의 계단수는, n-1 길이의 계단 수에서,
마지막 digit이 1크거나 1작게 끝나는 경우에서로부터 construct된다.

n-1의 모든 1로 끝나는 계단수는 n길이의 0이나 2로 끝나는 계단수가 된다.
이를 토대로 위처럼 구조를 짜면 된다.
"""