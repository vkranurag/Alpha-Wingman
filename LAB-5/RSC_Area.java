import java.util.Scanner;
abstract class Shape {
	abstract void RectangleArea(float length , float breadth);
    abstract void SquareArea(float side);
    abstract void CircleArea(float radius);
}

class Area extends Shape {
	double Area;

    void RectangleArea(float length , float breadth){
    Area = length * breadth;
    System.out.println("Area of Rectangle: "+Area);
    }

    void SquareArea(float side){
    Area = side * side;
    System.out.println("Area of Square: "+Area);
    }

    void CircleArea(float radius){
    Area = 3.14*(radius * radius);
    System.out.println("Area of Circle: "+Area);
    }
}

public class RSC_Area {

	public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
		Area area = new Area();
        System.out.println("Enter the length and breadth of Rectangle: ");
        int l = sc.nextInt();
        int b = sc.nextInt();
        
        System.out.println("Enter the side of the Square: ");
        int s = sc.nextInt();

        System.out.println("Enter the radius of the Circle: ");
        int r = sc.nextInt();

        area.RectangleArea(l,b);
        area.SquareArea(s);
        area.CircleArea(r);
	}
}
