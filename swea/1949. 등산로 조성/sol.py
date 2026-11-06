import sys
sys.stdin  = open('input.txt', 'r')

dy = [-1,0,1,0]
dx = [0,1,0,-1]

def go(y, x, h, cut, length):
    global result
    result = max(result, length)
    for d in range(4):
        ny, nx = y + dy[d], x + dx[d]
        if not (0 <= ny < N and 0 <= nx < N) or visited[ny][nx]:
            continue
        if arr[ny][nx] < h:                        
            visited[ny][nx] = True
            go(ny, nx, arr[ny][nx], cut, length + 1)
            visited[ny][nx] = False
        elif cut and arr[ny][nx] - K < h:          
            visited[ny][nx] = True
            go(ny, nx, h-1, False, length + 1)        
            visited[ny][nx] = False

T = int(input())
for tc in range(1, T + 1):
    N, K = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    max_h = max(max(row) for row in arr)
    visited = [[False] * N for _ in range(N)]
    result = 0
    for r in range(N):
        for c in range(N):
            if arr[r][c] == max_h:
                visited[r][c] = True
                go(r, c, arr[r][c], True, 1)
                visited[r][c] = False
    print(f"#{tc} {result}")