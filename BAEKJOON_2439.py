# BAEKJOON_2439번
# 첫째 줄에는 별 1개, 둘째 줄에는 별 2개, N번째 줄에는 별 N개를 찍는 문제
# 하지만, 오른쪽을 기준으로 정렬한 별(예제 참고)을 출력하시오.

N = int(input())
for i in range(N) :
    print(" "*(N-(i+1)) + "*"*(i+1))


# 쉼표로 구분할 경우, 띄어쓰기가 포함되므로 +로 구분해줌
# 혹은 print 함수에서 end = ""으로 해주어도 됨. 아래 예시 참고

# N = int(input())
# for i in range(N) :
#     print(" "*(N-(i+1)), end = "")
#     print("*"*(i+1))