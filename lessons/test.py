print()
print()
print()












class Error(Exception):
    """Base class for other exceptions."""
    pass

class ValueTooSmallError(Error):
    """Raised when the value of the input is too small."""
    pass

class ValueTooLargeError(Error):
    """Raised when the value of the input is too large."""
    pass

def get_integer(prompt):
    """Prompt user for input and validate it as an integer."""
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

def validate_guess(guess, target):
    """Validate the user's guess against the target number."""
    if guess < target:
        raise ValueTooSmallError("The value is too small. Try again.")
    elif guess > target:
        raise ValueTooLargeError("The value is too large. Try again.")
    else:
        return guess

def print_results(guess):
    """Print the final result after correct guess."""
    print("--- Results ---")
    print(f"Congratulations! You guessed it correctly. The number was {guess}.")

def main():
    target_number = 10

    while True:
        try:
            user_guess = get_integer("Enter your guess: ")
            validated_guess = validate_guess(user_guess, target_number)
            print_results(validated_guess)
            break
        except ValueTooSmallError as e:
            print(e)
            print()
        except ValueTooLargeError as e:
            print(e)
            print()

    print("\nTHE END!")

if __name__ == "__main__":
    main()






















print()
print()
print()
