// BAEKJOON_1712
// 손익분기점

#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main(void) {
	int A = 0, B = 0, C = 0;		// A : 고정수익, B : 가변비용, C : 노트북 가격
	int num = 0;					// num : 손익분기점을 넘기 시작할 때의 노트북 개수

	scanf("%d %d %d", &A, &B, &C);

	if (B >= C)	printf("-1");

	else
	{
		printf("%d", A / (C - B) + 1);
	}

	return 0;
}
