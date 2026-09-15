public class SumofElements {

    public static void main(String[] args) {

        int[] a = {1, 2, 3, 4, 5};

        int sum = sumArray(a);

        System.out.println("Sum of all elements in the array is: " + sum);
    }

    public static int sumArray(int[] a) {

        int sum = 0;

        // Extract every value of array and add each value to sum

        for (int i = 0; i < a.length; i++) {

            sum = sum + a[i];
        }

        return sum;
    }
}