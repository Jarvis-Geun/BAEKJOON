// BAEKJOON_10818
// N���� ������ �־�����. �̶�, �ּڰ��� �ִ��� ���ϴ� ���α׷��� �ۼ��Ͻÿ�.

#include <stdio.h>

int main(void) {
	int N = 0, num = 0;
	int min = 1000000;
    int max = -1000000;
    int i;
	
	scanf("%d", &N);

	for (i = 0; i < N; i++) {
		scanf("%d", &num);
		if (num >= max)	max = num;
		if (num <= min) min = num;
	}

	printf("%d %d", min, max);
    return 0;
}
