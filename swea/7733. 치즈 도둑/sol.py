import sys
sys.stdin = open('input.txt', 'r')

from collections import deque

dy = [-1,0,1,0]
dx = [0,1,0,-1]

def bfs(sy, sx, day):
    q = deque([(sy, sx)])
    visited[sy][sx] = True
    while q:
        y, x = q.popleft()
        for d in range(4):
            ny, nx = y + dy[d], x + dx[d]
            if 0 <= ny < N and 0 <= nx < N and not visited[ny][nx] and arr[ny][nx] > day:
                visited[ny][nx] = True
                q.append((ny, nx))

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    mx = 1                                  
    for day in range(1, 101):
        visited = [[False] * N for _ in range(N)]
        cnt = 0
        for r in range(N):
            for c in range(N):
                if arr[r][c] > day and not visited[r][c]:
                    cnt += 1
                    bfs(r, c, day)
        mx = max(mx, cnt)
    print(f"#{tc} {mx}")