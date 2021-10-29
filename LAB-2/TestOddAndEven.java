import java.util.Scanner;

class OddAndEven {
    private int countOfOdd;
    private int countOfEven;
    
    public OddAndEven() {
        countOfOdd = 0;
        countOfEven = 0;
    }

    public void addNumber(int number) {
        if (number % 2 == 0) {
            countOfEven++;
        } else {
            countOfOdd++;
        }
    }

    public String toString() {
        return "Number of Odd: " + countOfOdd + ", Number of Even: " + countOfEven;
    }
}

public class TestOddAndEven {
    public static void main(String[] args) {
        OddAndEven oddAndEven = new OddAndEven();
        Scanner scanner = new Scanner(System.in);
        System.out.println("Enter a number or Q to quit: ");
        String input = scanner.nextLine();
        while (!input.equals("Q")) {
            oddAndEven.addNumber(Integer.parseInt(input));
            System.out.println("Enter a number or Q to quit: ");
            input = scanner.nextLine();
        }
        System.out.println(oddAndEven.toString());
        scanner.close();
    }
}