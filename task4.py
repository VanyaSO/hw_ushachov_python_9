import random
import datetime

# Guess a number
RANDOM_NUMBER = int(random.uniform(1, 500))

# Get a number to start the game
user_num = int(input("Enter a number: "))
attempts = 1

time_start = datetime.datetime.now()

# Loop until the user guesses the number
while user_num != RANDOM_NUMBER:
    attempts += 1
        
    if user_num == 0 :
        exit()
    elif user_num > 500 or user_num < 0 : 
        print("The number is in the range from 1 to 500")
    elif user_num < RANDOM_NUMBER :
        print(f"The guessed number is greater than {user_num} ")
    elif user_num > RANDOM_NUMBER :
        print(f"The guessed number is less than {user_num} ")
      
    user_num = int(input("Enter again, or end the game by entering 0: "))
    
time_end = datetime.datetime.now()

time_spent = time_end - time_start
    
print(f"- You won, the guessed number was {RANDOM_NUMBER} \n- Guessed in {attempts} attempts \n- It took {round(time_spent.total_seconds())} seconds")


        
    
