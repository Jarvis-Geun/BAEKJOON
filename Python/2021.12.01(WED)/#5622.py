# 백준 5622번 문제 : 다이얼

'''
arr = list(input())
sum = 0

for i in range(len(arr)) :        
    if ord(arr[i]) >= ord('A') and ord(arr[i]) <= ord('C'):     # ord : 문자를 아스키 코드 반환
        sum += 3

    elif ord(arr[i]) >= ord('D') and ord(arr[i]) <= ord('F'):
        sum += 4

    elif ord(arr[i]) >= ord('G') and ord(arr[i]) <= ord('I'):
        sum += 5

    elif ord(arr[i]) >= ord('J') and ord(arr[i]) <= ord('L'):
        sum +=6

    elif ord(arr[i]) >= ord('M') and ord(arr[i]) <= ord('O'):
        sum += 7

    elif ord(arr[i]) >= ord('P') and ord(arr[i]) <= ord('S'):
        sum += 8

    elif ord(arr[i]) >= ord('T') and ord(arr[i]) <= ord('V'):
        sum += 9

    elif ord(arr[i]) >= ord('W') and ord(arr[i]) <= ord('Z'):
        sum += 10

print(sum)
'''

# 다른 코드(백준 참고함)
dial = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']

arr = input()
sum = 0

for j in range(len(arr)) :
    for i in dial :
        if arr[j] in i :
            sum += dial.index(i) + 3

print(sum)