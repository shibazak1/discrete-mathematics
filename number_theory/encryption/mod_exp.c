#include<stdio.h>

long int mod(long int x,long int n,int m){

    if(n==0){

	return 1;
    }
    else if(n%2==0){

	int y = mod(x,n/2,m);
	return (y*y)%m;
    }
    else{

	return ((x%m)*mod(x,n-1,m)%m);
    }


}

long int mod2(long int x,long int n,long int m){

    if(n==0){

	return 1;
    }
    if(n==1){

	return x;
    }
    if(n%2==0){

	return mod2((x*x)%m,n/2,m);

    }
    else{

	return (mod2(x,n-1,m)*x)%m;
	
    }




}



int main(void){

    printf("%Ld",mod2(314159265358, 2718281828, 123456789));


}
