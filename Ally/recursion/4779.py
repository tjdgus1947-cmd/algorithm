# BOJ 4779
# 내 풀이


# BOJ 4779 풀이 코드
# 1. bottom-up 방식(작은것 부터 큰 순으로 답을 구하는 방식)
# f(n) = f(n-1) + 공백 3**(n-1)개 + f(n-1)
ans = ["" for _ in range(13)]
ans[0] = "-"

for i in range(1, 13):
    ans[i] = ans[i - 1] + (" " * (3 ** (i - 1))) + ans[i - 1]

while True:
    try:
        N = int(input())
        print(ans[N])
    except:
        break


# 2. 재귀함수
def func(k):  # 입력이 k일때 답을 출력하는 함수
    # base case
    if k == 0:
        print("-", end="")
        return

    # recursive case
    func(k - 1)
    print(" " * (3 ** (k - 1)), end="")
    func(k - 1)


while True:
    try:
        N = int(input())
        func(N)
        print()
    except:
        break
