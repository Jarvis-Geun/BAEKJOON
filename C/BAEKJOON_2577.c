// 백준 2577번 문제 : 숫자의 개수 

#include <stdio.h>

int main(void)  {
    int A, B, C;
    int i = 1, result = 0, number = 0;
    
    scanf("%d", &A);
    scanf("%d", &B);
    scanf("%d", &C); 
    
    result = A*B*C;
    int num[10] = {0, };        // 0~9까지의 나머지를 넣을 배열 선언
    
    while(result > 0) {
    	number = result % 10; 
        result /= 10;
        num[number] += 1;		// 10으로 나눈 나머지를 배열에 넣음 
        i++;
    }
    
    for(i=0; i<10; i++) {
    	printf("%d\n", num[i]);
	}

    return 0;
}
