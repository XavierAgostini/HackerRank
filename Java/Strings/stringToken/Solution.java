import java.io.*;
import java.util.*;

public class Solution {

  public static void main(String[] args) {
    Scanner scan = new Scanner(System.in);
    String s=scan.nextLine();//[_\@ !,?.'

    String delims = "[ !,?.\'@_]+";
    if(s.trim().length() > 400000 || s.trim().length() ==0 ) {  
      System.out.println(0);
      return;
    } 
    String[] tokens = s.trim().split(delims);
    System.out.println(tokens.length);
    if(tokens.length!=0) {
      for(int i=0;i<tokens.length;i++) {
        System.out.println(tokens[i]);
      }
    }
  }
}

       
