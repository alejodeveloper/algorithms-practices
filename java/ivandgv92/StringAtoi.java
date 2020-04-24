public class StringAtoi {
    public int myAtoi(String str) {
        str = str.trim();
        char a;
        int sign=1;
        String result="";

        if(!str.isEmpty() || !str.isBlank()){
            if(str.charAt(0)=='-' || str.charAt(0)=='+') {

                if (str.charAt(0) == '-') {
                    sign = sign * -1;
                }
                str = str.substring(1);
            }
        }else return 0;

        if(str.isBlank() || str.isEmpty())
            return 0;



        for (int i=0;i<str.length();i++){
            a=str.charAt(i);

            if(Character.isDigit(a)){

                result += a;

            }else  if (!Character.isDigit(a) ){
                if(i>0 && Character.isDigit(str.charAt(i-1))){
                    try {
                        return Integer.parseInt(result)*sign;
                    }catch(NumberFormatException e){

                        if(Double.parseDouble(result) >= Integer.MAX_VALUE && sign==-1){
                            return  (Integer.MIN_VALUE)*sign;
                        }else if (Double.parseDouble(result) > Integer.MAX_VALUE && sign==1){
                            return  Integer.MAX_VALUE;
                        }else
                            return 0;
                    }
                }else{
                    return 0;


                }

            }
        }
        try {
            return Integer.parseInt(result)*sign;
        }catch(NumberFormatException e){

            if(Double.parseDouble(result) >= Integer.MAX_VALUE && sign==-1){
                return  (Integer.MIN_VALUE)*sign;
            }else if (Double.parseDouble(result) > Integer.MAX_VALUE && sign==1){
                return  Integer.MAX_VALUE;
            }else
                return 0;
        }



    }

}
