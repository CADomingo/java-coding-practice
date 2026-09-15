import java.util.ArrayList;

public class EliminateDuplicate {

    public static void main(String[] args) {

        // Eliminate duplicates and print Unique numbers in the Array

        // My understanding:
        // Start with an empty ArrayList.
        // Pick one number from the array.
        // Check whether that number is already present in the ArrayList.
        // If it is not present, add it to the ArrayList and start counting
        // how many times that number occurs in the remaining array.

        // 4 - 3, 5 - 3, 6 - 2, 9 - 1

        // Expected frequency:
        // 4 -> 3 times
        // 5 -> 3 times
        // 6 -> 2 times
        // 9 -> 1 time
        //
        // Therefore, 9 is the unique number.

        int a[] = {4, 5, 5, 5, 4, 6, 6, 9, 4};

        // Create an empty ArrayList to store numbers that have already
        // been processed. This prevents us from counting the same number again.
        ArrayList<Integer> al = new ArrayList<Integer>();

        // Traverse through every element of the array.
        for (int i = 0; i < a.length; i++) {

            // k is used to count how many times the current number occurs.
            int k = 0;

            // Check whether the current number is already processed.
            // If it is not present, process it.
            if (!al.contains(a[i])) {

                // Add the current number to the ArrayList so that we
                // don't process the same number again.
                al.add(a[i]);

                // Count the current element itself.
                k++;

                // Scan the elements after the current index.
                for (int j = i + 1; j < a.length; j++) {

                    // If the current number matches another number,
                    // increase the count.
                    if (a[i] == a[j]) {
                        k++;
                    }
                }

                // If the number occurred only once, it is unique.
                if (k == 1) {
                    System.out.println(a[i] + " is unique number");
                }
            }
        }
    }
}