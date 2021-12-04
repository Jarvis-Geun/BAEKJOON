# BAEKJOON 1181번 문제 : 단어정렬
# 못품
'''
N = int(input())
words = []

for i in range(N) :
    words.append(str(input()))

words_set_list = list(set(words))
words_set_list.sort()
words_sort = words_set_list

print(words_sort)

min = 51
for i in range(len(words_set_list)) :
    if len(words_sort[i]) < min :
        min = len(words_sort)
        min_arg = i

print(words_sort.pop(min_arg))
print(i)
'''