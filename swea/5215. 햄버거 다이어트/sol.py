import sys
sys.stdin = open('input.txt', 'r')

def go(i, cals, score):
    global result
    if cals > L:
        return
    
    if i==N:
        result = max(score, result)
        return

    go(i+1, cals+cals_lst[i], score+score_lst[i])
    go(i+1, cals, score)
    
T = int(input())
for tc in range(1, T+1):
    N, L = map(int, input().split())
    score_lst = []
    cals_lst = []
    result = float("-inf")

    for _ in range(N):
        score, cals = map(int, input().split())
        score_lst.append(score)
        cals_lst.append(cals)

    go(0,0,0)
    print(f"#{tc} {result}")