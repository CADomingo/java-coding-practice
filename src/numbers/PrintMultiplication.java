public class PrintMultiplication {

    public static void main(String[] args) {

        int result = multiply(5, 10);

        System.out.println("Multiplication result of 5 and 10 is: " + result);
    }

    public static int multiply(int i, int j) {

        // Add i to itself j times to get the multiplication result

        int k = 1;
        int sum = 0;

        while (k <= j) {

            sum = sum + i;
            k++;
        }

        return sum;
    }
}