# BAEKJOON 1712번 문제 : 손익분기점

# A : 고정비용, B : 가변비용, C : 노트북 가격

A, B, C = map(int, input().split())

if B >= C :
    print(-1)

else :
    print(int(A / (C-B) + 1))