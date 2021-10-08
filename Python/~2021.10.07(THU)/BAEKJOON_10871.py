# 정수 N개로 이루어진 수열 A와 정수 X가 주어진다. 이때, A에서 X보다 작은 수를 모두 출력하는 프로그램을 작성하시오.

'''
N, X = map(int, input().split())

list = list(map(int, input().split()))
less_num = []
for i in range(N) :
    if list[i] < X :
        less_num.append(list[i])

for i in range(len(less_num)) :
    print(less_num[i], end=" ")

'''

# 더 간결한 코드
N, X = map(int, input().split())

A = list(map(int, input().split()))

for i in range(len(A)) :
    if A[i] < X :
        print(A[i], end=" ")