import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution {

    public static void main(String[] args) {
        /* Enter your code here. Read input from STDIN. Print output to STDOUT. Your class should be named Solution. */
        Scanner sc = new Scanner(System.in);
        int t = sc.nextInt();
        for(int i=0;i<t;i++) {
            int a = sc.nextInt();
            int b = sc.nextInt();
            int n = sc.nextInt();          

            int sum = a;
            for(int j=0;j<n;j++) {             
                sum+=Math.pow(2,j)*b;
                System.out.print(sum + " ");
            }
            System.out.println();
        }
        
    }
}