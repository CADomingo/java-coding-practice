import java.util.ArrayList;

public class CompareArray {

    // Compare same indexes of 2 different arrays
    // and create another array of matching values

    public static void main(String[] args) {

        int a[] = {1, 4, 5, 7};
        int b[] = {6, 4, 3, 7}; // Matching values: {4, 7}

        ArrayList<Integer> al = new ArrayList<Integer>();

        for (int i = 0; i < Math.min(a.length, b.length); i++) {

            if (a[i] == b[i]) {
                // Add matching value to ArrayList
                al.add(a[i]);
            }
        }

        Integer[] c = al.toArray(new Integer[0]);

        for (int value : c) {
            System.out.println("Matching value: " + value);
        }
    }
}