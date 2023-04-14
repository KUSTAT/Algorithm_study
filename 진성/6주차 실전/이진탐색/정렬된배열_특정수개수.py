import sys
from bisect import bisect_left, bisect_right

def solve():
    input = sys.stdin.readline
    N, K = tuple(map(int, input().split()))
    l = list(map(int, input().split()))
    left = bisect_left(l, K)
    right = bisect_right(l, K)

    if left + 1 < N and l[left + 1] == K:
        if right - 1 >= 0 and l[right - 1] == K:
            print(right - left)
        else:
            print(-1)
    else:
        print(-1)

    # actually you don't need it
    # what you only need is to check if right-left == 0
    # if so, there doesn't exist
    # then you print -1 for that
solve()

"""
7 2
1 1 2 2 2 2 3
4

8 4
1 1 2 2 2 2 3 5
-1
"""