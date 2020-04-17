import java.util.*;
import java.io.*;

class Node {
    Node left;
    Node right;
    int data;
    
    Node(int data) {
        this.data = data;
        left = null;
        right = null;
    }
}

class Solution {

	
    /*class Node 
    	int data;
    	Node left;
    	Node right;
    */
	public static int height(Node root) {
          // Write your code here.
        
       
        if(root.right != null && root.left != null){
        return Math.max(1+height(root.right),height(root.left));
        }if(root.left != null){
           return height(root.left) + 1; 
        }else if(root.right != null){
           return height(root.right) +1; 
        }   else{
            return 0;
        }   

        
    }

    

	public static Node insert(Node root, int data) {