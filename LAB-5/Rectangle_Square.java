import java.util.Scanner;
    
    class Rectangle
    {
        int length, breadth;
        Rectangle(int l, int b)
        {
            length = l;
            breadth = b;
        }
        void area()
        {
            System.out.println("Area of Rectangle is: " + length * breadth);
        }
        void perimeter()
        {
            System.out.println("Perimeter of Rectangle is: " + 2 * (length + breadth));
        }
    }
    class Square extends Rectangle
    {
        Square(int s)
        {
            super(s,s);
        }
        void area()
        {
            System.out.println("Area of Square is: " + length * breadth);
        }
        void perimeter()
        {
            System.out.println("Perimeter of Square is: " + 4 * length);
        }
    }
    class Rectangle_Square
    {
        public static void main(String[] args)
        {
            Scanner sc = new Scanner(System.in);
            System.out.println("Enter the length and breadth of the Rectangle: ");
            int l = sc.nextInt();
            int b = sc.nextInt();
            Rectangle r = new Rectangle(l,b);
            r.area();
            r.perimeter();
            System.out.println("Enter the side of the Square: ");
            int s = sc.nextInt();
            Square sq = new Square(s);
            sq.area();
            sq.perimeter();
        }
    }