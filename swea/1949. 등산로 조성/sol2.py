import sys
sys.stdin = open('input.txt', 'r')

dy = [-1,0,1,0]
dx = [0,1,0,-1]

def go(y, x, cut, h, length):
    global result
    result = max(length, result)

    for d in range(4):
        ny, nx = y+dy[d], x+dx[d]
        if 0<=ny<N and 0<=nx<N and not visited[ny][nx]:
            if arr[ny][nx] < h:
                visited[ny][nx] = True
                go(ny, nx, cut, arr[ny][nx], length+1)
                visited[ny][nx] = False

            elif cut == 1 and arr[ny][nx]-K < h:
                visited[ny][nx] = True
                go(ny, nx, 0, h-1, length+1)
                visited[ny][nx] = False
    

T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    max_high = max(max(row) for row in arr)
    visited = [[False] * N for _ in range(N)]
    result = float('-inf')
    for r in range(N):
        for c in range(N):
            if arr[r][c] == max_high:
                visited[r][c] = True
                go(r, c, 1, arr[r][c], 1)
                visited[r][c] = False

    print(f"#{tc} {result}")