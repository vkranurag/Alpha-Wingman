import java.util.Scanner;

class Complex{

    private float real;
    private float imaginary;

    public Complex(int temp_Real, int temp_Imaginary)
    {
        real = temp_Real;
        imaginary = temp_Imaginary;
    }

    public Complex(){
    }

    Complex add(Complex C1, Complex C2)
    {
        Complex Sum = new Complex();

        Sum.real = C1.real + C2.real;
        Sum.imaginary = C1.imaginary + C2.imaginary;

        return Sum;
    }

    Complex sub(Complex C1, Complex C2)
    {
        Complex Sub = new Complex();

        Sub.real = C1.real - C2.real;
        Sub.imaginary = C1.imaginary - C2.imaginary;

        return Sub;
    }

    void printComplexNumber()
    {
        System.out.println("Complex number: "+ real + " + "+ imaginary + "i");
    }

    public static void main(String[] args){

        int a1,a2,b1,b2;
        Scanner scanner = new Scanner(System.in);
        System.out.println("Enter the first complex number");
        a1 = scanner.nextInt();
        b1 = scanner.nextInt();
        Complex C1 = new Complex(a1, b1);
        C1.printComplexNumber();
  
        System.out.println("Enter the second complex number");
        a2 = scanner.nextInt();
        b2 = scanner.nextInt();
        Complex C2 = new Complex(a2, b2);
        C2.printComplexNumber();

        scanner.close();
  
        Complex C3 = new Complex();

        C3 = C3.add(C1, C2);
        System.out.print("\nSum of ");
        C3.printComplexNumber();

        C3 = C3.sub(C1, C2);
        System.out.print("Difference of ");
        C3.printComplexNumber();
    }
}


