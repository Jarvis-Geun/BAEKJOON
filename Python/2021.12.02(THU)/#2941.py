# 백준 2941번 문제 : 크로아티아 알파벳

croa_alpha = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

alpha_input = input()

for i in croa_alpha :
    # replace 함수를 사용하여 크로아티아 알파벳을 0으로 대체
    alpha_input = alpha_input.replace(i, '0')

print(len(alpha_input))