import java.util.Scanner;

class Person {
    private String name;
    private int age;

    public Person(String name, int age) {
        this.name = name;
        this.age = age;
    }

    public String getName() {
        return name;
    }

    public int getAge() {
        return age;
    }

    public void setName(String name) {
        this.name = name;
    }

    public void setAge(int age) {
        this.age = age;
    }

    public String toString() {
        return "Name: " + name + "\nAge: " + age;
    }
}

class Employee extends Person {
    private int emId;
    private double hourlyPay;

    public Employee(String name, int age, int emId, double hourlyPay) {
        super(name, age);
        this.emId = emId;
        this.hourlyPay = hourlyPay;
    }

    public int getId() {
        return emId;
    }

    public double getHourlyPay() {
        return hourlyPay;
    }

    public void setId(int emId) {
        this.emId = emId;
    }

    public void setHourlyPay(double hourlyPay) {
        this.hourlyPay = hourlyPay;
    }

    public double getRaise() {
        hourlyPay += hourlyPay * 0.15;
        return hourlyPay;
    }

    public void payday(int hours) {
        if (hours >= 40) {
            hourlyPay = 40 * hourlyPay + ((hourlyPay - 40) * 1.5);
        } else {
            hourlyPay = hourlyPay * hours;
        }

        System.out.println("Pay:" + hourlyPay);
    }

    public String toString() {
        return super.toString() + "\nEmployee ID: " + emId + "\nHourly Pay: " + hourlyPay;
    }
}

public class PersonEmployee {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter no of employees: ");
        int n = sc.nextInt();
        for (int i = 0; i < n; i++) 
        {
            System.out.print("Enter name: ");
            String name = sc.next();
            System.out.print("Enter age: ");
            int age = sc.nextInt();
            System.out.print("Enter employee ID: ");
            int emId = sc.nextInt();
            System.out.print("Enter hourly pay: ");
            double hourlyPay = sc.nextDouble();
            Employee e = new Employee(name, age, emId, hourlyPay);
            System.out.println("Raise: " + e.getRaise());

            System.out.println("\n---Info---");
            System.out.println("Id:" + e.getId());
            System.out.println("Hourly Pay:" + e.getHourlyPay());
            System.out.println("After Raise 15%:" + e.getRaise());
            System.out.print("No of hours worked:");
            int hours = sc.nextInt();
            e.payday(hours);

            System.out.println("\n\nFinal Info:");
            System.out.println(e.toString());
            System.out.println("----------------\n");
        }

    }
}
