dy = [0, -1, 1, 0, 0]
dx = [0, 0, 0, -1, 1]
rev = [0, 2, 1, 4, 3]

T = int(input())
for tc in range(1, T + 1):
    N, M, K = map(int, input().split())
    groups = []
    for _ in range(K):
        y, x, cnt, d = map(int, input().split())
        groups.append((y, x, cnt, d))                 # ① 입력은 여기까지

    for _ in range(M):                                # ② M시간
        moved = []
        for y, x, cnt, d in groups:                   # a. 이동 + 약품
            ny, nx = y + dy[d], x + dx[d]
            if ny == 0 or ny == N-1 or nx == 0 or nx == N-1:
                cnt = cnt//2
                d = rev[d]
                if cnt == 0:
                    continue                               # 사라짐 → 다음 군집으로
            moved.append((ny, nx, cnt, d))

        new = {}                                      # b. 합치기
        for y, x, cnt, d in moved:
            key = (y, x)
            if key not in new:
                new[key] = [cnt, cnt, d]
            else:
                new[key][0] += cnt
                if cnt > new[key][1]:
                    new[key][1] = cnt
                    new[key][2] = d

        groups = []                                   # c. 다시 리스트로
        for (y, x), (total, mx, d) in new.items():
            groups.append((y, x, total, d))

    answer = sum(cnt for y, x, cnt, d in groups)      # ③
    print(f"#{tc} {answer}")