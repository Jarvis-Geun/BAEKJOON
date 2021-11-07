# BAEKJOON 4673번 : 셀프넘버

dn = 0
num = 1
arr = list(0 for i in range(0, 10000))
arr[0] = 1

while(1) :
    dn = num + num // 1000 + (num // 100 % 10) + (num // 10 % 10) + (num % 10)
    
    if dn >= 10000 :
        break
    arr[dn] = dn
    num += 1

for i in range(len(arr)) :

    if arr[i] == 0 :
        print(i)

    if arr[i] > 9993 :
        break