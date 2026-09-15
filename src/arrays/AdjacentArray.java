public class AdjacentArray {

    public static void main(String[] args) {

        // Find maximum absolute difference between adjacent elements

        int[] a = {1, 4, 8, 15, 17};

        int maxDiff = 0;

        for (int i = 0; i < a.length - 1; i++) {

            int currentDiff = Math.abs(a[i + 1] - a[i]);

            if (currentDiff > maxDiff) {
                maxDiff = currentDiff;
            }
        }

        System.out.println(
            "Maximum difference between adjacent elements is: " + maxDiff
        );
    }
}