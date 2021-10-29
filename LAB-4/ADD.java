import java.util.Scanner;

class Complex
{
    float real;
    float imag;
    Complex()
    {
        real=0;
        imag=0;
    }
    Complex(float real,float imag)
    {
        this.real=real;
        this.imag=imag;
    }
    Complex add(Complex c2)
    {
        Complex c3=new Complex();
        c3.real=real+c2.real;
        c3.imag=imag+c2.imag;
        return c3;
    }

    void display()
    {
        System.out.println(real + "+" + imag + "i");
    }
}

class Vector
{
    float x;
    float y;
    Vector()
    {
        x=0;
        y=0;
    }
    Vector(float x,float y)
    {
        this.x=x;
        this.y=y;
    }
    Vector add(Vector v2)
    {
        Vector v3=new Vector();
        v3.x=x+v2.x;
        v3.y=y+v2.y;
        return v3;
    }

    void display()
    {
        System.out.println("<" + x + "," + y + ">");
    }
}


public class ADD
{
    public static void main(String args[])
    {
        Scanner sc=new Scanner(System.in);
        while(true)
        {
        System.out.println("\nEnter the type of addition");
        System.out.println("1. Floating point addition");
        System.out.println("2. Complex number addition");
        System.out.println("3. Vector addition");
        System.out.println("4. Exit");
        System.out.print("\nEnter your Choice: ");
        int choice=sc.nextInt();
        switch(choice)
        {
            case 1:
                System.out.println("\nEnter the two floating point numbers: ");
                float a=sc.nextFloat();
                float b=sc.nextFloat();
                System.out.println("The sum of the two numbers is "+add(a,b));
                break;
            case 2:
                System.out.println("\nEnter the two complex numbers");
                Complex c1=new Complex();
                Complex c2=new Complex();
                System.out.println("Enter the first complex number");
                c1.real = sc.nextFloat();
                c1.imag = sc.nextFloat();

                System.out.println("Enter the second complex number");
                c2.real = sc.nextFloat();
                c2.imag = sc.nextFloat();

                Complex c3 = add(c1,c2);
                System.out.print("The sum of the two complex numbers is ");
                c3.display();
                break;
            case 3:
                System.out.println("\nEnter the two vectors");
                Vector v1=new Vector();
                Vector v2=new Vector();

                System.out.println("Enter the first vector: ");
                v1.x = sc.nextFloat();
                v1.y = sc.nextFloat();
                System.out.println("Enter the second vector: ");
                v2.x = sc.nextFloat();
                v2.y = sc.nextFloat();

                Vector v3 = add(v1,v2);
                System.out.print("The sum of the two vectors is ");
                v3.display();
                break;
            case 4:
                System.exit(0);
            default:
                System.out.println("Invalid choice");
        }
                    
    }
}


    public static float add(float a,float b)
    {
        return a+b;
    }
    public static Complex add(Complex c1,Complex c2)
    {
        return c1.add(c2);
    }
    public static Vector add(Vector v1,Vector v2)
    {
        return v1.add(v2);
    }
}
