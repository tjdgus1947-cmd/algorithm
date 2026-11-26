import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

def dp_go():
    max_n = 10**6
    dp = [0] * (max_n+1)
    dp[1] = 0
    dp[2] = 1
    dp[3] = 1
    for i in range(4, max_n+1):
        dp[i] = dp[i-1] + 1
        if i % 2 ==0:
            dp[i] = min(dp[i], dp[i//2]+1)
        if i % 3 ==0:
            dp[i] = min(dp[i], dp[i//3]+1)
    return dp

dp = dp_go()

T = 2
for tc in range(1, T+1):
    print(dp[int(input())])