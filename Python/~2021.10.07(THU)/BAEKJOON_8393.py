# BAEKJOON_8393번 문제
# 문제 : n이 주어졌을 때, 1부터 n까지 합을 구하는 프로그램을 작성하시오.
# 입력 : 첫째 줄에 n (1 ≤ n ≤ 10,000)이 주어진다.

# sum = 0
# for i in range(1, int(input())+1) :
#     sum += i
# print(sum)


# 다른 방법
n = int(input())
print(int(n*(n+1)/2))