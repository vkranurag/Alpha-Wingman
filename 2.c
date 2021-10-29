#include<stdio.h> 
#include<stdlib.h> 
int main()
{
    char n[30]; 
    FILE *p;
    p=fopen("Stud.txt","r"); 
    printf("The inputed student names are: \n"); 
    while(fscanf(p,"%s",n)!=EOF)
    printf("%s\n",n); 
    fclose(p); 
    return 0;
}