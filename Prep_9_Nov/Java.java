import java.util.Scanner;

public class Java {
    public static void main(String[] args) {
        int sum = 0;
        int count = 0;

        Scanner myObj = new Scanner(System.in);  // Initialize Scanner object outside the loop

        while (count < 5) {
            System.out.println("Enter a number");

            int input = myObj.nextInt();  // Use nextInt() to read an integer input
            sum = sum + input;  // Update the sum with the input value
            count = count + 1;
        }

        System.out.println("The sum is: " + sum);
    }
}
