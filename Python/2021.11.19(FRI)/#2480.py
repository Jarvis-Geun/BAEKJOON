# BAEKJOON 2480번 문제 : 주사위 세개
# 같은 눈 3개 : 10,000 + (같은 눈) x 1,000
# 같은 눈 2개 : 1,000 + (같은 눈) x 100
# 모두 다른 눈 : (가장 큰 눈) x 100

a = list(map(int, input().split()))
print(a[0], a[1], a[2])

if a[0] == a[1] == a[2] :
    print(10000+a[0]*1000)

elif a[0] == a[1] :
    print(1000+a[0]*100)

elif a[1] == a[2] :
    print(1000+a[1]*100)

elif a[2] == a[0] :
    print(1000+a[2]*100)

else :
    print(100*max(a[0], a[1], a[2]))