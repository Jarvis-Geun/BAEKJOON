// ���� 11720�� ���� : ������ �� 

#include <stdio.h>
int main(void) { 
	int N, i, sum = 0; 
	char arr[101] = { 0, };
	
	scanf("%d", &N);
	scanf("%s", arr);			// scanf_s�� ���ڿ��� �Է¹��� ���, ������ ���ڿ� �޸� ũ�⸦ �����־�� ������ �߻����� ����.
	
	for (i = 0; i < N; i++)		sum += (arr[i] - '0');	// �ƽ�Ű �ڵ带 �̿��Ͽ� ǰ.

	printf("%d", sum); 
	
	return 0; 
}
