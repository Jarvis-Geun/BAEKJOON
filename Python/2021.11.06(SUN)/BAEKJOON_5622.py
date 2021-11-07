# BAEKJOON 5622번 : 다이얼

list = list(map(str, input()))

i = 0
sum = 0
for i in range(len(list)) :
    print(list[i])
    if (list[i] == 'A') or (list[i] == 'B') or (list[i] == 'C') :
        sum += 3

    elif (list[i] == 'D') or (list[i] == 'E') or (list[i] == 'F') :
        sum += 4

    elif (list[i] == 'G') or (list[i] == 'H') or (list[i] == 'I') :
        sum += 5

    elif (list[i] == 'J') or (list[i] == 'K') or (list[i] == 'L'):
        sum += 6

    elif (list[i] == 'M') or (list[i] == 'N') or (list[i] == 'O') :
        sum += 7

    elif (list[i] == 'P') or (list[i] == 'Q') or (list[i] == 'R') or (list[i] == 'S'):
        sum += 8
    
    elif (list[i] == 'T') or (list[i] == 'U') or (list[i] == 'V') :
        sum += 9

    elif (list[i] == 'W') or (list[i] == 'X') or (list[i] == 'Y') or (list[i] == 'Z'):
        sum += 10


print(sum)