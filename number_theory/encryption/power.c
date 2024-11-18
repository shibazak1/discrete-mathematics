/* 2024/6/20
   compute the x^n useing recuresion
   wite it by VIIBUG 
 */
#include<stdio.h>

int  pow1(int x,int n){

    if(n==0){
	return 1;
    }
    else{

	return x*pow1(x,n-1);
    }
}

int pow2(int x,int n){

    if(n==0){
	return 1;
    }
    else if(n%2==0){

	int y = pow2(x,n/2);
	return y*y;

    }
    else{

	return x*pow2(x,n-1);
    }



}





int main(void){



    printf("\n%d\n",pow1(2,9));
    printf("%d",pow2(2,9));


    return 0;
}
