import sys
sys.stdin = open('input.txt', 'r')
from collections import deque

dy = [-1,0,1,0]
dx = [0,1,0,-1]

def go(y,x):
    q = deque([(y,x)])
    while q:
        y,x = q.popleft()
        for d in range(4):
            ny, nx = y+dy[d], x+dx[d]
            if 0<=ny<N and 0<=nx<N:
                new = dist[y][x] + arr[ny][nx]
                if dist[ny][nx] > new:
                    dist[ny][nx] = new
                    q.append((ny,nx))
    
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().strip())) for _ in range(N)]
    dist = [[float('inf')] * N for _ in range(N)]
    dist[0][0] = 0
    go(0,0)
    result = dist[N-1][N-1]

    print(f"#{tc} {result}")