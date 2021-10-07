# BAEKJOON 2884번 문제 : 알람 시계
# 지정한 시간보다 45분 이른 시간 표시하기

H, M = map(int, input().split())

if M >= 45 :
    M = M-45
else :
    M = (M+60)-45
    H = H-1
    
    if H < 0 :
        H = H+24

print(H, M)