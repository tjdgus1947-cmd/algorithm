import sys
sys.stdin = open('D1.txt', 'r')

dy = [-1,0,1,0]
dx = [0,1,0,-1]

def go(y, x):
    visited[y][x] = True
    for d in range(4):
        ny, nx = y+dy[d], x+dx[d]
        if 0<=ny<N and 0<=nx<M and arr[ny][nx] == 1 and visited[ny][nx] == False:
            go(ny, nx)
    return


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [[False]*M for _ in range(N)]
    result = 0
    for r in range(N):
        for c in range(M):
            if arr[r][c] == 1 and visited[r][c] == False:
                go(r,c)
                result += 1

    print(f"#{tc} {result}")