public class driver {

	public static void main(String[] args) throws Exception {
        Payable p[] = new Payable[2];
        
        p[0] = new Invoice("111","abc",2,100);
        p[1] = new SalariedEmployee("John", "Snow", "123", 100);

        System.out.println("Invoices");
        System.out.println(p[0].display());
        System.out.println("\nSalaried Employees");
        System.out.println(p[1].display());
    }
}