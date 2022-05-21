import java.util.*;
public class loan_1{                                                       //classes + objects + pop= oop
    double y,amt;
    void loan(int a){
        Scanner in =new Scanner(System.in);
        double r=8.31;
        System.out.println("Enter amt,y");                                            //banks having a fixed rate
        amt=in.nextDouble();
        y=in.nextDouble();
        System.out.println("Interest over "+y+" years="+y*(amt*r)/100);
    }
    void loan(int a, int b){             //by lender                         //this is another cool feature of oop: function overlading
                                                                            //ob.loan() has been used twice with the same name but different 
         Scanner in =new Scanner(System.in);                                 //arguments
        double r_lender;
        System.out.println("Enter amt,y,r_lender");
        amt=in.nextDouble();                                        //r_lender: rate decided by lender
        y=in.nextDouble();
        r_lender=in.nextDouble();
        System.out.println("Interest over "+y+" years="+y*(amt*r_lender)/100);
    }
    
    loan_1(int x,int z){                                                               //constructor
        y=x;
        amt=z;
    }
    
    public static void main(String args[]){
        Scanner in =new Scanner(System.in);
        loan_1 ob=new loan_1(0,0);
        String str;
        int w=2;
        while(w!=1){
          System.out.println("Bank_loan(B) or Lender(L)");
          str=in.next();
          if(str.compareTo("B")==0){
            ob.loan(1);
            w=1;
          }
          else if(str.compareTo("L")==0){
            ob.loan(1,2);
            w=1;
          }
          else {
              w=3;
          }
          }
        }
    }