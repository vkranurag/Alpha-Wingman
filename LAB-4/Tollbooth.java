import java.util.Scanner;
public class Tollbooth {

    
    static int totalVehicles;
    static int totalAmount;
    static int totalAmountWithoutToll;
    static int lossofamount;

    static int totalHeavyVehicles;
    static int totalAmountHeavyVehicles;
    static int totalheavyvehiclesWithoutToll;
    

    static int totalMediumVehicles;
    static int totalAmountMediumVehicles;
    static int totalmediumVehiclesWithoutToll;

    static int totalTwoWheelers;
    static int totalAmountTwoWheelers;
    static int totaltwoWheelersWithoutToll;

    
    
    public static void main(String[] args) {
        
        Scanner sc = new Scanner(System.in);
        
        System.out.print("Enter the number of vehicles: ");
        int n = sc.nextInt();

        
        
        for(int i=0;i<n;i++) {
            
            System.out.print("\nEnter the vehicle type (Heavy/Medium/Two) ");
            System.out.print("\nType your Choice: ");
            String vehicleType = sc.next();
            
            System.out.print("Enter the vehicle amount (50 for Heavy ,20 for Medium, 10 for two wheelers and Rs0 if not paying) ");
            System.out.print("\nType your Choice: ");
            int vehicleAmount = sc.nextInt();
            
            if(vehicleAmount == 0)
            {

                if(vehicleType.equals("Heavy"))
                totalheavyvehiclesWithoutToll++;

                else if(vehicleType.equals("Medium"))
                totalmediumVehiclesWithoutToll++;

                else if(vehicleType.equals("Two"))
                totaltwoWheelersWithoutToll++;
            }

            
            if(vehicleType.equals("Heavy")) {
                
                totalHeavyVehicles++;
                totalAmountHeavyVehicles = totalAmountHeavyVehicles + vehicleAmount;
                
            }
            
            else if(vehicleType.equals("Medium")) 
            {
                    
                totalMediumVehicles++;
                totalAmountMediumVehicles = totalAmountMediumVehicles + vehicleAmount;

                    
            }
                
            else if(vehicleType.equals("Two")) 
            {
                    
                totalTwoWheelers++;
                totalAmountTwoWheelers = totalAmountTwoWheelers + vehicleAmount;

            }
                
                totalVehicles++;
                totalAmount = totalAmount + vehicleAmount;

                lossofamount = (totalHeavyVehicles * 50 + totalMediumVehicles * 20 + totalTwoWheelers * 10) - totalAmount;
                
            }


            
            System.out.println("\nTotal Vehicles: "+totalVehicles);
            System.out.println("Total Amount: "+totalAmount);

            System.out.println("Total Heavy Vehicles: "+totalHeavyVehicles);
            System.out.println("Total Amount of Heavy Vehicles: "+totalAmountHeavyVehicles);
            System.out.println("Total Number of Heavy Vehicle without paying toll: "+totalheavyvehiclesWithoutToll);

            System.out.println("Total Medium Vehicles: "+totalMediumVehicles);
            System.out.println("Total Amount of Medium Vehicles: "+totalAmountMediumVehicles);
            System.out.println("Total number of Medium vehicle without paying toll: "+totalmediumVehiclesWithoutToll);

            System.out.println("Total Two Wheelers: "+totalTwoWheelers);
            System.out.println("Total Amount of Two Wheelers: "+totalAmountTwoWheelers);
            System.out.println("Total number of Two wheeler without paying toll: "+totaltwoWheelersWithoutToll);

            System.out.print("The lose of amount on that day: "+lossofamount);
            
    }
        
}   