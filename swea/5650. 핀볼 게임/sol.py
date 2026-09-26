import sys
sys.stdin = open('input.txt', 'r')

dy = [-1,0,1,0]
dx = [0,1,0,-1]

turn = [[],
        [2,3,1,0],
        [1,3,0,2],
        [3,2,0,1],
        [2,0,3,1],
        [2,3,0,1],
        [2,3,0,1]]

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    warm = [6,7,8,9,10]
    holes = {}
    warm_dict = {}
    for y in range(N):
        for x in range(N):
            if arr[y][x] in warm:
                if arr[y][x] not in holes:
                    holes[arr[y][x]] = []
                holes[arr[y][x]].append((y,x))

    for hole in holes:
        a, b = holes[hole]
        warm_dict[a] = b
        warm_dict[b] = a
    # print(warm_dict)

    answer = 0
    for sy in range(N):
        for sx in range(N):
            if arr[sy][sx] != 0:
                continue
            for sd in range(4):
                y, x, d = sy, sx, sd       # 현재 위치·방향 (출발값 복사)
                cnt = 0
                while True:
                    y += dy[d]             # [a] 한 칸 이동
                    x += dx[d]

                    # [b] 벽: 판 밖으로 나갔으면
                    if not (0 <= y < N and 0 <= x < N):
                        d = turn[5][d]
                        cnt += 1
                        continue           # 다음 바퀴에 판 안으로 되돌아옴

                    # [c] 종료: 출발 위치로 돌아왔거나 블랙홀(-1)
                    if (y==sy and x==sx) or arr[y][x]==-1:
                        break

                    v = arr[y][x]
                    # [d] 블록 1~5
                    if 1 <= v <= 5:
                        d = turn[v][d]
                        cnt += 1
                    # [e] 웜홀 6~10
                    elif v >= 6:
                        y, x = warm_dict[(y,x)]

                answer = max(answer, cnt)
    print(f"#{tc} {answer}")