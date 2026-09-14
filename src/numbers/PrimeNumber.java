public class PrimeNumber {
    public static void main(String[] args){
        boolean flag = false;
        int val=31;
        for(int i=2;i<=val/2;i++){
            if(val%i==0){
                flag = true;
                break;
            }
        }
        if(flag)
        System.out.println("it is not prime");
        else
        System.out.println("it is prime");
    }
}
