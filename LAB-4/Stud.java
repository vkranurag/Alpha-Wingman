import java.util.Scanner;

public class Stud {

    private int rollno;
    private String name;
    private int marks[] = new int[3];
    private char grade;

    char calgrade() {

        int sum = 0;
        for (int i = 0; i < 3; i++) 
        {
            sum += marks[i];
        }

        float avg = sum/3;

        if (avg >= 90) 
        {
            return 'A';
        } 
        else if (avg >= 80) 
        {
            return 'B';
        }
        else if (avg >= 70) 
        {
            return 'C';
        } 
        else if (avg >= 60) 
        {
            return 'D';
        } 
        else 
        {
            return 'F';
        }
    }

    public int getrollno()
    {
        return rollno;
    }

    public static Stud[] sort(Stud[] stud,int n){

        Stud temp;
        for (int i = 0; i < n; i++) {
            for (int j = i + 1; j < n; j++) {
                if (stud[i].getrollno() > stud[j].getrollno()) {
                    temp = stud[i];
                    stud[i] = stud[j];
                    stud[j] = temp;
                }
            }
        }
        return stud;
    }
    

    public void setData() {

        Scanner sc = new Scanner(System.in);
        System.out.print("\nEnter the Roll number: ");
        rollno = sc.nextInt();
        System.out.print("Enter the Name: ");
        name = sc.next();
        System.out.println("Enter the Marks: ");
        marks[0] = sc.nextInt();
        marks[1] = sc.nextInt();
        marks[2] = sc.nextInt();
        grade = calgrade();

    }

    public void Display(){

        System.out.println("\nRoll number: "+rollno);
        System.out.println("Name: "+name);
        System.out.println("Marks are "+marks[0]+" "+marks[1]+" "+marks[2]);
        System.out.println("Grade: "+grade);
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter the Number of Students: ");
        int n = sc.nextInt();   
        Stud [] s;
        s = new Stud[n];
        System.out.println("Enter the details of the Student ");
        for(int i=0;i<n;i++)
        {
            s[i]=new Stud();
            s[i].setData();
        }
        System.out.println("Sorted Data (Based on rollno): ");
        s = sort(s,n);
        for(int i=0;i<n;i++){
            s[i].Display();
        }
        sc.close();
    }

}
