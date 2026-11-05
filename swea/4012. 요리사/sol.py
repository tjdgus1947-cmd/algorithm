import sys
sys.stdin = open('input.txt', 'r')

def taste(group):
    total = 0
    for i in group:
        for j in group:
            total += S[i][j]        # i == j면 S[i][i] = 0이라 그냥 더해도 됨
    return total

def go(start, cnt):
    global result
    if cnt == N//2:                  # 반 다 골랐으면
        A = [i for i in range(N) if visited[i]]
        B = [i for i in range(N) if not visited[i]]
        result = min(result, abs(taste(A) - taste(B)))
        return
    for i in range(start, N):
        visited[i] = True                # 고름
        go(i+1, cnt+1)
        visited[i] = False                # 되돌림

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    S = [list(map(int, input().split())) for _ in range(N)]
    visited = [False] * N
    result = float('inf')
    go(0,0)
    print(f"#{tc} {result}")