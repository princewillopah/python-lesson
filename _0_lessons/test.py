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


# ==============================================
# lesson
# =======================================

# if a  number is divided by 2 and the rememder is 0 
#        that number is a even number
# if a  number is divided by 2 and the rememder is 1 
#        that number is a odd number

# how to get a remainder from a divison
# num%2 
# print(1%2) # 1
# print(2%2) # 0
# print(3%2) # 1
# print(4%2) # 0
# print(5%2) # 1
# print(6%2) # 0
# print(7%2) # 1
# print(8%2) # 0
# print(9%2) # 1
# print(10%2) # 0
# print(11%2) # 1

# num = 1449577484848


# if num % 2 == 0:
#     print(f"{num} is even number")
# elif num % 2 == 1:
#      print(f"{num} is odd number")

#   -97 ... -25  -24    ....   -6  -5 -4  -3   -2  -1 0 1 2 3 4 5 6 7 8 9  10 11 12 13 14 15 16 17 ... 100 ..... 1000000

# print("enter numer")
# num = int(input())

# if num > 0:
#     print(f"{num} is a positive number")
# elif num < 0:
#       print(f"{num} is a negative number")


# vowels = aeiou
# print("enter a letter")
# letter = input()

# if letter == 'a':
#     print(f"{letter} is a vowel")
# elif letter == 'o':
#     print(f"{letter} is a vowel")
# elif letter == 'e':
#     print(f"{letter} is a vowel")
# elif letter == 'i':
#     print(f"{letter} is a vowel")
# elif letter == 'o':
#     print(f"{letter} is a vowel")
# else:
    # print(f"{letter} is NOT a vowel")

# -----------------------------
# print("enter a letter")
# letter = input()

# if letter == 'a' or letter == 'o' or letter == 'e' or letter == 'i' or letter == 'u':
#     print(f"{letter} is a vowel")
# else:
#     print(f"{letter} is NOT a vowel")

# -------------------------

# print("enter a letter")
# letter = input()

# list_of_vowel = "aeiou"

# if letter in list_of_vowel:
#      print(f"{letter} is a vowel")
# else:
#       print(f"{letter} is NOT a vowel")

# ---------------------------
# question 7
# Write an if statement that prints "Number is in range" if number is between 1 and 10 (inclusive).
# number = 7

# print("enter a Number")
# num = int(input())

# if num >= 1 and num <= 10:
#     print(f"{num} is in the range 1 - 10")
# else:
#  print(f"{num} is NOT in the range 1 - 10")




















print()
print()
print()
