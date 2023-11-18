import random

def play_guess_the_number():
    number = random.randint(1, 10)
    attempts = 0
    max_attempts = 5
    correct_guesses = 0

    print("This is a guess the number game.")
    print("You can guess 5 times.")
    print("Guess a number between 1 and 10.")
    print("Good luck!")

    while attempts < max_attempts:
        guess = int(input("Guess the number (between 1 and 10): "))

        if guess == number:
            print("Congratulations! You guessed the right number:", number)
            correct_guesses += 1
            break
        elif guess < number:
            print("Try a higher number.")
        else:
            print("Try a lower number.")

        attempts += 1

    if attempts == max_attempts:
        print("Sorry, you've reached the maximum number of attempts. The correct number was:", number)

    return correct_guesses

def main():
    total_correct_guesses = 0
    play_again = 'yes'

    while play_again.lower() == 'yes':
        total_correct_guesses += play_guess_the_number()
        play_again = input("Do you want to play again? (yes/no): ")

    print(f"Thanks for playing! You guessed the right number {total_correct_guesses} time(s). Goodbye!")

if __name__ == "__main__":
    main()
