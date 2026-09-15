public class Fibonacci {

    public static void main(String[] args) {

        // Fibonacci Series: 0, 1, 1, 2, 3, 5, 8, 13

        int a = 0;
        int b = 1;
        int sum = 0;
        int i = 1;

        while (i < 9) {

            System.out.println("Fibonacci number: " + a);

            sum = a + b;
            a = b;
            b = sum;

            i++;
        }
    }
}