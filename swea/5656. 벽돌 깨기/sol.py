import sys
sys.stdin = open('input.txt', 'r')
from itertools import product
from collections import deque

dy = [-1,0,1,0]
dx = [0,1,0,-1]

T = int(input())
for tc in range(1, T+1):
    N, W, H = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(H)]
    answer = float('inf')          

    for order in product(range(W), repeat=N):
        board = [row[:] for row in arr]

        for c in order:
            # [1]
            top = -1
            for h in range(H):
                if board[h][c] != 0:
                    top = h
                    break
            if top == -1:
                continue

            # [2] 연쇄 폭발
            q = deque()
            q.append((top,c))
            while q:
                y, x = q.popleft()
                v = board[y][x]
                board[y][x] = 0
                for d in range(4):
                    for i in range(1,v):
                        ny, nx = y+dy[d]*i, x+dx[d]*i
                        if 0<=ny<H and 0<=nx<W and board[ny][nx] != 0:
                            q.append((ny,nx))
            # [3] 중력
            for w in range(W):
                not0_lst = []
                for h in range(H):
                    if board[h][w] != 0:
                        not0_lst.append(board[h][w])
                change_lst = [0] * (H - len(not0_lst)) + not0_lst
                for h in range(H):
                    board[h][w] = change_lst[h]
        cnt = 0
        for h in range(H):
            for w in range(W):
                if board[h][w] != 0:
                    cnt += 1
        answer = min(answer, cnt)
        if answer ==0:
            break 
    print(f"#{tc} {answer}")