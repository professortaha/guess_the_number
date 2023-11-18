import random

def play_guess_the_number():
    number = random.randint(1, 10)
    max_attempts = 5

    print("Welcome to the Guess the Number game!")
    print(f"You have {max_attempts} attempts to guess a number between 1 and 10. Good luck!")

    for attempts in range(max_attempts):
        guess = int(input("Enter your guess: "))

        if guess == number:
            print(f"Congratulations! You guessed the right number: {number}")
            return 1

        elif guess < number:
            print("Try a higher number.")
        else:
            print("Try a lower number.")

    print(f"Sorry, you've reached the maximum number of attempts. The correct number was: {number}")
    return 0

def main():
    total_correct_guesses = 0

    while True:
        total_correct_guesses += play_guess_the_number()

        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            break

    print(f"Thanks for playing! You guessed the right number {total_correct_guesses} time(s). Goodbye!")

if __name__ == "__main__":
    main()
