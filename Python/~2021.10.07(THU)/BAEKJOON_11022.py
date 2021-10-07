# BAEKJOON_11022번
# 문제 : 두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.
'''입력 : 첫째 줄에 테스트 케이스의 개수 T가 주어진다. 각 테스트 케이스는 한 줄로 이루어져 있으며, 
각 줄에 A와 B가 주어진다. (0 < A, B < 10)'''

# T = int(input())
# for i in range(T) :
#     A, B = input().split()
#     A, B = int(A), int(B)
#     print("Case #{}: {} + {} = {}".format((i+1), A, B, A+B))


# 다른 방법
for i in range(int(input())) :
    A, null, B = input()
    print("Case #{}: {} + {} = {}".format((i+1), A, B, int(A)+int(B)))