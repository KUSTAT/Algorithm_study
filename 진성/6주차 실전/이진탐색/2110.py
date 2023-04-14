import sys


def solution():
    input = sys.stdin.readline
    houses = []
    n, c = map(int, input().split())
    for _ in range(n):
        houses.append(int(input()))
    houses = sorted(houses)

    left = 1
    right = houses[-1] - houses[0]
    ans = houses[1] - houses[0]

    while left <= right:
        cur = houses[0]
        mid = (left + right) // 2
        count = 1

        for index in range(1, n):
            dist = houses[index] - cur
            if dist >= mid:
                cur = houses[index]
                count += 1

        if count >= c:
            left = mid + 1
            ans = mid
        else:
            right = mid - 1

    print(ans)


if __name__ == "__main__":
    solution()