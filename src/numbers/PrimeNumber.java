public class PrimeNumber {

    public static void main(String[] args) {

        boolean flag = false;

        int val = 31;

        for (int i = 2; i <= val / 2; i++) {

            if (val % i == 0) {

                flag = true;
                break;
            }
        }

        if (flag) {
            System.out.println("The number " + val + " is not a prime number");
        } else {
            System.out.println("The number " + val + " is a prime number");
        }
    }
}