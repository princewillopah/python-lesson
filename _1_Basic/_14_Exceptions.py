
# try:
#     a = int(input("enter num1: "))
#     b = int(input("enter num2: "))
#     print("{}+{}={}".format(a,b,a+b))
# except ValueError:
#         print("VALUE ERROR FOUND: Please enter valid integers.")
#         print(str(a)+"+"+str(b)+" = ERROR")
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

# main()


# if __name__ == "__main__":
    # main()



# =================================================================

# def get_integer(prompt):
#     while True:
#         try:
#             number = int(input(prompt))
#             return number
#         except ValueError:
#             print("Invalid input. Please enter a valid integer.")

# def add(a, b):
#     return a + b

# def sub(a, b):
#     return a - b

# def mul(a, b):
#     return a * b

# def div(a, b):
#     if b == 0:
#         raise ZeroDivisionError("Cannot divide by zero!")
#     return a / b

# def print_confirmation(a, b):
#     print(f"First Number = {a}")
#     print(f"Second Number = {b}")
#     print()
#     print(""" Select a number below representing the operation you want to perform: 
#         1 = Addition
#         2 = Subtraction
#         3 = Multiplication
#         4 = Division
#      """)
#     user_selection = input("Now Select between 1 and 4: ")

#     if user_selection == '1':
#         return add(a, b), 'Addition'
#     elif user_selection == '2':
#         return sub(a, b), 'Subtraction'
#     elif user_selection == '3':
#         return mul(a, b), 'Multiplication'
#     elif user_selection == '4':
#         if b == 0:  # Ensure division by zero is prevented
#             print("Error: Cannot divide by zero!")
#             return None, 'Invalid Operation'
#         return div(a, b), 'Division'
#     else:
#         print("Invalid operation selected.")
#         return None, 'Invalid Operation'

# def operation(a, b):
#     result = print_confirmation(a, b)
#     print()
#     print("--- Results ---")
#     print()
#     if result[0] is not None:  # If valid operation, print the result
#         print(f"The {result[1]} of {a} and {b} is {result[0]}")
#     else:
#         print("No valid operation performed due to error.\nYou may have wrongly enter a numer that is not 1,2,3 or 4, or you may have entered zero as the second oprand")

# def main():
#     a = get_integer("Enter first integer: ")
#     b = get_integer("Enter second integer: ")  # Do not allow zero here; check inside the operation
#     operation(a, b)
#     print("\nTHE END!")

# main()

# =====================================================================-
# # # define python user-defined exception
# class Error(Exception):
#     """Base class for other exceptions."""
#     pass

# class ValueMustNotBeZero(Error):
#     """Raised when the value of the input is zero"""

# def get_integer(prompt):
#     """Prompt user for input and validate it as an integer."""
#     while True:
#         try:
#             return int(input(prompt))
#         except ValueError:
#             print("Invalid input. Please enter a valid integer.")

# def add(a, b):
#     return a + b

# def sub(a, b):
#     return a - b

# def mul(a, b):
#     return a * b

# def div(a, b):
    
#     return a / b

# def print_confirmation(a, b):
#     print(f"First Number = {a}")
#     print(f"Second Number = {b}")
#     print()
#     print("""Select a number below representing the operation you want to perform: 
# 1 = Addition
# 2 = Subtraction
# 3 = Multiplication
# 4 = Division
#      """)
#     user_selection = input("Now Select between 1 and 4: ")

#     if user_selection == '1':
#         return add(a, b), 'Addition'
#     elif user_selection == '2':
#         return sub(a, b), 'Subtraction'
#     elif user_selection == '3':
#         return mul(a, b), 'Multiplication'
#     elif user_selection == '4':
#         return div(a, b), 'Division'
#     else:
#         print("Invalid operation selected.")
#         return None, 'Invalid Operation'

# def main():
#     a = get_integer("Enter first integer: ")
#     b = get_integer("Enter second integer: ")  # Do not allow zero here; check inside the operation
#     results = print_confirmation(a, b)
#     print(f"{results[1]} of {a} and {b}  = {results[0]}")
#     print("\nTHE END!")


# main()

# def operation(a, b):
#     result = print_confirmation(a, b)
#     print()
#     print("--- Results ---")
#     print()
#     if result[0] is not None:  # If valid operation, print the result
#         print(f"The {result[1]} of {a} and {b} is {result[0]}")
#     else:
#         print("No valid operation performed due to error.\nYou may have wrongly enter a numer that is not 1,2,3 or 4, or you may have entered zero as the second oprand")

# def main():
#     a = get_integer("Enter first integer: ")
#     b = get_integer("Enter second integer: ")  # Do not allow zero here; check inside the operation
#     operation(a, b)
#     print("\nTHE END!")

# main()




# =====================================================================

# # define python user-defined exception
# class Error(Exception):
#     """base class for the exception"""
#     pass
# class ValueTooSmallError(Error):
#     """Raised when the value of the input is too small"""

# class ValueTooLargeError(Error):
#     """Raised when the value of the input is too small"""
# class ValueMustNotBeZero(Error):
#     """Raised when the value of the input is zero"""

# number = 10
# while True:
#     try:
#       i_num = int(input("Enter number: "))
#       if i_num == 0:
#         raise ValueMustNotBeZero
#       elif i_num < number:
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
#     except ValueMustNotBeZero:
#         print("the value is NOT be zero, try again")
#         print()
# print("Congratulation! you guessed it correctly")

# ================ Improve guessing 10=================================

# class Error(Exception):
#     """Base class for other exceptions."""
#     pass

# class ValueTooSmallError(Error):
#     """Raised when the value of the input is too small."""
#     pass

# class ValueTooLargeError(Error):
#     """Raised when the value of the input is too large."""
#     pass

# def get_integer(prompt):
#     """Prompt user for input and validate it as an integer."""
#     while True:
#         try:
#             return int(input(prompt))
#         except ValueError:
#             print("Invalid input. Please enter a valid integer.")

# def validate_guess(guess, target):
#     """Validate the user's guess against the target number."""
#     if guess < target:
#         raise ValueTooSmallError("The value is too small. Try again.")
#     elif guess > target:
#         raise ValueTooLargeError("The value is too large. Try again.")
#     else:
#         return guess

# def print_results(guess):
#     """Print the final result after correct guess."""
#     print("--- Results ---")
#     print(f"Congratulations! You guessed it correctly. The number was {guess}.")

# def main():
#     target_number = 10

#     while True:
#         try:
#             user_guess = get_integer("Enter your guess: ")
#             validated_guess = validate_guess(user_guess, target_number)
#             print_results(validated_guess)
#             break
#         except ValueTooSmallError as e:
#             print(e)
#             print()
#         except ValueTooLargeError as e:
#             print(e)
#             print()

#     print("\nTHE END!")

# if __name__ == "__main__":
#     main()

