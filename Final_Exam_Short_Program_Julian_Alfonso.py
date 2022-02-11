#Final Program - Short
#import random to bring out the random functions
import random
#Defining the main function
def main():
#Opening the output file in write mode
    outfile = open('outfile.txt','w')
#Input to as the user how many times that they want to roll the pair of dice
    num_of_rolls = int(input('Input how many times that would you like to roll the pair of dice:'))
#for statment for how many times the dice will be thrown   
    for x in range(num_of_rolls):
#Assigning Dice_roll to the roll_dices function        
        Dice_roll = roll_dices()
#Calling the win_lost function        
        win_lost(num_of_rolls,Dice_roll,outfile)
#Closing the outfile
    outfile.close
#Creating the roll_dices function  
def roll_dices():
# Randomizing six sides dice    
    Dice_1 = random.randint(1,6)
    Dice_2 = random.randint(1,6)
#Finding the sum of the two dice roll    
    Dice_roll = Dice_1 + Dice_2
#Returning the variable Dice_roll    
    return Dice_roll
#Defining the win_lost function    
def win_lost(num_of_rolls,Dice_roll,outfile):
# if statement to calcutlate if you lose    
    if Dice_roll == 2 or Dice_roll == 3 or Dice_roll == 12:
        lost = Dice_roll
#Writing to the output file        
        outfile.write('You rolled ')
        outfile.write(str(Dice_roll))
        outfile.write('. You Lost' + '\n')
#Retunring the variable lost
        return lost
# elif statement to calcutlate if you won    
    elif Dice_roll == 7 or Dice_roll == 11:
        win = Dice_roll
#Writing to the output file           
        outfile.write('You rolled ')
        outfile.write(str(win))
        outfile.write('. You Win' + '\n')
#Retunring the variable win
        return win
# else statement to calcutlate how many points you earned        
    else:
        point = Dice_roll
#Writing to the output file         
        outfile.write('You earned ')
        outfile.write(str(point))
        outfile.write(' points' + '\n')
#Returning the variable point
        return point
#calling main        
main()
#End of Program
