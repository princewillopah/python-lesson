print()
print()
print()
print()


# A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).
# This is less like the for keyword in other programming languages, and works more like an iterator method as found in other object-orientated programming languages.
# With the for loop we can execute a set of statements, once for each item in a list, tuple, set etc

# ----------------------------------------------
# for iterating_var in sequence:
#    statement(s)
# ----------------------------------------------

# words1 = """A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).
# This is less like the for keyword in other programming languages, and works more like an iterator method as found in other object-orientated programming languages.
# With the for loop we can execute a set of statements, once for each item in a list, tuple, set etc"""

# names =  ["Kunle","Ade","Olumide",'Adam', 'Joseph', 'Leo', 'Peter', 'Evans','Mathew', 'Banabas', 'Smart','Joe', 'Smith', 'Ken', "Apolo",'Paul','Mary', 'Jennifer', 'Linda', 'Patricia', 'Elizabeth','Mary,' 'Barbara', 'Susan','Jessica', 'Sarah', 'Karen', "Alice",'Karen','Robert Lewandowski', 'Lionel Messi', 'Eden Hazard', 'Cristiano Ronaldo', 'Kevin De Bruyne', 'Mohamed Salah', 'Kylian Mbappé', 'Neymar Jr.']
# list2 = [2,3,4,3,4,2,4,5,6,7,8,5,4,5,5]

# ---------------------------------------------------------------------------------------------------------------
# BASIC FOR
# ---------------------------------------------------------------------------------------------------------------

# for a in words1:
#   print(a)

# for a in list1:
#   print(a)


# for a in list2:
#     print(a)

## the above will print each "item" in the string or in the list. where "a" is assigned to each item for each iteration 
# -------------------------------------

# for i in range(len(list1)):
#     print(list1[i])

# print()

# for i in list1:
#     print(i, end=", ")
# print()
# print()
# for i in range(len(list1)):
#     print(list1[i], end=", ")

# xx = ["Kunle","Ade","Olumide"]
# print()
# for _ in range(5):
#     for i in range(len(xx)):
#         print(xx[i])

# ---------------------------------------------------

# names =  ["Kunle","Ade","Olumide",'Adam', 'Joseph', 'Leo', 'Peter', 'Evans','Mathew', 'Banabas', 'Smart','Joe', 'Smith', 'Ken', "Apolo",'Paul','Mary', 'Jennifer', 'Linda', 'Patricia', 'Elizabeth','Mary,' 'Barbara', 'Susan','Jessica', 'Sarah', 'Karen', "Alice",'Karen','Robert Lewandowski', 'Lionel Messi', 'Eden Hazard', 'Cristiano Ronaldo', 'Kevin De Bruyne', 'Mohamed Salah', 'Kylian Mbappé', 'Neymar Jr.']

# for index, name in enumerate(names, start=1):
#     print(f"{index}) {name.capitalize()}")
# -----------------------
# ------------------------
# # Initialize index counter
# index = 1
# # Print each name with the specified format
# for name in names:
#     print(f"{index}) {name.capitalize()}")  # Capitalize the first letter of each name
#     index += 1  # Increment index counter



# ---------------------------------------------------------------------------------------------------------------
# RANGE

# Range() function - The range() function returns a sequence of numbers, starting from 0 by default, and increments 
# by 1 (by default), and ends at a specified number. 
# To loop through a set of code a specified number of times, we can use the range() function
# ---------------------------------------------------------------------------------------------------------------

# - range(start, stop, step)
# - the format is range(starting-value, end-value, increemtal-value)
# - The range() function defaults to 0 as a starting value, however it is possible to specify the starting value by adding a parameter: range(2, 6), 
#   which means values from 2 to 6 (but not including 6)
# - The range() function defaults to increment the sequence by 1, however it is possible to specify the increment value by adding a third parameter: range(2, 30, 3):
# - for loops cannot be empty, but if you for some reason have a for loop with no content, put in the pass statement to avoid getting an error.



# for num in range(6):
#    print (num, end=' ')

# print()

# for num in range(2, 20):
#    print (num, end=' ')

# print()

# for num in range(2, 30, 3):
#    print (num, end=' ')


# for num in range(2, 30, 3):
#    pass



# ---------------------------------------------------------------------------------------------------------------
# For Else Loop
# ---------------------------------------------------------------------------------------------------------------
######
# for count in range(6):
#    print ("Iteration no. {}".format(count))
# else:
#    print ("for loop over. Now in else block")
# print ("End of for loop")
######
# for i in ['T','P']:
#    print(i)
# else:
#    # Loop else statement
#    # there is no break statement in for loop, hence else part gets executed directly
#    print("ForLoop-else statement successfully executed")
#####

# for i in ['T','P']:
#    print(i)
#    break
# else:
#    # Loop else statement
#    # terminated after 1st iteration due to break statement in for loop
#    print("Loop-else statement successfully executed")

####

# creating a function to check whether the list item is a positive or a negative number

# def positive_or_negative():
#    # traversing in a list
#    for i in [5,6,7]:
#    # checking whether the list element is greater than 0
#       if i>=0:
#          # printing positive number if it is greater than or equal to 0
#          print ("Positive number")
#       else:
#          # Else printing Negative number and breaking the loop
#          print ("Negative number")
#          break
#    # Else statement of the for loop
#    else:
#       # Statement inside the else block
#       print ("Loop-else Executed")
# # Calling the above-created function
# positive_or_negative()
# ---------------------------------------------------------------------------------------------------------------
# The break Statement 
# The continue Statement
# ---------------------------------------------------------------------------------------------------------------
# With the break statement we can stop the loop before it has looped through all the items:
# With the continue statement we can stop the current iteration of the loop, and continue with the next:

## --- break ----------------------------------
# fruits = ["apple", "banana", "cherry"]
# for x in fruits:
#   print(x)
#   if x == "banana":
#     break

# fruits = ["apple", "banana", "cherry"]
# for x in fruits:
#   if x == "banana":
#     break
#   print(x)

## --- continue ----------------------------------

# fruits = ["apple", "banana", "cherry"]
# for x in fruits:
#   if x == "banana":
#     continue
#   print(x)


# ---------------------------------------------------------------------------------------------------------------
# Else in For Loop
# ---------------------------------------------------------------------------------------------------------------

# for x in range(6):
#   print(x)
# else:
#   print("Finally finished!")

# print()

# for x in range(6):
#   if x == 3: break
#   print(x)
# else:
#   print("Finally finished!")

# ---------------------------------------------------------------------------------------------------------------
# Nested Loops
# ---------------------------------------------------------------------------------------------------------------
# adj = ["red", "big", "tasty"]
# fruits = ["apple", "banana", "cherry"]

# for x in adj:
#   for y in fruits:
#     print(x, y)

# ---------------------------------------------------------------------------------------------------------------
# Examples 
# ---------------------------------------------------------------------------------------------------------------

# Find the sum and avearge of a list
# numbers = [34,54,67,21,78,97,45,44,80,19]
# total = 0
# for num in numbers:
#    total += num
# print (f"Total = {total}\nAverage = {total/len(numbers)}")

# ---------------------------------------------------------------------------------------------------------------
# print all prime numbers
# ---------------------------------------------------------------------------------------------------------------
# numbers_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
#                 11, 12, 13, 14, 15, 16, 17, 18, 19, 20,
#                 21, 22, 23, 24, 25, 26, 27, 28, 29, 30,
#                 31, 32, 33, 34, 35, 36, 37, 38, 39, 40,
#                 41, 42, 43, 44, 45, 46, 47, 48, 49, 50]



# def is_prime(n):

#     if n <= 1:
#         return False
#     if n == 2:
#         return True
#     for i in range(2, n):
#         if n % i == 0:
#             return False
#     return True


# if is_prime(num):
#         prime_numbers_list.append(num)
#         sum_of_prime_numbers_list += num



# for i in range(2, n):

# This line starts a loop where i takes on values starting from 2 up to n-1.
# Example: If n is 10, range(2, 10) generates values [2, 3, 4, 5, 6, 7, 8, 9].
# if n % i == 0:

# Inside the loop, this line checks if n is divisible by i without leaving a remainder (i.e., n modulo i equals 0).
# If n is divisible by i, it means n has a divisor other than 1 and itself.
# Example: If n is 10 and i is 2, 10 % 2 == 0 is True, indicating 10 is not a prime number.
# return False

# If n is found to be divisible by any number i (where 2 <= i < n), the function immediately returns False.
# This indicates that n is not a prime number because it has divisors other than 1 and itself.
# ---------------------------------------------------------------------------------------------------------------
# get sum of all odd,evenprime from a list of numbers
# ---------------------------------------------------------------------------------------------------------------
# def is_prime(n):

#     if n <= 1:
#         return False
#     if n == 2:
#         return True
#     for i in range(2, n):
#         if n % i == 0:
#             return False
#     return True




# numbers_list = list(range(1, 51))
# # numbers_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
# #                 11, 12, 13, 14, 15, 16, 17, 18, 19, 20,
# #                 21, 22, 23, 24, 25, 26, 27, 28, 29, 30,
# #                 31, 32, 33, 34, 35, 36, 37, 38, 39, 40,
# #                 41, 42, 43, 44, 45, 46, 47, 48, 49, 50]
# odd_numbers_list = []
# even_numbers_list = []
# prime_numbers_list = []

# sum_of_numbers_list = 0
# sum_of_odd_numbers_list = 0
# sum_of_even_numbers_list = 0
# sum_of_prime_numbers_list = 0

# for num in numbers_list:
#     sum_of_numbers_list += num
#     if num % 2 == 0:
#         even_numbers_list.append(num)
#         sum_of_even_numbers_list += num
#     else:
#         odd_numbers_list.append(num)
#         sum_of_odd_numbers_list += num
#     if is_prime(num):
#         prime_numbers_list.append(num)
#         sum_of_prime_numbers_list += num

# print(f"All Numbers: {numbers_list}")
# print(f"Total = {sum_of_numbers_list}\nAverage = {sum_of_numbers_list / len(numbers_list)}")

# print()

# print(f"Odd Numbers: {odd_numbers_list}")
# print(f"Total = {sum_of_odd_numbers_list}\nAverage = {sum_of_odd_numbers_list / len(odd_numbers_list)}")

# print()

# print(f"Even Numbers: {even_numbers_list}")
# print(f"Total = {sum_of_even_numbers_list}\nAverage = {sum_of_even_numbers_list / len(even_numbers_list)}")

# print()

# print(f"Prime Numbers: {prime_numbers_list}")
# print(f"Total = {sum_of_prime_numbers_list}\nAverage = {sum_of_prime_numbers_list / len(prime_numbers_list)}")
# ---------------------------------------------------------------------------------------------------------------
# get sum of all odd,evenprime from a list of numbers - version 2
# ---------------------------------------------------------------------------------------------------------------
# start=int(input("Enter the start value for the range: "));
# end=int(input("Enter the end value for the range: \n"));
# print(f"List will be: {list(range(start, (end+1)))}\n")
# for num in range(start, (end+1)):
#     if(num%2==0 & num<2):
#         if(num==2):
#             print("{} | even number | prime number |".format(num))
#         else:
#             print("{} | even number |".format(num))
#     else:#for odd above 2
#         if(num/num == 1):
#             print("{} | odd number | prime number |".format(num))
#         else:
#             print("{} | odd number |".format(num))
# ---------------------------------------------------------------------------------------------------------------
# The following example illustrates the combination of an else statement with a for statement that searches for prime numbers from 1 to 25.
# ---------------------------------------------------------------------------------------------------------------
##For loop to iterate between 10 to 20
# for num in range(1, 25):  
#    #For loop to iterate on the factors 
#    for i in range(2,num): 
#       #If statement to determine the first factor
#       if num%i == 0:      
#          #To calculate the second factor
#          j=num/i          
#         #  print ("%d * %d = d" % (i,j,num))
#          print (f"{num} = {i} * {int(j)}")
#          #To move to the next number
#          break 
#       else:                  
#          print (num, "= prime number")
#          break
# ---------------------------------------------------------------------------------------------------------------
# 
# ---------------------------------------------------------------------------------------------------------------



# ---------------------------------------------------------------------------------------------------------------
# 
# ---------------------------------------------------------------------------------------------------------------

# ---------------------------------------------------------------------------------------------------------------
# 
# ---------------------------------------------------------------------------------------------------------------



# ---------------------------------------------------------------------------------------------------------------
# 
# ---------------------------------------------------------------------------------------------------------------

# ---------------------------------------------------------------------------------------------------------------
# 
# ---------------------------------------------------------------------------------------------------------------



# ---------------------------------------------------------------------------------------------------------------
# 
# ---------------------------------------------------------------------------------------------------------------
### Python for Loop with Tuples
# numbers = (34,54,67,21,78,97,45,44,80,19)
# for x in numbers:
#    print (x)

### Python for Loop with Lists
# numbers = [34,54,67,21,78,97,45,44,80,19]
# for x in numbers:
#    print (x)


### Python for Loop with Dictionaries
# numbers = {10:"Ten", 20:"Twenty", 30:"Thirty",40:"Forty"}

# for x in numbers:
#    print (x)

# print()

# for x in numbers:
#    print (x,":",numbers[x])

# print()

# for x in numbers.items():
#    print (x)






# ---------------------------------------------------------------------------------------------------------------
# 
# ---------------------------------------------------------------------------------------------------------------













































































































print()
print()
print()
print()