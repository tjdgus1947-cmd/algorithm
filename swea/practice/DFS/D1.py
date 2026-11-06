import sys
sys.stdin = open('D1.txt', 'r')

dy = [-1,0,1,0]
dx = [0,1,0,-1]

def go(y, x):
    global result
    if y == N-1 and x == N-1:
        result += 1
        return 
    for d in range(4):
        ny, nx = y+dy[d], x+dx[d]
        if 0<=ny<N and 0<=nx<N and visited[ny][nx] == False and arr[ny][nx] == 0:
            visited[ny][nx] = True
            go(ny, nx)
            visited[ny][nx] = False
    
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [[False] * N for _ in range(N)]
    result = 0
    visited[0][0] = True
    go(0, 0)
    print(f"#{tc} {result}")