import sys
sys.stdin = open('input.txt', 'r')

def go(cnt, y, x, total):
    global result
    if cnt == N:
        result = min(result, total + abs(y-ey) + abs(x-ex))
        return
    if total > result:
        return
    for j in range(N):
        if visited[j]:
            continue
        visited[j] = True
        ny, nx = customers[j]
        d = abs(y-ny) + abs(x-nx)
        go(cnt+1, ny, nx, total+d)
        visited[j] = False

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    lst = list(map(int, input().split()))
    sy, sx = lst[0], lst[1]
    ey, ex = lst[2], lst[3]
    customers = [(lst[i], lst[i+1]) for i in range(4, 4+2*N, 2)]
    visited = [False] * len(customers)
    result = float('inf')
    go(0, sy, sx, 0)
    print(f"#{tc} {result}")