
public class Driver {

	public static void main(String[] args) throws Exception {
        payable a[ ]=new payable[2];
        a[0] = new Invoice("1","First",5,10000);
        a[1]= new SalariedEmployee("Aya","Razeem","1800567",2000);

        System.out.println("Invoices");
        System.out.println(a[0].display());
        System.out.println("\nSalaried Employees");
        System.out.println(a[1].display());

	}

}
