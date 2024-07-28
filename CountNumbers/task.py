import random

def number_guessing_game():
    # Computer generates a random number between 1 and 100
    number_to_guess = random.randint(1, 6)
    
    print("Welcome to the Number Guessing Game!")
    print("I have selected a random number between 1 and 100.")
    print("Can you guess what it is?")
    
    while True:
        # Prompt the user to guess the number
        try:
            user_guess = int(input("Enter your guess: "))
        except ValueError:
            print("Invalid input. Please enter an integer.")
            continue
        
        # Check if the user's guess is correct, too high, or too low
        if user_guess < number_to_guess:
            print("Too low! Try again.")
        elif user_guess > number_to_guess:
            print("Too high! Try again.")
            
        else:
            print(f"Congratulations! You've guessed the correct number: {number_to_guess}")
            break

# Run the game
number_guessing_game()
