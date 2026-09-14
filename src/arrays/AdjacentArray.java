public class AdjacentArray {
    public static void main(String[] args){
        //Max difference between any adjacent index in an array
        int[] a = {1,4,8,15,17};
        int diff = 0;
        for(int i=0;i<a.length-1;i++){
            if(a[i+1]-a[i]>diff){
                diff=a[i+1]-a[i];
            }
            }
        System.out.println(diff);
    }
}