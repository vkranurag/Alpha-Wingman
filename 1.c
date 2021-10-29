#include <stdio.h>
#include <string.h>
#include <stdlib.h>
struct student
{
    char name[20];
    int rollno;
    float cgpa;
}stud;

void insert()
{
    FILE *fp;
    fp = fopen("Record", "a");
    printf("Enter the Roll no: ");
    scanf("%d", &stud.rollno);
    printf("Enter the Name: ");
    scanf("%s", &stud.name);
    printf("Enter the cgpa: ");
    scanf("%f", &stud.cgpa);
    fwrite(&stud, sizeof(stud), 1, fp);
    fclose(fp);
}

void disp()
{
    FILE *fp1;
    fp1 = fopen("Record", "r");
    while (fread(&stud, sizeof(stud), 1, fp1))
    printf("Roll Number: %d\nName: %s\nCGPA: %.2f\n", stud.rollno, stud.name, stud.cgpa);
    fclose(fp1);
}

void search()
{
    FILE *fp2;
    int r, s, avl;
    printf("Enter the Roll no you want to search: ");
    scanf("%d", &r);
    fp2 = fopen("Record", "r");
    while (fread(&stud, sizeof(stud), 1, fp2))
    {
        s = stud.rollno;
        if (s == r)
        {
            printf("Roll no= %d", stud.rollno);
            printf("\nName= %s", stud.name);
            printf("\nCGPA= %.2f\n", stud.cgpa);
        }
        fclose(fp2);
    }
}

void deletefile()
{
    FILE *fpo;
    FILE *fpt;
    int r, s;
    printf("Enter the Roll no you want to delete: ");
    scanf("%d", &r);
    fpo = fopen("Record", "r");
    fpt = fopen("TempFile", "w");
    while (fread(&stud, sizeof(stud), 1, fpo))
    {
        s = stud.rollno;
        if (s != r)
        fwrite(&stud, sizeof(stud), 1, fpt);
    }
    fclose(fpo);
    fclose(fpt);
    fpo = fopen("Record", "w");
    fpt = fopen("TempFile", "r");
    while (fread(&stud, sizeof(stud), 1, fpt))
    fwrite(&stud, sizeof(stud), 1, fpo);
    fclose(fpo);
    fclose(fpt);
    disp();
}

void update()
{
    int avl;
    FILE *fpt;
    FILE *fpo;
    int s, r, ch;
    printf("Enter roll number to update: ");
    scanf("%d", &r);
    fpo = fopen("Record", "r");
    fpt = fopen("TempFile", "w");
    while (fread(&stud, sizeof(stud), 1, fpo))
    {
        s = stud.rollno;
        if (s != r)
        fwrite(&stud, sizeof(stud), 1, fpt);
        else
        {
            printf("1. Update Name of Roll Number %d", r);
            printf("\n2. Update CGPA of Roll Number %d", r);
            printf("\n3. Update both Name and CGPA of Roll Number %d", r);
            printf("\nEnter your choice: ");
            scanf("%d", &ch);
            switch (ch)
            {
                case 1:
                printf("Enter Name: ");
                scanf("%s", &stud.name);
                break;
                
                case 2:
                printf("Enter CGPA: ");
                scanf("%f", &stud.cgpa);
                break;
                    
                case 3:
                printf("Enter Name: ");
                scanf("%s", &stud.name);
                printf("Enter CGPA: ");
                scanf("%f", &stud.cgpa);
                break;
                    
                default:
                printf("Invalid Selection");
                break;
            }
            fwrite(&stud, sizeof(stud), 1, fpt);
        }
        fclose(fpo);
        fclose(fpt);
        fpo = fopen("Record", "w");
        fpt = fopen("TempFile", "r");
        while (fread(&stud, sizeof(stud), 1, fpt))
        fwrite(&stud, sizeof(stud), 1, fpo);
        fclose(fpo);
        fclose(fpt);
        printf("Updated!\n");
    }
}

void scount()
{
    FILE *fp=fopen("new.dat","r");
    int count=0;
    while(fread(&stud,sizeof(stud),1,fp))
    count++;
    printf("The number of students: %d\n", count);
    fclose(fp);
}

int main()
{
    FILE *fp;
    int ch, rn, c = 1;
    while (1)
    {
        printf("1. Input student\n");
        printf("2. Update details\n");
        printf("3. Search by roll no\n");
        printf("4. Number of students\n");
        printf("5. Delete details\n");
        printf("6. Display\n");
        printf("7. Exit\n");
        printf("Input your choice: ");
        scanf("%d", &ch);
        switch (ch)
        {
            case 1:
            insert();
            break;
            case 2:
            update();
            break;
            case 3:
            search();
            break;
            case 4:
            scount();
            break;
            case 5:
            deletefile();
            break;
            case 6:
            disp();
            break;
            default:
            {
                printf("Invalid choice!");
                exit(0);
            }
        }
    }
    return 0;
}