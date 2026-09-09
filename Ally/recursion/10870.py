# BOJ 10870
# 내 풀이
def fibo(x):
    if x == 0:
        return 0
    elif x == 1:
        return 1
    return fibo(x - 1) + fibo(x - 2)


n = int(input())
print(fibo(n))

# BOJ 10870 풀이 코드
# 1. 반복문 + 메모이제이션
n = int(input())

arr = [-1] * (n + 2)  # 나올 수 없는 값으로 초기값(-1) 설정
arr[0] = 0
arr[1] = 1

for i in range(2, n + 1):
    arr[i] = arr[i - 1] + arr[i - 2]

print(arr[n])


# 2. 재귀함수
def fibo(x):
    # base case
    if x == 0:
        return 0
    if x == 1:
        return 1

    # recursive case
    return fibo(x - 1) + fibo(x - 2)


n = int(input())
print(fibo(n))


# 3. 재귀함수 + 메모이제이션
def fibo(x):
    global arr

    # base case
    if arr[x] != -1:  # 구해놓은 값이 있다면 다시 구하지 않고 바로 해당 값을 사용
        return arr[x]

    # recursive case
    arr[x] = fibo(x - 1) + fibo(x - 2)
    return arr[x]


n = int(input())

arr = [-1] * (n + 2)
arr[0] = 0  # 초기값 써줘야 함
arr[1] = 1

print(fibo(n))


## 똑같은 값을 여러 번 구한다면, 배열에 저장하여 재사용하는 것이 좋다.(메모이제이션 기법)
