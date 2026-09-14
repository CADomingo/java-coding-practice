public class PrintMultiplication {
    public static void main(String[] args){
        int result = multiply(5,10);
        System.out.println(result);
    } 
    public static int multiply(int i, int j){
        // i has to sum itself j times to get the results
        int k=1;
        int sum=0;
        while(k<=j){
            sum = sum + i;
            k++;
        }
        return sum;
    }
}