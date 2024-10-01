# number_guessing.py

import random

def number_guessing_game():
    print("🎲 Welcome to the Number Guessing Game! 🎲")
    print("I'm thinking of a number between 1 and 100.")
    
    # Generate a random number between 1 and 100
    secret_number = random.randint(1, 100)
    
    # Set the number of attempts
    attempts = 5
    print(f"You have {attempts} attempts to guess the number. Good luck! 🤞")

    # Loop until the user runs out of attempts or guesses correctly
    while attempts > 0:
        # Take user input and ensure it's a valid number
        try:
            guess = int(input("Make a guess: "))
        except ValueError:
            print("Invalid input. Please enter a number. ⚠️")
            continue
        
        # Check the guess against the secret number
        if guess < secret_number:
            print("Too low! 📉 Try again.")
        elif guess > secret_number:
            print("Too high! 📈 Try again.")
        else:
            print(f"🎉 Congratulations! You guessed the number {secret_number} correctly! 🎉")
            break  # Exit the loop if the user guesses correctly

        # Decrement the number of attempts
        attempts -= 1
        print(f"You have {attempts} attempts remaining.\n")
    
    # If the user runs out of attempts, reveal the secret number
    if attempts == 0:
        print(f"😞 Sorry, you've run out of attempts. The number was {secret_number}. Better luck next time!")
    
# Run the game
if __name__ == "__main__":
    number_guessing_game()
