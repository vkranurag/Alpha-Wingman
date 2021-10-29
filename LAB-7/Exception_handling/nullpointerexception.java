import java.util.Scanner;
class nullpointerexception
{
    void nothing() 
    {
        System.out.println("This print statement wont print anything");
    }
    public static void main (String[] args) throws NullPointerException
    {
        try
        {
            Scanner sc = new Scanner(System.in);
            nullpointerexception s = new nullpointerexception();
            s = null;
            s.nothing();
        }

        catch(NullPointerException e)
        {
            System.out.println("Cannot invoke a method from a null object");
        }

        finally
        {
            System.out.println("Out of try-catch block");
        }
    }
}
