import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution {

    public static void main(String[] args) {
        /* Enter your code here. Read input from STDIN. Print output to STDOUT. Your class should be named Solution. */
        Scanner sc = new Scanner(System.in);
        String sentence = sc.nextLine();
        int k = sc.nextInt();
        String maxSub="";
        String minSub="";
        
        for(int i=0;i<=sentence.length()-k;i++) {
            String word = sentence.substring(i,i+k);
            //System.out.println(word);
            if(maxSub.length()==0) {
                maxSub = word;
                minSub = word;
            } else {
                if(word.compareTo(maxSub)>=0) {
                maxSub = word;
                }
                if(word.compareTo(minSub)<0) {
                    minSub = word;
                }
            }
            
        }
        System.out.println(minSub);
        System.out.println(maxSub);
    }
}