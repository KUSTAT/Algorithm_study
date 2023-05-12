def check(p):
    stack = []
    for c in p:
        if c == '(':
            stack.append(c)
        else:
            if stack:
                stack.pop()
            else:
                return False
    return len(stack) == 0

def rec(p):
    if p == "":
        return ""
    cnt = {"(" : 0, ")" :0}
    till = 0
    for c in p:
        till += 1
        cnt[c] += 1
        if cnt["("] == cnt[")"]:
            break
    u, v = p[:till], p[till:]
    if check(u):
        return u + rec(v)
    else:
        u = u[1:-1]
        new = ""
        for c in u:
            if c == "(":
                new += ")"
            else:
                new += "("
        return "(" + rec(v) + ")" + new
    

def solution(p):
    if check(p):
        return p
    answer = rec(p)
    return answer