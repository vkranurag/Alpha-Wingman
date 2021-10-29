import java.util.Scanner;
public class myException extends Exception{
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter the Weight: ");
        int weight = sc.nextInt();
        try 
        {
            productCheck(weight);
        } 
        catch (myException e) {
            System.out.println("Product invalid");
        }
    }
    public static void productCheck(int weight) throws myException {
        if (weight < 100) {
            throw new myException();
        }

        else
        {
            System.out.println("Product is Valid");
        }
    }
}