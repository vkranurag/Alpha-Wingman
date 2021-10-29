import java.util.Scanner;


public class test {

    public static void main(String[] args) {
        
        Scanner scan = new Scanner(System.in);
        System.out.print("Enter any number: ");

        int num = scan.nextInt();

        scan.close();

        for(int i = 1; i < num; i++) 
        {
            if (i % 2 == 0) 
            {
                System.out.println(i);
            }
        }
    }
    
}
