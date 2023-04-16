# 외계인 기타 연주
# 런타임

from collections import deque

if __name__ == "__main__":
    N, P = map(int, input().split())
    a = [list(map(int, input().split())) for _ in range(N)]
    stack = [deque([]) for _ in range(7)]
    ans = 0
    for s, p in a:
        if not stack[s]:
            stack[s].appendleft(p)
            ans += 1
        else:
            while stack[s] and stack[s][0] > p:
                stack[s].popleft()
                ans += 1
            if not stack[s] or stack[s][0] != p:
                stack[s].appendleft(p)
                ans += 1
    print(ans)