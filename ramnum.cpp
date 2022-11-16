#include<stdio.h>
#include<conio.h>
int main()
{
	int xo,x1; /*xo=seed, x1=next random number that we will generate */
	int a,c,m; /*a=constant multiplier, c=increment, m=modulus */
	int i,n; /*i for loopcontrol, n for how many random numbers */
	int array[20]; /*to store the random numbers generated */
	
	printf("Enter the seed value xo: ");
	scanf("%d",&xo);
	printf("\n");
	
	printf("Enter the constant multiplier a: ");
	scanf("%d",&a);
	printf("\n");
	
	printf("Enter the increment c: ");
	scanf("%d",&c);
	printf("\n");	
	 
	printf("Enter the modulus m: ");
	scanf("%d",&m);
	printf("\n");
	printf("How many random numbers you want to generate: ");
	scanf("%d",&n);
	printf("\n");				
	
	for(i=0;i<n;i++) /* loop to generate random numbers */
	{
		x1=(a*xo+c) %m;
		array[i]=x1;
		xo=x1;
		}
	
	
	printf("The generated random numbers are: ");
	for(i=0;i<n;i++)
	{
		printf("%d",array[i]);
		printf("\t");
	}
	
	getch();
	return(0);
	
}
