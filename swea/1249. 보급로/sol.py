import sys
sys.stdin = open('input.txt', 'r')

from collections import deque

dy = [-1,0,1,0]
dx = [0,1,0,-1]

def go():
    q = deque([(0,0)])
    dist[0][0] = 0
    while q:
        y, x = q.popleft()
        for d in range(4):
            ny, nx = y+dy[d], x+dx[d]
            if 0<=ny<N and 0<=nx<N:
                new = dist[y][x] + arr[ny][nx]
                if new < dist[ny][nx]:
                    dist[ny][nx] = new
                    q.append((ny,nx))

    return dist[N-1][N-1]

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().strip())) for _ in range(N)]

    dist = [[float('inf')] * N for _ in range(N)]
    result = go()

    print(f"#{tc} {result}")