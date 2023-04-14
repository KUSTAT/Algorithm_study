#https://school.programmers.co.kr/learn/courses/30/lessons/60059
import numpy as np

def solution(key, lock):
    n = len(lock)
    m = len(key)
    correct = [1] * (n*n)
    size = n + 2*(m-1)
    a = np.array([0] * (size * size)).reshape((size, size))
    for r in range(m-1, n+m-1):
        for c in range(m-1, n+m-1):
            a[r][c] = lock[r-m+1][c-m+1]
    
    for rotation in range(4):
        key = np.array(list(zip(*key[::-1])))
        for start_row in range(size-m+1):
            for start_col in range(size-m+1):
                b = np.array([0] * (size * size)).reshape((size, size))
                for r in range(start_row, start_row + m):
                    for c in range(start_col, start_col + m):
                        b[r][c] = key[r-start_row][c-start_col]
                check = np.add(a, b)
                if list(check[m-1:n+m-1, m-1:n+m-1].reshape(n*n)) == correct:
                    return True
    return False