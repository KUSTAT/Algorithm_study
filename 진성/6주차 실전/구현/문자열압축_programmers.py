# https://school.programmers.co.kr/learn/courses/30/lessons/60057
def solution(s):
    mini = len(s)
    for piece in range(1, len(s)//2 + 1):
        local = 0
        pre = ''
        cnt = 0
        for start in range(0, len(s), piece):
            now = s[start:start+piece]
            if now != pre:
                local += len(now)
                pre = now
                cnt = 1
            else:
                if cnt == 1:
                    local += 1
                cnt += 1
                if cnt == 10:
                    local += 1
                if cnt == 100:
                    local += 1
                
        if local < mini:
            mini = local
    return mini