class Solution {
    public int reverse(int x) {
        String reverseNum = new String();
        String reverseNumber = new String();
        int solution;
        
        reverseNum = String.valueOf(Math.abs(x));
        
        for(int i = reverseNum.length() - 1; i >= 0; i--)
            {
               reverseNumber = reverseNumber + reverseNum.charAt(i);
            }
        
        try{
            solution = Integer.parseInt(reverseNumber);
        }catch(NumberFormatException e){
            return 0;
        }
            
       
        if(x<0)
            return solution*-1;
        else
            return solution;
               
    }
}