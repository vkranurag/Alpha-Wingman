#include<stdio.h> 
#include<stdlib.h> 
int main()
{
    FILE *p;
    p=fopen("Stud.txt","r"); 
    int c=0,w=0;
    char a; 
    while ((a=fgetc(p))!=EOF)
    {
        c++;
        if (a==' '||a=='\n'||a=='\t'||a=='\0')
         w++;
    }
    printf("No of Words are : %d",w);
    printf("No of Characters are: %d",c);  
    fclose(p);
    return 0;
}