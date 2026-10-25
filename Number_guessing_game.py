
# NUMBER GUESSING GAME
import random

secret_number = random.randint(1, 20)

print("Welcome to the Number Guessing Game!")

guess = 0

while secret_number != guess:
    guess = int(input("Guess a number between 1 and 20: "))

    if guess < secret_number:
        print("Too low! Try again.")

    elif guess > secret_number:
        print("Too high! Try again.")
    else:
    	print("You won the game! 🎉")
    	
    	
    	#NUMBER GUESSING GAME
    	import random
    	secret_number=random.randint(1,50)
    	print("welcome to the Number guessing game.")
    	guess=int(input("Enter the secret number: "))
    	if guess==secret_number:
    		print("correct!You won the game🎉")
    	else:
    		print("Try again!!")
    		print("the correct number is: ", secret_number)