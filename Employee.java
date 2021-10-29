
public abstract class Employee implements payable{
    private String firstName;
    private String lastName;
    private String socialSecurityNumber;    
    public Employee(String firstName,String lastName,String socialSecurityNumber)
    {
        this.firstName=firstName;
        this.lastName=lastName;
        this.socialSecurityNumber=socialSecurityNumber;
    }

    public String display()
    {
        return "First Name : "+firstName+"\nLast Name : "+lastName+"\nSocial Security No : "+socialSecurityNumber;
    }
}