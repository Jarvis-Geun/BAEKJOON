# BAEKJOON 4344 : 평균은 넘기겠지

C = int(input())

j = 0
while(j < C) :
    arr = list(map(int, input().split()))
    SUM = sum(arr[1:])
    avg = SUM / len(arr[1:])

    num = 0
    for i in range(len(arr[1:])) :
        if arr[i+1] > avg :
            num += 1
    print("{:.3f}%".format((num / len(arr[1:])) * 100))

    j += 1