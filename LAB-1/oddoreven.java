import java.util.Scanner;

class oddoreven{

    public static void main(String[] args) {

        Scanner scan = new Scanner(System.in);
        System.out.print("Enter any number: ");

        int num = scan.nextInt();

        scan.close();

        if (num % 2 == 0) {
  
            System.out.println(num + " is an Even Number!");
        }
        else {
  
            System.out.println(num + " is an Odd Number!");
        }
        
    }
}