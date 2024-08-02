
print()
print()
print()


# ---------------------------------------------
# If Statements
# -------------------------------------------
# Question 1:
# Write a Python program that checks if a number entered by the user is positive, negative, or zero.
# 

# ## solution
# number = int(input("Enter a number: "))
# if number > 0:
#     print(f"{number} is a positive number")
# elif number < 0:
#     print(f"{number} is a negative number")   
# else:
#     print(f"{number} is zero")


# # Question 2:
# # Write a Python program that checks if a given year is a leap year. 
# (Hint: A year is a leap year if it is divisible by 4, but not by 100, unless it is also divisible by 400).
# year = int(input("Enter a year: "))
# # Write your if statement here

## solution
# year = int(input("Enter a year so i can tell you if it is a leap year or not: "))

# if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
#     print(f"{year} is a leap year.")
# else:
#     print(f"{year} is not a leap year.")

 ## OR 

# if (year % 4 == 0 and year % 100 != 0):
#     print(f"{year} is a leap year.")
# elif  (year % 400 == 0):
#     print(f"{year} is a leap year.")
# else:
#     print(f"{year} is not a leap year.")

 ## OR 

# names = ["Paul","Jude","Amanda","Ronaldino","Micheal"]

# for n in names:
#     if len(n) > 7:
#       print(f"{n} is TOP qualified")
#     elif len(n) > 4:
#        print(f"{n} is qualifier")
#     else:
#       print(f"{n} is NOT qualified")





# # -------------------------------------------
# # For Loops
# # -------------------------------------------


# # Question 3:
# # Write a Python program to print numbers from 1 to 10 using a for loop.

# num = [1,2,3,4,5,6,7,8,9,10,11]
## solution

# for i in num:
#     print(i)

# for i in range(1, 11):
#     print(i)



# Write your for loop here
# Question 4:
# Write a Python program that prints the multiplication table of a number entered by the user up to 10

# solution
# number = int(input("Enter a number: "))
# number = 7
# for i in range(1, 11): # 1,2,3,4,5,6,7,8.9.10
#     # print(f"{number} x {i} = {number * i}")
#     print(f"{number} x {i} = {i*number}")
# Write a Python program that prints the multiplication table of a number entered by the user up to 10

# number = 5
#  print(f"{number} x {i} = {number * i}")
# 5 * 1 = 5
# 5 * 2 = 10
# 5 * 3 = 15
# 5 x 4 = 20
# 5 x 5 = 25
# 5 x 6 = 30
# 5 x 7 = 35
# 5 x 8 = 40
# 5 x 9 = 45
# 5 x 10 = 50

# num1 = 10
# num2 = 5

# print(f"{num1} x {num2} = {num1*num2}")  # 10 x 5 = 50

# number = int(input("Enter a number: "))

# num1 = 3
# my_list = [2,6,10,14,18,20]

# for i in my_list: 
#     # print(f"{num1} x {i} = ")
#     print(f"{i} x {num1} = {i*num1}")


# print(f"{number} x 1 = {number * 1} ")
# print(f"{number} x 2 = {number * 2} ")
# print(f"{number} x 3 = {number * 3} ")
# print(f"{number} x 4 = {number * 4} ")
# print(f"{number} x 5 = {number * 5} ")
# print(f"{number} x 6 = {number * 6} ")
# print(f"{number} x 7 = {number * 7} ")
# print(f"{number} x 8 = {number * 8} ")
# print(f"{number} x 9 = {number * 9} ")
# print(f"{number} x 10 = {number * 10} ")



# range1 = range(1,5)
# range2 = range(3,15)
# range3 = range(3,15,2)
# range4 = range(1,15,1)
# range5 = range(2,15,5)
# range6 = range(2,21,4)

# list1 = list(range(1,5))
# list2 = list(range(3,15))
# list3 = list(range(3,15,2))
# list4 = list(range(1,15,1))
# list5 = list(range(2,15,5))
# list6 = list(range(2,21,4))

# print(list1)
# print(list2)  #3,4,5,6,7,8,9,10,11,12,13,14
# print(list3) #3,5,7,9,11,13
# print(list4) # 1,2,3,4,5,6,7,8,9,10,11,12,13,14
# print(list5) # 2,7,12
# print(list6)  # 2,6,10,14,18

# my_range = range(2,21,2)

# for i in my_range:
#     print(i)

# for i in range(2,21,2):   #  range(2,21,2) = 2,4,6,8,10.12,14,16,18,20
#     print(i)



# for i in ["apple","june","play","orange","Gold"]:
#     print(i)

# i = "apple"      print(i)      apple
# i = "june"       print(i)      june
# i = 4           print(i)      4
# i = 5           print(i)      5
# i = 6
# i = 7
# i = 8
# i = 9
# i = 10


# students = {
#             'student_1': "love",
#             'student_2': "color",
#             'student_3': "greeb",
#             'student_4': "Blow",
#             'student_5': "tom",
#             'student_6':  5,
#             'student_7': "Man",
          
#             }

# students = {'student_1': "love",'student_2': "color",'student_3': "greeb",'student_4': "Blow",'student_5': "tom",'student_6': "five",'student_7': "Man"}
# print(students["student_5"]) 

# students1 = ["love","color","green","Blow","tom","Man"]
# print(students1[4])
# for i in students:
#     print(i)

# world_presidents = {"America":"Biden", "England":"Keir","Nigeria":"Tunubu"}

# print(world_presidents["England"])

# for i in world_presidents:
#     print(world_presidents[i])

# print(world_presidents["Nigeria"])

# world_presidents2 = ["Biden","Keir","Tunubu"]

# print(world_presidents2[2])

# # -------------------------------------------
# # Lists
# # -------------------------------------------

# # Question 5:
# # Write a Python program that prints all the items in a list.
# fruits = ["apple", "banana", "cherry"]
# # Write your for loop here to print each fruit

# ## solution
# fruits = ["apple", "banana", "cherry"]

# for fruit in fruits:
#     print(fruit)




# # Question 6:
# # Write a Python program to find the largest number in a list.
# numbers = [3, 5, 7, 2, 8]
# # Write your code here to find the largest number

## solution
# numbers = [3, 5, 7, 2, 8]

# largest = numbers[0]
# for number in numbers:
#     if number > largest:
#         largest = number

# print(f"The largest number is {largest}")



# # -------------------------------------------
# # Combining Topics
# # -------------------------------------------
# # Question 7:
# # Write a Python program that prints all the even numbers from a list of numbers.
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# # Write your code here


# ## solution
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# for number in numbers:
#     if number % 2 == 0:
#         print(number)



# # Question 8:
# # Write a Python program that counts how many times a specific value appears in a list.
# numbers = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
# value = int(input("Enter a value to count: "))
# # Write your code here

## solution
# numbers = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
# value = int(input("Enter a value to count: "))

# count = 0
# for number in numbers:
#     if number == value:
#         count += 1

# print(f"The value {value} appears {count} times in the list.")



# # Question 9:
# # Write a Python program that prints all numbers from 1 to 20, but for multiples of 3, print "Fizz" instead of the number, and for the multiples of 5, print "Buzz". For numbers which are multiples of both 3 and 5, print "FizzBuzz".
# # Write your code here


## solution
# for i in range(1, 21):
#     if i % 3 == 0 and i % 5 == 0:
#         print("FizzBuzz")
#     elif i % 3 == 0:
#         print("Fizz")
#     elif i % 5 == 0:
#         print("Buzz")
#     else:
#         print(i)






# # Question 10:
# # Write a Python program to create a new list that contains the squares of all the numbers in a given list.
# numbers = [1, 2, 3, 4, 5]
# # Write your code here

## solution
# numbers = [1, 2, 3, 4, 5]
# squares = []

# for number in numbers:
#     squares.append(number ** 2)

# print(squares)






female_names = ['Mary', 'Jennifer', 'Linda', 'Patricia', 'Elizabeth','Mary' 'Barbara', 'Susan','Jessica', 'Sarah', 'Karen', "Alice",'Karen']
male_names = ['Adam', 'Joseph', 'Leo', 'Peter', 'Evans','Mathew', 'Banabas', 'Smart','Joe', 'Smith', 'Ken', "Apolo",'Paul']

not_S_listlist = []
S_names = []


for n in female_names:
    if ("s" in n) or ("S" in n):
        S_names.append(n)
        male_names.append(n)
    else:
        not_S_listlist.append(n)


print(S_names)
print(not_S_listlist)
print(male_names )


















































print()
print()
print()