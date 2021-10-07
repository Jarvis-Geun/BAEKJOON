# BAEKJOON_11720번 문제
# N개의 숫자가 공백 없이 쓰여있다. 이 숫자를 모두 합해서 출력하는 프로그램을 작성하시오.

# N = int(input())
# print(sum(map(int, input())))

N = int(input())
list = list(map(int, input("")))
sum = sum(list)
print(sum)