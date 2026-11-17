import sys
sys.stdin = open('input.txt', 'r')

dy = [-1,0,1,0]
dx = [0,1,0,-1]



T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    lst = [0] * (N*N + 1)
    for r in range(N):
        for c in range(N):
            for d in range(4):
                nr, nc = r+dy[d], c+dx[d]
                if 0<=nr<N and 0<=nc<N and (arr[nr][nc] == arr[r][c] + 1):
                    lst[arr[r][c]] = 1
    
    cur = 0
    start = 0
    best_start = 1
    best_cur = 0

    for i in range(1, N*N + 1):
        if lst[i] == 1:
            if cur == 0:              
                start = i           
            cur += 1                  
            if cur > best_cur:        
                best_cur = cur        
                best_start = start    

                
        else:
            cur = 0                  

    print(f"#{tc} {best_start} {best_cur + 1}")







