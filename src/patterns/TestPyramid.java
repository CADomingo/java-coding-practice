public class TestPyramid {

    public static void main(String[] args) {

        // Print Pyramid Pattern
        //
        // *
        // * *
        // * * *
        // * * * *

        for (int i = 1; i <= 4; i++) { // Outer loop prints 4 rows

            for (int j = 1; j <= i; j++) { // Inner loop prints stars

                System.out.print("*");
                System.out.print("\t");
            }

            System.out.println();
        }
    }
}