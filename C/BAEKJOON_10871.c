// BAEKJOON_10871
// X���� ���� ��.
// ���� N���� �̷���� ���� A�� ���� X�� �־�����.
// �̶�, A���� X���� ���� ���� ��� ����ϴ� ���α׷��� �ۼ��Ͻÿ�.

#include <stdio.h>

int main(void)	{
	int N, X, i;
	int a;
	
	scanf("%d %d", &N, &X);
	
	for(i=0; i<N; i++)	{
		scanf("%d", &a);
		if(a<X)	printf("%d ", a);
	}
		
	return 0;
} 
