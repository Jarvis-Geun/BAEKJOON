// BAEKJOON_10871
// X보다 작은 수.
// 정수 N개로 이루어진 수열 A와 정수 X가 주어진다.
// 이때, A에서 X보다 작은 수를 모두 출력하는 프로그램을 작성하시오.

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
