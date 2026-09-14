public class SumofElements{
    public static void main(String[] args){
        int[] a = {1,2,3,4,5};
        int sum = sumArray(a);
        System.out.println(sum);
    }
    public static int sumArray(int[] a){
        int sum =0;
        //extract every value of array and sum each value with other
        for(int i=0;i<a.length;i++){
            sum = sum + a[i];
        }
        return sum;
    }
}