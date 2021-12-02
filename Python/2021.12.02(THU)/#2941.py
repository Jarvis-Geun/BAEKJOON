# 백준 2941번 문제 : 크로아티아 알파벳

croa_alphabet = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

word = input()

for j in range(len(word)) :
    for i in range(3) :
        if word[j:i] == croa_alphabet[j]