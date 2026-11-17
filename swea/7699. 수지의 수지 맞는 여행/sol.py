import sys
sys.stdin = open('input.txt', 'r')

dy = [-1,0,1,0]
dx = [0,1,0,-1]

def go(y,x,length):
    global result
    result = max(result, length)
    for d in range(4):
        ny, nx = y+dy[d], x+dx[d]
        if 0<=ny<R and 0<=nx<C and arr[ny][nx] not in s:
            s.add(arr[ny][nx])
            go(ny, nx, length+1)
            s.remove(arr[ny][nx])


T = int(input())
for tc in range(1, T+1):
    R, C = map(int, input().split())
    arr = []
    for _ in range(R):
        arr.append(input().strip())
    s = set()
    result = float('-inf')
    s.add(arr[0][0])
    go(0,0,1)
    print(f"#{tc} {result}")