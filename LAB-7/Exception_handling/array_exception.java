import java.util.Scanner;
public class array_exception {
    public static void main(String[] args) throws ArrayIndexOutOfBoundsException,NumberFormatException
    {
        int[] arr = {1,2,3,4,5,6,7,8,9,10};
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter the index value: ");
        try 
        {
            int index = Integer.parseInt(sc.next());
            System.out.println("The value at index " + index + " is " + arr[index]);
        }
        catch (ArrayIndexOutOfBoundsException e) {
            System.out.println("The index value is out of bounds");
        }
        catch (NumberFormatException e) {
            System.out.println("The value entered is not a number");
        }
    }
}

