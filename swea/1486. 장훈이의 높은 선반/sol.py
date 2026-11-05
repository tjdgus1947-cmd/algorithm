import sys
sys.stdin = open('input.txt', 'r')

def go(i, total):
    global result

    if total - B >= result:
        return

    if i == N:
        if total >= B:
            diff = total-B
            result = min(result, diff)
        return
    
    go(i+1, total+height[i])
    go(i+1, total)

T = int(input())
for tc in range(1, T+1):
    N, B = map(int, input().split())
    height = list(map(int, input().split()))
    result = float("inf")

    go(0, 0)
    print(f"#{tc} {result}")