import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

def dp_go():
    dp = [0] * (300+1)
    dp[0] = 0
    dp[1] = stairs[1]
    dp[2] = stairs[1] + stairs[2]

    for i in range(3, N+1):
        dp[i] = max(dp[i-2]+stairs[i], dp[i-3]+stairs[i-1]+stairs[i])

    return dp[N]

N = int(input())
stairs = [0] + [int(input()) for _ in range(N)] + [0] * (300-N)
result = dp_go()

print(result)