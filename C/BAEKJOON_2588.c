#include <stdio.h>

int main()	{
	int i, j;

	scanf("%d", &i);
	scanf("%d", &j);

	printf("%d\n", i*(j%10));
	printf("%d\n", i*((j/10)%10));
	printf("%d\n", i*(j/100));
	printf("%d\n", i*j);

	return 0;
}
