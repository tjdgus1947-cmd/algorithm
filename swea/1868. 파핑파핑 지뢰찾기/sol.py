import sys
sys.stdin = open('input.txt', 'r')

from collections import deque

dy = [-1,0,1,0,-1,1,1,-1]
dx = [0,1,0,-1,1,1,-1,-1]

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [input().strip() for _ in range(N)]

    num = [[0] * N for _ in range(N)]
    
    for r in range(N):
        for c in range(N):
            if arr[r][c] == '*':
                num[r][c] = -1
                continue
            for d in range(8):
                nr, nc = r+dy[d], c+dx[d]
                if 0<=nr<N and 0<=nc<N and arr[nr][nc] == '*':
                    num[r][c] += 1

    visited = [[False] * N for _ in range(N)]
    cnt = 0
    for r in range(N):
        for c in range(N):
            if num[r][c] == 0 and not visited[r][c]:
                cnt += 1
                q = deque([(r,c)])
                visited[r][c] = True
                while q:
                    y, x = q.popleft()
                    for d in range(8):
                        ny, nx = y+dy[d], x+dx[d]
                        if 0<=ny<N and 0<=nx<N and not visited[ny][nx] and num[ny][nx] != -1:
                            visited[ny][nx] = True
                            if num[ny][nx] == 0:
                                q.append((ny,nx))

    for r in range(N):
        for c in range(N):
            if num[r][c] > 0 and visited[r][c] == False:
                cnt += 1

    print(f'#{tc} {cnt}')