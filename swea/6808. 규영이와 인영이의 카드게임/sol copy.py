# itertools 사용

import sys
sys.stdin = open('input.txt', 'r')
from itertools import permutations

def get_score(young):
    global win, lose
    gyu_score = 0
    young_score = 0
    for i in range(9):
        if gyu[i] > young[i]:
            gyu_score += gyu[i] + young[i]
        if gyu[i] < young[i]:
            young_score += gyu[i] + young[i]
    if gyu_score > young_score:
        win += 1
    if young_score > gyu_score:
        lose += 1

    
T = int(input())
for tc in range(1, T+1):
    gyu = list(map(int, input().split()))
    young = []
    win = 0
    lose = 0
    for i in range(1,19):
        if i not in gyu:
            young.append(i)
    for perm in permutations(young, 9):
        get_score(perm)

    print(f"#{tc} {win} {lose}")