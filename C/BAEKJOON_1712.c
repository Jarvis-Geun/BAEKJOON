// BAEKJOON_1712
// ���ͺб���

#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main(void) {
	int A = 0, B = 0, C = 0;		// A : ��������, B : �������, C : ��Ʈ�� ����
	int num = 0;					// num : ���ͺб����� �ѱ� ������ ���� ��Ʈ�� ����

	scanf("%d %d %d", &A, &B, &C);

	if (B >= C)	printf("-1");

	else
	{
		printf("%d", A / (C - B) + 1);
	}

	return 0;
}
