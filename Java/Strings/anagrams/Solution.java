import java.io.*;
import java.util.*;

public class Solution {

   static boolean isAnagram(String A, String B) {
      //Complete the function

    Map<Character, Integer> charMapA = new HashMap<Character, Integer>();
    Map<Character, Integer> charMapB = new HashMap<Character, Integer>();
    int lenA = A.length();
    int lenB = B.length();
    if(lenA!=lenB) return false;
       
    for(int i=0; i<lenA;i++) {
        char a = Character.toLowerCase(A.charAt(i));
        if(charMapA.get(a)==null) {
            charMapA.put(a,1);
        } else {
            charMapA.put(a,charMapA.get(a)+1);
        }
        
        char b = Character.toLowerCase(B.charAt(i));
        if(charMapB.get(b)==null) {
            charMapB.put(b,1);
        } else {
            charMapB.put(b,charMapB.get(b)+1);
        }
    }
    for (Map.Entry<Character, Integer> entry : charMapA.entrySet()) {
        if(entry.getValue()!=charMapB.get(entry.getKey())) {
            return false;
        }
    }
    return true;
     
   
   }
    public static void main(String[] args) {
        
        Scanner sc=new Scanner(System.in);
        String A=sc.next();
        String B=sc.next();
        boolean ret=isAnagram(A,B);
        if(ret)System.out.println("Anagrams");
        else System.out.println("Not Anagrams");
        
    }
}
