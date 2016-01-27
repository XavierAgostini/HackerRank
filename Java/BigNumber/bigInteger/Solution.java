import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution {

    public static void main(String[] args) {
     	Scanner sc = new Scanner(System.in);
        BigInteger x,y;
        x = new BigInteger(sc.nextLine());
        y = new BigInteger(sc.nextLine());
        System.out.println(x.add(y));
        System.out.println(x.multiply(y));
    }
}