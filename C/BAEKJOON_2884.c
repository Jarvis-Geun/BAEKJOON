// BAEKJOON_2884
// "45분 일찍" 알람시계

#include <stdio.h>

int main(void)	{
	int Hi, Mi;	// 0<=Hi<=23, 0<=Mi<=59 ==> H시 M분(input 값) 
				// 불필요한 0 사용x ==> 0:0(자정, 하루의 시작), 23:59(자정 1분 전, 하루의 끝) 
	int Ho, Mo; // output 값(45분 감소된 값)
	 
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
