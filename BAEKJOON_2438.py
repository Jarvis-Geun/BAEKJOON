# BAEKJOON 2438번 문제
# 첫째 줄에는 별 1개, 둘째 줄에는 별 2개, N번째 줄에는 별 N개를 찍는 문제

N = int(input())

for i in range(N) :
    star = "*"
    print(star*(i+1))


# 또는 아래와 같은 방법이 있음
# for i in range(int(input())) :
#     print("*"*(i+1))