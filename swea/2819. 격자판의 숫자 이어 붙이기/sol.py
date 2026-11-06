import sys
sys.stdin = open('input.txt', 'r')
sys.setrecursionlimit(10**6)

dy = [-1,0,1,0]
dx = [0,1,0,-1]

def go(y, x, s):

    if len(s) == 7:
        nums.add(s)
        return
            
    for d in range(4):
        ny, nx = y+dy[d], x+dx[d]
        if 0<=ny<4 and 0<=nx<4:
            go(ny, nx, s + str(arr[ny][nx]))


T = int(input())
for tc in range(1, T+1):
    arr = [list(map(int, input().split())) for _ in range(4)]
    nums = set()

    for r in range(4):
        for c in range(4):
            go(r,c,str(arr[r][c]))

    result = len(nums)

    print(f"#{tc} {result}")