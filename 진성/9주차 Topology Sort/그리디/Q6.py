from functools import partial

num_zeros = 0

def one_round(x, sub):
    global num_zeros
    if x == 0:
        return x
    elif x == sub:
        num_zeros += 1
        return x-sub
    else:
        return x-sub

def solution(food_times, k):
    if sum(food_times) <= k:
        return -1
    global num_zeros
    
    greedy = list(sorted(list(set(food_times))))
    last = 0
    
    non_zeros = len(food_times)
    
    for g in greedy:
        gs = g - last
        last = g
        if k >= gs * non_zeros:
            round_func = partial(one_round, sub=gs)
            food_times = list(map(round_func, food_times))
            k -= gs * non_zeros
            non_zeros = len(food_times) - num_zeros
        else:
            break
    
    index = k % non_zeros
    for i in range(len(food_times)):
        if food_times[i] == 0:
            continue
        else:
            if index == 0:
                return i + 1
            else:
                index -= 1  

import heapq

def solution(food_times, k):
    answer = -1
    pq = []
    for i in range(len(food_times)):
        heapq.heappush(pq, (food_times[i], i + 1))

    left = len(food_times)  # 남은 음식 개수
    prev = 0  # 이전에 제거한 음식의 food_time

    while pq:
        # 먹는데 걸리는 시간: (남은 양) * (남은 음식 개수)
        time_to_eat = (pq[0][0] - prev) * left
        # 시간이 남을 경우 현재 음식 빼기
        if k >= time_to_eat:
            k -= time_to_eat
            prev, _ = heapq.heappop(pq)
            left -= 1
        # 시간이 부족할 경우(음식을 다 못먹을 경우) 남은 음식 중에 먹어야 할 음식 찾기
        else:
            index = k % left
            pq.sort(key=lambda x: x[1])
            answer = pq[index][1]
            break

    return answer