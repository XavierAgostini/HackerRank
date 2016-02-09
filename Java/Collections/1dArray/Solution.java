import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[] arr = new int[n];
        
        int i = 0;    
        while(sc.hasNextInt()) {
            arr[i] = sc.nextInt();
            i++;
        }
        int negSub = 0;
        for(int j=0;j<n;j++) {
            int sum = 0;        
            for(int k =j;k<n;k++){     
                sum+=arr[k];
                //System.out.println(sum);
                if(sum<0) {
                    negSub+=1;
                }
            }
        }

        System.out.println(negSub);
        //System.out.println(Arrays.toString(arr));

    }
}