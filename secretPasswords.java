

/**
 * The purpose of this program is to generate random passwords with different
 * sets of characters.
 *
 * @author Jimmy Ying
 * @version 07/2/20
 */
import java.util.Scanner;
import java.io.IOException;
import java.io.PrintWriter;
import java.io.File;
import java.util.Random;
class secretPasswords
{
   public static void main (String [ ] args) throws IOException
   {
      Scanner in = new Scanner(System.in);
      System.out.println("Password Generator Menu");
      System.out.println();
      System.out.println("************************************************");
      System.out.println("[1] Lowercase letters");
      System.out.println("[2] Uppercase letters");
      System.out.println("[3] Numbers");
      System.out.println("[4] All letters and numbers");
      System.out.println("[5] Quit");
      System.out.println("************************************************");
      System.out.println();
      
      //simulating
      int trials = 0;
      int pwordlength = 0;
      PrintWriter outFile = new PrintWriter(new File("data.txt"));
      
      while (trials != 5){
          System.out.println("Enter your selection (1-5)");
          trials = in.nextInt();
          
          while (trials > 5){
              System.out.println("Invalid option, please try again.");
              trials = in.nextInt();
            }
            
          System.out.println("Password length (6 or more)");
          
          if (trials != 5){
              pwordlength = in.nextInt();
            }
          else {
              pwordlength = 6;
            }
            
          while (pwordlength < 6){
          System.out.println("Too short, please try again.");
          pwordlength = in.nextInt();
          System.out.println();
        }
        
        String pword = "";
        
        if (trials == 1){
          for (int index=0; index < pwordlength; index++){
            int randNum = 0;
            Random randNumList = new Random();
            while( !(randNum>=97 && randNum<=122))
            {
            randNum = randNumList.nextInt(251);
            }  
            char a = (char)randNum;  
            pword += a;  
            
        } 
      
        }
        else if (trials == 2){
        for (int index=0; index < pwordlength; index++){
            int randNum = 0;
            Random randNumList = new Random();
            while( !(randNum>=65 && randNum<=90))
            {
            randNum = randNumList.nextInt(251);
            }  
            char a = (char)randNum;  
            pword += a;  
            
        } 
        }
        
        else if (trials == 3) {
        for (int index=0; index < pwordlength; index++){
            int randNum = 0;
            Random randNumList = new Random();
            while( !(randNum>=48 && randNum<=57))
            {
            randNum = randNumList.nextInt(251);
            }  
            char a = (char)randNum;  
            pword += a;  
            
        } 
        }
        else if (trials == 4) {
        for (int index=0; index < pwordlength; index++){
            int randNum = 0;
            Random randNumList = new Random();
            while( !((randNum>=97 && randNum<=122) || (randNum>=65 && randNum<=90) || (randNum>=48 && randNum<= 57)))
            {
            randNum = randNumList.nextInt(251);
            }  
            char a = (char)randNum;  
            pword += a;  
            
        } 
        
        }
        outFile.println(pword);
        }
        
        
        
        outFile.close ( );
        
        System.out.println();
        System.out.println("Thank you for using Password Generator.");
        System.out.println();
        System.out.println("Here are your randomly generated passwords:");
        
        File fileName = new File("data.txt");
        Scanner inFile = new Scanner(fileName);
        String pazword = "";
        int counter = 1;
      
      while( inFile.hasNext() )
        {
            pazword = inFile.next();
            System.out.println(counter+".      "+pazword);
            counter++;
        }
        

   }//end of main method
}//end of clas

//PMR
//+ Combination of everything I've learned so far - made me review and look
//back to revisit things such as file reading and random
//- Very tedious, took a long time to fix all errors.