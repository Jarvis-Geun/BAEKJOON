// 백준 11720번 문제 : 숫자의 합 

#include <stdio.h>
int main(void) { 
	int N, i, sum = 0; 
	char arr[101] = { 0, };
	
	scanf("%d", &N);
	scanf("%s", arr);			// scanf_s로 문자열을 입력받을 경우, 마지막 인자에 메모리 크기를 적어주어야 오류가 발생하지 않음.
	
	for (i = 0; i < N; i++)		sum += (arr[i] - '0');	// 아스키 코드를 이용하여 품.

	printf("%d", sum); 
	
	return 0; 
}
