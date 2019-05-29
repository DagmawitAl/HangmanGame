import time

#Welcoming the player

print ("Welcome! Time to play hangman!")

#Ask player's name
name = input("What is your name? ")

print ("Hello, " + name, "!")

print ("")

#wait for 1 second
time.sleep(1)

print ("Start guessing...")

#wait for 0.5 second
time.sleep(0.5)

#The answer is happy
word = "happy"

#Set guesses to empty
guesses = ''

#Determine the number of turns
turns = 10

# Create a while loop

#check if the turns are more than zero
while turns > 0:         

    # make a failed counter that starts with zero
    failed = 0             

    # for every letter in word   
    for char in word:      

    # see if the letter is in the player's guess
        if char in guesses:    
    
        # print the letter
            print (char,end="")    

        else:
    
        # if it's not in the player's guess, print a dash
            print ("\n_\n"),     
       
        # increment the failed counter with one
            failed += 1    

    # if failed is equal to zero

    # print You Won
    if failed == 0:        
        print ("\nYou're a winner!!!")  

    # exit the script
        break              

    print

    # Ask the player to guess a letter
    guess = input("\nGuess a letter:") 

    # Assign the players guess to guesses
    guesses += guess                    

    # if the guess is not found in the happy word
    if guess not in word:  
 
     # turns counter decreases with 1
        turns -= 1        
 
    # print incorrect
        print ("Incorrect")    
 
    # print how many turns there are left
        print ("You have", + turns, 'more guesses') 
 
    # if the turns are equal to zero
        if turns == 0:           
    
        # print "Game Over! You Lose."
            print ("Game Over! You Lose.")  
