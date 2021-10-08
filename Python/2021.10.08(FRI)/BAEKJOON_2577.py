# BAEKJOON 2577번 문제 : 숫자의 개수

A = int(input())
B = int(input())
C = int(input())

mul = A * B * C

x = [int(i) for i in str(mul)]

for i in range(10) :
    print(x.count(i))