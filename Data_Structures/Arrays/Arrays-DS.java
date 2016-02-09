import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution {

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int n = in.nextInt();
        int arr[] = new int[n];
        for(int arr_i=0; arr_i < n; arr_i++){
            arr[arr_i] = in.nextInt();
        }
        // swap values of array at both ends until midpoint reached
        for(int i=0; i<n/2; i++) {
            int temp = arr[n-i-1]; 
            arr[n-i-1] = arr[i];
            arr[i] = temp;      
        }
        //need to format array string from [1, 2, 3, 4] to: 1 2 3 4
        String reversedArray = Arrays.toString(arr).replace("[","").replace(",","").replace("]","").trim();
        System.out.println(reversedArray);
    }
}
