import java.util.Scanner;

abstract class Marks {
	abstract double getPercentage();
}

class A extends Marks{
	private float s1, s2, s3;
	  
    public A(float sub1, float sub2, float sub3) {
        s1 = sub1;
    	s2 = sub2;
    	s3 = sub3;
    }
    double getPercentage() {
    	return (s1 + s2 + s3)/300.0 * 100;
    }

}

class B extends Marks {
	private float s1, s2, s3, s4;
	
    public B(float sub1, float sub2, float sub3, float sub4) {
        s1 = sub1;
    	s2 = sub2;
    	s3 = sub3;
    	s4 = sub4;
    }
    double getPercentage() {
    	return (s1 + s2 + s3 +s4)/400.0 * 100;
    }
}

public class Marks_Sub{
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		System.out.println("Enter the 3 marks of Student A: ");
		int m1 = sc.nextInt();
		int m2 = sc.nextInt();
		int m3 = sc.nextInt();
		A a = new A(m1,m2,m3);     
		System.out.println("Enter the 4 marks of Student B: ");
		int m4 = sc.nextInt();
		int m5 = sc.nextInt();
		int m6 = sc.nextInt();
		int m7 = sc.nextInt();
	    B b = new B(m4,m5,m6,m7);  
	    double p1 = a.getPercentage();  
	    double p2 = b.getPercentage();  
	    System.out.println("% mark for student A : " + p1);
	    System.out.println("% mark for student B : " + p2);
	}
}
