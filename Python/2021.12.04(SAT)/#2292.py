# 백준 1316번 문제 : 그룹 단어 체커

num = int(input())
a_n = 1

for n in range(1, num) :

    a_n = a_n + 6*n

    if num <= a_n :
        print(n+1)
        break

if num == 1 :
    print(1)