import os
os.system('cls')
print("----------------------------------------------------------------------------------------")
print(" RESULTS")
print("----------------------------------------------------------------------------------------")
print()
print()











### ========================================================================================
###
### ========================================================================================

### -------- without functions  -----:

# for num in range(1,11):

#     print(f"{num} is {num_is} and its square is {num**2}")

### -------- with functions  ----------

# def numType(num):
#     if num % 2 == 0:
#         num_is = "Even"
#     else:
#         num_is = "Odd"
#     return num_is


# for num in range(1,11):
#     print(f"{num} is {numType(num)} and its square is {pow(num,2)}")


### -------- other variations of the function above  ----------

# def numType(num):
#     if num % 2 == 0:
#         return "Even"
#     return "Odd"

# --------


### ========================================================================================
### python scope
### ========================================================================================
"""
Local Scope:
- Variables defined inside a function belong to the local scope of that function.
- These variables are only accessible within the function and are destroyed after the function finishes execution.
"""
# def my_function1():
#     x = 10  # Local variable
#     print(x)  # Accessible only inside the function

# my_function1()
## print(x) # This would raise an error, as x is not accessible outside the function
## ----------------

"""
Enclosing Scope (Nonlocal Scope)
- In nested functions, the inner function can access variables from the enclosing (outer) function's scope.
- These variables are neither local nor global but exist in the enclosing scope.
"""
# def outer_function():
#     y = 20  # Enclosing variable
#     def inner_function():
#         x = 20
#         print(20+y+x) # Accessible within the inner function
#     inner_function()

# outer_function()

# -------------------------------

"""
Global Scope
- Variables defined at the top level of a script or module are in the global scope.
- These variables can be accessed from anywhere in the module or script unless shadowed by a local variable with the same name.
"""

# z = 30  # Global variable
# def my_function():
#     global z  # accessing the global variable in a local scope
#     z = 40
#     print(z)  # 40
#     z = 45
#     print(z)  # 45

# print(z)  # 30

# my_function()

# print(z)  # 45

# -------------------------
"""
nonlocal: Allows you to modify a variable in the enclosing scope (but not in the global scope).
"""  
# def outer_function():
#     y = 10
#     def inner_function():
#         nonlocal y
#         y = 20  # Modifies the 'y' from the enclosing scope
#     inner_function()
#     print(y)  # Output: 20
# outer_function()








### ========================================================================================
### A Function that Returns Multiple Results
### ========================================================================================

### Method 1: Returning Multiple Results as a Tuple

# def calculate(a, b):
#     sum_result = a + b
#     diff_result = a - b
#     product_result = a * b
#     if b != 0:
#         division_result = a / b
#     else:
#         division_result = None  # Handle division by zero
#     return sum_result, diff_result, product_result, division_result  ### this sill be resurn as (sum_result, diff_result, product_result, division_result)




# results = calculate(10, 5)# Call the function
# print(f"Sum: {results[0]}, Difference: {results[1]}, Product: {results[2]}, Division: {results[3]}")# Access the results

# -----------------------------------------------

### Method 4. Returning Multiple Results Using Multiple Variables    ---- Python allows unpacking of multiple return values into separate variables.

# def calculate_multiple_vars(a, b):
#     sum_result = a + b
#     diff_result = a - b
#     product_result = a * b
#     division_result = a / b if b != 0 else None
#     return sum_result, diff_result, product_result, division_result

# # Call the function and unpack the results
# sum_result, diff_result, product_result, division_result = calculate_multiple_vars(10, 5)

# # Print the unpacked results
# print(f"Sum: {sum_result}, Difference: {diff_result}, Product: {product_result}, Division: {division_result}")

# -----------------------------------------------

### Method 2. Returning Multiple Results as a List  ## If you want the results to be mutable (changeable), return them as a list.
# def calculate_as_list(a, b):
#     sum_result = a + b
#     diff_result = a - b
#     product_result = a * b
#     division_result = a / b if b != 0 else None
#     return [sum_result, diff_result, product_result, division_result]


# results = calculate_as_list(10, 5)  # Call the function
# print(f"Results as List: {results}")  # Access the results
# print(f"Sum: {results[0]}, Difference: {results[1]}, Product: {results[2]}, Division: {results[3]}")

# -----------------------------------------------

### Method 3. Returning Multiple Results as a Dictionary   ----   A dictionary can make the results more readable by associating each result with a key.

# def calculate_as_dict(a, b):
#     return {
#         'sum': a + b,
#         'difference': a - b,
#         'product': a * b,
#         'division': a / b if b != 0 else None
#     }

# # Call the function
# results = calculate_as_dict(10, 5)

# # Access the results
# print(f"Sum: {results['sum']}, Difference: {results['difference']}, Product: {results['product']}, Division: {results['division']}")















### ========================================================================================
###  changing function name
### ========================================================================================
# def original_Calculating_function(a,b):
#     return a+b

# # Change the function name by assigning it to a new name
# new_calculating_function = original_Calculating_function

# # Now you can call the function using the new name
# print(new_calculating_function(4,7))  # Output: This is the original function.

# # and still use the old name
# print(original_Calculating_function(3,9))


### ========================================================================================
###  Argument Type
### ========================================================================================
"""
- Positional Arguments: Passed based on the position.
- Keyword Arguments: Passed with the parameter name explicitly.
- Default Arguments: Uses default values if not provided.
- Variable-Length Arguments:
    *args: Allows passing a variable number of positional arguments.
    **kwargs: Allows passing a variable number of keyword arguments.
- Positional-Only Arguments: Must be passed by position, not by name.
- Keyword-Only Arguments: Must be passed by keyword

"""

### --------------------------------------
### Positional or Required Arguments  -- Passed based on the position.
### --------------------------------------
"""
Positional arguments are the most common type of argument. These are passed to a function in a specific order, and their position matters.
"""
# def greet(name, message):
#     print(f"{message}, {name}!")

# # Calling the function with positional arguments
# greet("Alice", "Hello")  # Output: Hello, Alice!





### --------------------------------------
### Keyword Arguments
### --------------------------------------
"""
Keyword arguments are passed using the name of the parameter (key) rather than its position. 
This makes it clear what each argument is doing.
"""
# def greet(name, message):
#     print(f"{message}, {name}!")

# # Calling the function with keyword arguments - we swapped the position yet the result is as expected
# greet(message="Hello", name="Alice")  # Output: Hello, Alice!




### --------------------------------------
### Default Arguments
### --------------------------------------
""" 
Default arguments are used when you want to provide default values for one or more parameters. 
If no argument is passed for these parameters, the default value is used.
"""
# def greet(name, message="Hello"):
#     print(f"{message}, {name}!")

# # Calling the function without the second argument (uses default)
# greet("Alice")  # Output: Hello, Alice!

# # Calling the function with both arguments
# greet("Bob", "Hi")  # Output: Hi, Bob!

# # greet()  ## this willl throw error since "name" requires an argument 




### --------------------------------------
### Variable-Length Arguments
### --------------------------------------
"""
These allow you to pass an arbitrary number of arguments to a function. There are two types of variable-length arguments:
    a. *args (Non-Keyword Variable-Length Arguments)
    *args allows you to pass any number of positional arguments to a function.

    b. **kwargs (Keyword Variable-Length Arguments)
    **kwargs allows you to pass any number of keyword arguments to a function.

"""
# def add_numbers(*args):
#     result = sum(args)
#     print(f"The sum is {result}")

# # Calling the function with multiple arguments
# add_numbers()           # Output: The sum is 0
# add_numbers(1)          # Output: The sum is 1
# add_numbers(1, 2)       # Output: The sum is 3
# add_numbers(1, 2, 3)    # Output: The sum is 6
 
## ------------

# def greet(**kwargs):
#     for key, value in kwargs.items():
#         print(f"{key}: {value}")

# # Calling the function with multiple keyword arguments
# greet(name="Alice", age=30, city="New York")
# # Output:
# # name: Alice
# # age: 30
# # city: New York




### --------------------------------------
### Positional-Only Arguments (Python 3.8+)
### --------------------------------------
"""
In some cases, you may want to enforce that arguments must be passed positionally (not as keywords). 
You can do this by placing a / in the parameter list.
"""
# def greet(name, /, message="Hello"):
#     print(f"{message}, {name}!")

# # Calling with positional argument works
# greet("Alice")  # Output: Hello, Alice!

# # Calling with keyword argument for `name` would raise an error
# # greet(name="Alice")  # This would raise a TypeError




### --------------------------------------
### Keyword-Only Arguments
### --------------------------------------
"""
To make an argument keyword-only, you can place * before the keyword arguments. 
This means the arguments after * must be passed as keywords.
"""

# def greet(*, name, message="Hello"):
#     print(f"{message}, {name}!")

# # Calling the function with keyword arguments is mandatory for `name`
# greet(name="Alice")  # Output: Hello, Alice!

# # Calling the function without keyword arguments for `name` would raise an error
# # greet("Alice")  # This would raise a TypeError



### --------------------------------------
### how python pass value
### --------------------------------------
# """

# """
# def returnNums(a,b):
#     a = a + 4
#     b = b + 4
#     print(f"num1 = {a} and num2 = {b}")

# def returnStr(my_string):
#     my_string = "Ololade"
#     print(f"Name is {my_string}")

# num1 = 8
# num2 = 4
# name = "Popoola"

# print(f"num1 = {num1} and num2 = {num2}")
# print(f"Name is {name}")
# print()
# returnNums(num1,num2)
# returnStr(name)



### --------------------------------------
### 
### --------------------------------------



### ========================================================================================
### importing function
### ========================================================================================

### --------------------------------------
### import _9a_functions
### --------------------------------------
"""
### this will import everythin in that python file inclusing the lines
"""
# import _9a_functions
# print(f"5 + 4 = {_9a_functions.add(5,4)}")

### --------------------------------------
### import _9a_functions as xx
### --------------------------------------
"""
### using alias for the file name
"""
# import _9a_functions as xx
# print(f"5 + 4 = {xx.add(5,4)}")
# print(f"5 - 4 = {xx.sub(5,4)}")
# print(f"5 x 4 = {xx.mul(5,4)}")

### --------------------------------------
### from  _9a_functions import *
### --------------------------------------
"""
## this will still give you the whole thing including the print() statent in the file BUT you do not have to 
reference the function by the filename. just use the function directly
"""
# from  _9a_functions import *
# print(f"5 + 4 = {add(5,4)}")
# print(f"5 - 4 = {sub(5,4)}")
# print(f"5 x 4 = {mul(5,4)}")

### --------------------------------------
### from  _9a_functions import add, sub
### --------------------------------------
"""
 now you are just importing 2 funtion of all in that file.
 print statement will still print out
"""
# from  _9a_functions import add as addision, sub
# print(f"5 + 4 = {addision(5,4)}")
# print(f"5 - 4 = {sub(5,4)}")


### --------------------------------------
### list all function in  _9a_functions 
### --------------------------------------
"""

"""
# import _9a_functions
# print(dir(_9a_functions)) # this is a list ['__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'add', 'div', 'max', 'min', 'mul', 'os', 'sub']



### --------------------------------------
### documentation
### --------------------------------------
"""
if we view the default inbuilt functions in _9a_functions, we will see proper docs

"""
import _9a_functions as my_func
# print(help(str.lower))
# print(help(str.center))
"""
the above will 
-------------------------
Help on method_descriptor:

center(self, width, fillchar=' ', /) unbound builtins.str method
    Return a centered string of length width.
    
    Padding is done using the specified fill character (default is a space).
None
------------------------
the below will show some like 

Help on function add in module _9a_functions:

add(a, b)

None
"""

# print(help(my_func.add))
### for proper comments










### --------------------------------------
### 
### --------------------------------------
"""

"""
print(my_func.name)



### --------------------------------------
### Print variable
### --------------------------------------
"""

"""





### --------------------------------------
### 
### --------------------------------------
"""

"""




### --------------------------------------
### 
### --------------------------------------
"""

"""




### --------------------------------------
### 
### --------------------------------------



### ========================================================================================
### 
### ========================================================================================



### --------------------------------------
### 
### --------------------------------------
"""

"""




### --------------------------------------
### 
### --------------------------------------
"""

"""




### --------------------------------------
### 
### --------------------------------------
"""

"""




### --------------------------------------
### 
### --------------------------------------
"""

"""




### --------------------------------------
### 
### --------------------------------------
"""

"""




### --------------------------------------
### 
### --------------------------------------
"""

"""




### --------------------------------------
### 
### --------------------------------------
"""

"""




### --------------------------------------
### 
### --------------------------------------
"""

"""




### --------------------------------------
### 
### --------------------------------------



### ========================================================================================
### 
### ========================================================================================



### --------------------------------------
### 
### --------------------------------------
"""

"""




### --------------------------------------
### 
### --------------------------------------
"""

"""




### --------------------------------------
### 
### --------------------------------------
"""

"""




### --------------------------------------
### 
### --------------------------------------
"""

"""




### --------------------------------------
### 
### --------------------------------------
"""

"""




### --------------------------------------
### 
### --------------------------------------
"""

"""




### --------------------------------------
### 
### --------------------------------------
"""

"""




### --------------------------------------
### 
### --------------------------------------
"""

"""




### --------------------------------------
### 
### --------------------------------------



### ========================================================================================
### 
### ========================================================================================



### --------------------------------------
### 
### --------------------------------------
"""

"""




### --------------------------------------
### 
### --------------------------------------
"""

"""




### --------------------------------------
### 
### --------------------------------------
"""

"""




### --------------------------------------
### 
### --------------------------------------
"""

"""




### --------------------------------------
### 
### --------------------------------------
"""

"""




### --------------------------------------
### 
### --------------------------------------
"""

"""




### --------------------------------------
### 
### --------------------------------------
"""

"""




### --------------------------------------
### 
### --------------------------------------
"""

"""




### --------------------------------------
### 
### --------------------------------------



### ========================================================================================
### 
### ========================================================================================



### --------------------------------------
### 
### --------------------------------------
"""

"""




### --------------------------------------
### 
### --------------------------------------
"""

"""




### --------------------------------------
### 
### --------------------------------------
"""

"""




### --------------------------------------
### 
### --------------------------------------
"""

"""




### --------------------------------------
### 
### --------------------------------------
"""

"""




### --------------------------------------
### 
### --------------------------------------
"""

"""




### --------------------------------------
### 
### --------------------------------------
"""

"""




### --------------------------------------
### 
### --------------------------------------
"""

"""




### --------------------------------------
### 
### --------------------------------------



### ========================================================================================
### 
### ========================================================================================



### --------------------------------------
### 
### --------------------------------------
"""

"""




### --------------------------------------
### 
### --------------------------------------
"""

"""




### --------------------------------------
### 
### --------------------------------------
"""

"""




### --------------------------------------
### 
### --------------------------------------
"""

"""




### --------------------------------------
### 
### --------------------------------------
"""

"""




### --------------------------------------
### 
### --------------------------------------
"""

"""




### --------------------------------------
### 
### --------------------------------------
"""

"""




### --------------------------------------
### 
### --------------------------------------
"""

"""




### --------------------------------------
### 
### --------------------------------------



### ========================================================================================
### 
### ========================================================================================



### --------------------------------------
### 
### --------------------------------------
"""

"""




### --------------------------------------
### 
### --------------------------------------
"""

"""




### --------------------------------------
### 
### --------------------------------------
"""

"""




### --------------------------------------
### 
### --------------------------------------
"""

"""




### --------------------------------------
### 
### --------------------------------------
"""

"""




### --------------------------------------
### 
### --------------------------------------
"""

"""




### --------------------------------------
### 
### --------------------------------------
"""

"""




### --------------------------------------
### 
### --------------------------------------
"""

"""




### --------------------------------------
### 
### --------------------------------------



### ========================================================================================
### 
### ========================================================================================



### --------------------------------------
### 
### --------------------------------------
"""

"""




### --------------------------------------
### 
### --------------------------------------
"""

"""




### --------------------------------------
### 
### --------------------------------------
"""

"""




### --------------------------------------
### 
### --------------------------------------
"""

"""




### --------------------------------------
### 
### --------------------------------------
"""

"""




### --------------------------------------
### 
### --------------------------------------
"""

"""




### --------------------------------------
### 
### --------------------------------------
"""

"""




### --------------------------------------
### 
### --------------------------------------
"""

"""




### --------------------------------------
### 
### --------------------------------------



### ========================================================================================
### 
### ========================================================================================



### --------------------------------------
### 
### --------------------------------------
"""

"""




### --------------------------------------
### 
### --------------------------------------
"""

"""




### --------------------------------------
### 
### --------------------------------------
"""

"""




### --------------------------------------
### 
### --------------------------------------
"""

"""




### --------------------------------------
### 
### --------------------------------------
"""

"""




### --------------------------------------
### 
### --------------------------------------
"""

"""




### --------------------------------------
### 
### --------------------------------------
"""

"""




### --------------------------------------
### 
### --------------------------------------
"""

"""




### --------------------------------------
### 
### --------------------------------------



### ========================================================================================
### 
### ========================================================================================



### --------------------------------------
### 
### --------------------------------------
"""

"""




### --------------------------------------
### 
### --------------------------------------
"""

"""




### --------------------------------------
### 
### --------------------------------------
"""

"""




### --------------------------------------
### 
### --------------------------------------
"""

"""




### --------------------------------------
### 
### --------------------------------------
"""

"""




### --------------------------------------
### 
### --------------------------------------
"""

"""




### --------------------------------------
### 
### --------------------------------------
"""

"""




### --------------------------------------
### 
### --------------------------------------
"""

"""




### --------------------------------------
### 
### --------------------------------------



### ========================================================================================
### 
### ========================================================================================









































































































































































print()
print()
print()
print()
print("----------------------------------------------------------------------------------------")


