// BAEKJOON_2884
// "45�� ����" �˶��ð�

#include <stdio.h>

int main(void)	{
	int Hi, Mi;	// 0<=Hi<=23, 0<=Mi<=59 ==> H�� M��(input ��) 
				// ���ʿ��� 0 ���x ==> 0:0(����, �Ϸ��� ����), 23:59(���� 1�� ��, �Ϸ��� ��) 
	int Ho, Mo; // output ��(45�� ���ҵ� ��)
	 
	scanf("%d %d", &Hi, &Mi);
	
	if(Mi-45>=0)	{
		Mo = Mi-45;
		Ho = Hi;
	}
	
	else if(Mi-45<0)	{
		Mo = (Mi+60)-45;
		Ho = Hi-1;
		
		if(Ho<0)	Ho = Ho+24;
	}
	
	printf("%d %d", Ho, Mo);
	
	return 0;		
} 
