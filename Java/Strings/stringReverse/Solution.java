import java.io.*;
import java.util.*;

public class Solution {

    public static void main(String[] args) {
        
        Scanner sc=new Scanner(System.in);
        String A=sc.next();
        boolean isPalindrome = true;
        int len = A.length()-1;
        /* Enter your code here. Print output to STDOUT. */
        for(int i=0; i<len;i++) {       
            //Break at midpoint of sentence
            if(i==len-i) {
                break;
            } else {
                if(A.charAt(i)!=A.charAt(len-i)) {
                    isPalindrome = false;
                    break;
                }
            }
            
        }
        if(isPalindrome) {
            System.out.println("Yes");
        } else {
            System.out.println("No");
        }
        
    }
}
