# 백준 1193번 문제 : 분수찾기

X = int(input())
X_1 = X
row = 1
sum = 0

# 몇번째 행에 위치하는지 계산
while(1) :
    X_1 -= row
    if X_1 <= 0 :
        break
    sum += row
    row += 1

total_num = 0
total_num += sum
i = 1

if row % 2 == 1 :
    while(total_num < X) :
        if total_num == X-1 :
            print("{}/{}".format((row+1)-i, i))
        i += 1
        total_num += 1

else :
    while(total_num < X) :
        if total_num == X-1 :
            print("{}/{}".format(i, (row+1)-i))
        i += 1
        total_num += 1


# 다른 방법
'''
n = int(input())

k = 0
while (k*(k+1))/2 < n:
    k += 1

s = int(n - (k*(k-1)/2)) -1

if k % 2 == 0:
    print(f'{1+s}/{k-s}')
else:
    print(f'{k-s}/{1+s}')
'''