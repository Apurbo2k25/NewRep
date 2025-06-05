import random
import time

def number_guessing_game():
    # Show difficulty options
    print("Choose a difficulty level:")
    print("1. Easy (1-50)")
    print("2. Medium (1-100)")
    print("3. Hard (1-500)")
    choice = int(input("Enter your choice: "))
    
    # Set secret number based on choice
    if choice == 1:
        secret_number = random.randint(1, 50)
        print("You Choose Easy level (1 - 50)! ")
    elif choice == 2:
        secret_number = random.randint(1, 100)
        print("You Choose Medium level (1 - 100)! ")
    elif choice == 3:
        secret_number = random.randint(1, 500)
        print("You Choose Hard level (1 - 500)! ")
    else:
        secret_number = random.randint(1, 100)
        print("Invalid choice, defaulting to Medium (1 - 100)")

    attempts = 0
    max_attempts = 10

    # Game instructions
    print("Welcome to the Number Guessing Game!")
    time.sleep(5)
    print("You have 10 attempts to guess the number!")
    time.sleep(5)
    print("Let's start the game.")
    time.sleep(5)
    print(f"I have selected a number based on your level. Can you guess it?")

    # Guessing loop
    while attempts < max_attempts:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1

            if guess < secret_number:
                print("Too low! Try again.")
            elif guess > secret_number:
                print("Too high! Try again.")
            else:
                print(f"Congrats! You guessed it in {attempts} attempts!")
                break
        except ValueError:
            print("Invalid input. Please enter a number.")
        
        if attempts == max_attempts:
            print(f"Sorry, you used all {max_attempts} attempts. The number was {secret_number}.")
            break

def main():
    # Keep playing until user says no
    while True:
        number_guessing_game()
        play_again = input("Play again? (yes/no): ").lower()
        if play_again != "yes":
            time.sleep(1)
            print("Thanks for playing! Goodbye!")
            break
        
# Start program here
if __name__ == "__main__":
    main()
