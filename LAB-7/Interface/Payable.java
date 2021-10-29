public interface Payable {
    double getPaymentAmount();
    String display();
}

class Invoice implements Payable{
	private String partNumber;
    private String partDescription;
    private int quantity;
    private double pricePerItem;

    public Invoice(String partNumber, String partDescription, int quantity, double pricePerItem) {
        this.partNumber = partNumber;
        this.partDescription = partDescription;
        this.quantity = quantity;
        this.pricePerItem = pricePerItem;
    }

    public String display() {
        return "Part Number: " + partNumber + "\nPart Description: " + partDescription + "\nQuantity: " + quantity + "\nPrice Per Item: " + pricePerItem;
    }

    public double getPaymentAmount() {
        return quantity * pricePerItem;
    }
}

abstract class Employee implements Payable {
	private String firstName;
    private String lastName;
    private String socialSecurityNumber;
    
    public Employee(String firstName, String lastName, String socialSecurityNumber){
        this.firstName = firstName;
        this.lastName = lastName;
        this.socialSecurityNumber = socialSecurityNumber;
    }

    public String display(){
        return "First Name: " + firstName + "\nLast Name: " + lastName + "\nSocial Security Number: " + socialSecurityNumber;
    }
}

class SalariedEmployee extends Employee{
	private double weeklysalary;
    
    public SalariedEmployee(String first, String last, String ssn, double salary){
        super(first, last, ssn);
        setWeeklySalary(salary);
    }
    
    public void setWeeklySalary(double salary){
        weeklysalary = salary;
    }
    
    public double getWeeklySalary(){
        return weeklysalary;
    }
    
    public double earnings(){
        return getWeeklySalary();
    }
    
    public String display(){
        return super.display() + "\nWeekly Salary: " + getWeeklySalary();
    }

    public double getPaymentAmount(){
        return getWeeklySalary();
    }
}


