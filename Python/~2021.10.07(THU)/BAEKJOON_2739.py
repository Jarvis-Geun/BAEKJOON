# BAEKJOON 2739번 문제 : 구구단
# N을 입력받은 뒤, 구구단 N단을 출력하는 프로그램을 작성하시오. 출력 형식에 맞춰서 출력하면 된다.

N = int(input())

for i in range(9) :
    print("{} * {} = {}".format(N, (i+1), N*(i+1)))