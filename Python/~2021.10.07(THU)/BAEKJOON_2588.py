# 백준 2588번 문제 : 곱셈

a = int(input())
b = int(input())

print(a * (b%10))
print(a * ((b//10) % 10))
print(a * (b//100))
print(a * b)