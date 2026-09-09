# 함수의 일종이며, 재귀함수는 함수 내에서 자기 자신을 호출하는 함수를 의미


# "1부터 n까지 더하는 함수를 만들어보세요."
# 함수를 이용하여 구현
def sum_func(n):
    ret = 0
    for i in range(1, n + 1):
        ret += i
    return ret


# 재귀함수를 이용하여 구현
def sum_func(n):
    if n == 1:
        return 1
    return sum_func(n - 1) + n
