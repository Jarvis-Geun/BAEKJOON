// ���� 2577�� ���� : ������ ���� 

#include <stdio.h>

int main(void)  {
    int A, B, C;
    int i = 1, result = 0, number = 0;
    
    scanf("%d", &A);
    scanf("%d", &B);
    scanf("%d", &C); 
    
    result = A*B*C;
    int num[10] = {0, };        // 0~9������ �������� ���� �迭 ����
    
    while(result > 0) {
    	number = result % 10; 
        result /= 10;
        num[number] += 1;		// 10���� ���� �������� �迭�� ���� 
        i++;
    }
    
    for(i=0; i<10; i++) {
    	printf("%d\n", num[i]);
	}

    return 0;
}
