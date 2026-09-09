from collections import deque

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
op = [1, 0, 3, 2]

tunnel = {
    1: [0, 1, 2, 3],
    2: [0, 1],
    3: [2, 3],
    4: [0, 3],
    5: [1, 3],
    6: [1, 2],
    7: [0, 2],
}

T = int(input())
for tc in range(1, T + 1):
    N, M, R, C, L = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    visited = [[False] * M for _ in range(N)]
    visited[R][C] = True
    q = deque([(R, C, 1)])
    cnt = 0

    while q:
        r, c, t = q.popleft()
        cnt += 1

        if t == L:
            continue

        for d in tunnel[arr[r][c]]:
            nr, nc = r + dr[d], c + dc[d]
            if 0 <= nr < N and 0 <= nc < M:
                if not visited[nr][nc] and arr[nr][nc] != 0:
                    if op[d] in tunnel[arr[nr][nc]]:
                        visited[nr][nc] = True
                        q.append((nr, nc, t + 1))

    print(f"#{tc} {cnt}")
