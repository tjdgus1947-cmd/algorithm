import sys
sys.stdin = open('input.txt', 'r')

dy = [1,1,-1,-1]
dx = [1,-1,-1,1]

def go(y, x, length, d):
    global result

    for nd in (d, d+1):
        if nd == 4:
            break
        ny, nx = y+dy[nd], x+dx[nd]
        if not (0<=ny<N and 0<=nx<N):
            continue
        if nd == 3 and ny==r and nx==c:
            result = max(result, length)
            continue
        if arr[ny][nx] in s:
            continue
        s.add(arr[ny][nx])
        go(ny, nx, length+1, nd)
        s.remove(arr[ny][nx])


    
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    result = -1
    s = set()
    for r in range(N):
        for c in range(N):
            s.add(arr[r][c])
            go(r, c, 1, 0)
            s.remove(arr[r][c])

    print(f"#{tc} {result}")