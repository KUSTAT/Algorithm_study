# n^2

N, M = tuple(map(int, input().split()))
balls = list(map(int, input().split()))

total = 0

for i in range(len(balls)-1):
    std = balls[i]
    for j in range(i+1, len(balls)):
        if std != balls[j]:
            total += 1

print(total)