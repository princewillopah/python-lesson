
# try:
#     a = int(input("enter num1: "))
#     b = int(input("enter num2: "))
#     print("{}+{}={}".format(a,b,a+b))
# except TypeError:
#         print("VALUE ERROR FOUND: Please enter valid integers.")
#         # print(str(a)+"+"+str(b)+" = ERROR")
# finally:
#     print("\nTHE END!")
# ------------------------------------
# try:
#     a = int(input("Enter num1: "))
#     b = int(input("Enter num2: "))
#     print("{} + {} = {}".format(a, b, a + b))
# except ValueError as e:
#     print("VALUE ERROR FOUND: Please enter valid integers.")
#     print(f"Error details: {e}")
# finally:
#     print("\nTHIS PROGRAM END!")
## ---------------------------------------------
# try:
#     a = int(input("Enter num1: "))
#     b = int(input("Enter num2: "))
#     print("{} + {} = {}".format(a, b, a + b))
# except ValueError:
#     print("VALUE ERROR FOUND: Please enter valid integers.")
# except TypeError:
#     print("TYPE ERROR FOUND")
# finally:
#     print("\nTHE END!")


### -----------------------------------
# try:
#     a = int(input("Enter num1: "))
#     b = int(input("Enter num2: "))
#     print("{} + {} = {}".format(a, b, a + b))
# except Exception as e:
#     print(f"An error occurred: {e}")
# finally:
#     print("\nTHE END!")




### -----------------------------------
# while True:
#   try:
#     a = int(input("enter num1: "))
#     break
#   except:
#       print("invalid imput")

### -----------------------------------
# while True:
#     try:
#         a = int(input("Enter first integer: "))
#         break
#     except ValueError:
#         print("Invalid input. Please enter a valid integer for first input.")

# while True:
#     try:
#         b = int(input("Enter second integer: "))
#         print()
#         print("--- Results ---")
#         print()
#         print(f"First Number = {a}")
#         print(f"Necond Number = {b}")
#         print(f"{a} + {b} = {a + b}")
#         break
#     except ValueError:
#         print("Invalid input. Please enter a valid integer for second input.")

# print("\nTHE END!")
### ---------------------- improvement ------------------------

# def get_integer(prompt):
#     while True:
#         try:
#             return int(input(prompt))
#         except ValueError:
#             print("Invalid input. Please enter a valid integer.")

# def print_results(a, b):
#     print()
#     print("--- Results ---")
#     print()
#     print(f"First Number = {a}")
#     print(f"Second Number = {b}")
#     print(f"{a} + {b} = {a + b}")

# def main():
#     a = get_integer("Enter first integer: ")
#     b = get_integer("Enter second integer: ")
#     print_results(a, b)
#     print("\nTHE END!")

# if __name__ == "__main__":
#     main()



# ========================


# # define python user-defined exception
# class Error(Exception):
#     """base class for the exception"""
#     pass
# class ValueTooSmallError(Error):
#     """Raised when the value of the imput is too small"""
#
# class ValueTooLargeError(Error):
#     """Raised when the value of the imput is too small"""
#
# number = 10
# while True:
#     try:
#       i_num = int(input("Enter number: "))
#       if i_num < number:
#          raise ValueTooSmallError
#       elif i_num > number:
#         raise ValueTooLargeError
#       break
#     except ValueTooSmallError:
#         print("the value is too small, try again")
#         print()
#     except ValueTooLargeError:
#         print("the value is too LARGE, try again")
#         print()
# print("Congratulation! you guessed it correctly")

# ================ Improve guessing 10=================================

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

