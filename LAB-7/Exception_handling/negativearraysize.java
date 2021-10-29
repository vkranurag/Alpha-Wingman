import java.util.Scanner;
public class negativearraysize
{
public static void main(String args[]) throws NegativeArraySizeException
{
    try 
    {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter the Size of the array: ");
        int n = sc.nextInt();
        int arr[]=new int[n];
        System.out.println("Enter elements into array: ");
        for (int i=0; i<n; i++) 
        {
            arr[i] = sc.nextInt();
        }

        System.out.println("Array elements are: ");
        for (int i=0; i<n; i++)
        {
            System.out.print(arr[i] + " ");
        }
    }
    catch (NegativeArraySizeException e) 
    {
        System.out.print("Array cannot be intialised to negative values.");
    }
}
}