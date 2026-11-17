import sys
sys.stdin = open('input.txt', 'r')

def go(cnt, total):
    global result

    if total > result:
        return

    if total >= B:
        result = min(total, result)

    if cnt == N:
        return
    
    go(cnt+1, total + heights[cnt])
    go(cnt+1, total)

T = int(input())
for tc in range(1, T+1):
    N, B = map(int, input().split())
    heights = list(map(int, input().split()))
    result = float('inf')
    go(0,0)
    sol = result - B

    print(f"#{tc} {sol}")