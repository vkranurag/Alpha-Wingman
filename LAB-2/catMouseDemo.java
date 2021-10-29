import java.util.Scanner;
class Animal {
    public void catAndMouse(int catA, int catB, int mouse) {
        int d1=Math.abs(catA-mouse);
        int d2=Math.abs(catB-mouse);

        if(d1>d2)
        {
        System.out.println("Cat B");
        }
        else if(d1<d2)
        {
        System.out.println("Cat A");
        }
        else
        {
        System.out.println("Mouse C");
        }
    }
}

public class catMouseDemo {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter the Position of Cat A: ");
        int catA = sc.nextInt();
        System.out.println("Enter the Position of Cat B: ");
        int catB = sc.nextInt();
        System.out.println("Enter the Position of Mouse: ");
        int mouse = sc.nextInt();
        sc.close();
        Animal obj = new Animal();
        obj.catAndMouse(catA, catB, mouse);
    }
}