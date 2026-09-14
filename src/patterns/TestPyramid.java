public class TestPyramid {
    public static void main(String[] args){
        // *
        // * *
        // * * *
        // * * * *
        for(int i=1;i<5;i++){ //outer loop print 4 rows
            for(int j=1;j<=i;j++){ // take care the logic of printing right format
                System.out.print("*");
                System.out.print("\t");
            }
        System.out.println();
        }
    }
}
