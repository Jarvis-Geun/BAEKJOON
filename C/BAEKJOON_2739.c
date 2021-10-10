// 백준 2739번 문제 : 구구단 

#include <stdio.h>

int main()	{
	int N=0;
	int i, j;
	
	scanf("%d", &N);
	
	for(i=1; i<10; i++)	
		printf("%d * %d = %d\n", N, i, N*i);
	
	return 0;
}
