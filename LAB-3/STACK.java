import java.util.Scanner;

public class STACK{
        
    private int[] deck;
    private int top;
    
    public STACK() {
        deck = new int[10];
        top = -1;
    }
    
    public void INSERT(int element) {
        if(top == deck.length-1) {
            System.out.println("Stack Overflow");
            return;
        }
        top++;
        deck[top] = element;
    }
    
    public void DISPLAYDECK() {
        for(int i = 0; i <= top; i++) {
            System.out.print(deck[i] + " ");
        }
        System.out.println();
    }
    
    public void DELETE() {
        if(top == -1) {
            System.out.println("Stack Underflow");
            return;
        }
        top--;
    }
    
    public int PEEK() {
        if(top == -1) {
            System.out.println("Stack Underflow");
            return -1;
        }
        return deck[top];
    }
    
    public static void main(String[] args) {
        STACK stack = new STACK();
        Scanner scanner = new Scanner(System.in);
        stack.INSERT(20);
        stack.INSERT(30);
        stack.INSERT(40);
        stack.INSERT(50);
        stack.INSERT(60);
        
        System.out.println("\nOrginal Stack: ");
        stack.DISPLAYDECK();
        
        while(true)
        {
            System.out.println("\n1. Insert");
            System.out.println("2. Display");
            System.out.println("3. Peek");
            System.out.println("4. Delete");
            System.out.println("5. Exit");

            System.out.print("\nEnter your choice: ");
            int ch = scanner.nextInt();

            switch(ch)
            {
                case 1: 
                    System.out.print("\nEnter the Number to Insert into the deck: ");
                    int ele;
                    ele = scanner.nextInt();
                    stack.INSERT(ele);
                    System.out.println(ele + " is pushed into the deck.");
                    break;

                case 2: 
                    System.out.println("\nCurrent deck Status: ");
                    stack.DISPLAYDECK();
                    break;

                case 3: 
                    System.out.println("\nPeek element of the deck: " + stack.PEEK());
                    break;

                case 4: 
                    int last_num;
                    last_num = stack.PEEK();
                    stack.DELETE();
                    System.out.println("\n" + last_num + " is popped from the deck.");
                    break;

                case 5:
                    System.out.println("Exiting!");
                    System.exit(0);

                default:
                    System.out.println("Invalid choice!");
                    break;

            }
        }

    }
}