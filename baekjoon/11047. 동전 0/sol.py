import sys
sys.stdin = open('input2.txt', 'r')

N, K = map(int, input().split())
types = [int(input()) for _ in range(N)][::-1]
ans = 0

for i in range(len(types)):
    ans += (K // types[i])
    K = K % types[i]

print(ans)