public class MinMaxNum {

    public static void main(String[] args) {

        // Print Min number and Max number in Multi Dimensional Array

        /*
            2 4 5
            3 4 7
            1 2 9
        */

        int abc[][] = {{2, 4, 5}, {3, 4, 7}, {1, 2, 9}};

        int min = abc[0][0];
        int max = abc[0][0];

        for (int i = 0; i < abc.length; i++) {          // Traverse rows

            for (int j = 0; j < abc[i].length; j++) {   // Traverse columns

                if (abc[i][j] < min) {
                    min = abc[i][j];
                }

                if (abc[i][j] > max) {
                    max = abc[i][j];
                }
            }
        }

        System.out.println("Minimum number: " + min);
        System.out.println("Maximum number: " + max);
    }
}