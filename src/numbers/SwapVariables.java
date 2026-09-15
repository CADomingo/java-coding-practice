public class SwapVariables {

    public static void main(String[] args) {

        // Method 1: Using a temporary variable
        // Basket A: Apple → Empty → Orange
        // Basket B: Orange → Empty → Apple
        // Basket C: Empty → Apple → Empty

        int a = 4;
        int b = 6;
        int temp;

        temp = a;
        a = b;
        b = temp;

        System.out.println("Value of a after swapping: " + a);
        System.out.println("Value of b after swapping: " + b);

        // Method 2: Without using a temporary variable

        int c = 5;
        int d = 4;

        c = c + d; // c = 9
        d = c - d; // d = 5
        c = c - d; // c = 4

        System.out.println("Value of c after swapping: " + c);
        System.out.println("Value of d after swapping: " + d);
    }
}