# 백준 8959번 문제 : OX퀴즈
'''
"OOXXOXXOOO"와 같은 OX퀴즈의 결과가 있다. O는 문제를 맞은 것이고, X는 문제를 틀린 것이다. 문제를 맞은 경우 그 문제의 점수는 그 문제까지 연속된 O의 개수가 된다. 예를 들어, 10번 문제의 점수는 3이 된다.

"OOXXOXXOOO"의 점수는 1+2+0+0+1+0+0+1+2+3 = 10점이다.

OX퀴즈의 결과가 주어졌을 때, 점수를 구하는 프로그램을 작성하시오.
'''

tc = int(input())   # tc : test case
num = 0             # num : j번째 O의 개수, X가 나오면 0으로 초기화하고 O가 나오면 +1 증가
sum = 0             # sum : O의 개수의 합
OX = []

for i in range(tc) :
    OX = input()
    OX = list(OX)

    for j in range(len(OX)) :
        if OX[j] == 'O' :
            num += 1

        else :
            num = 0

        sum += num

    print(sum)
    sum = 0
    num = 0