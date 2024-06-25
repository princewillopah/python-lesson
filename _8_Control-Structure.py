print()
print()
print()


#=============if statement--------------------------
# num=int(input("enter number: "))
# if(num%2==0):
#     print("{} is an even number".format(num))
# else:
#     print("{} is an odd number".format(num))
#
# print("")
# ---------------------------------------------------------------------
# start=int(input("Enter the start value for the range: "));
# end=int(input("Enter the end value for the range: "));
# for num in range(start, (end+1)):
#     if(num%2==0 & num<2):
#         if(num==2):
#             print("{} is an even number and a prime number".format(num))
#         else:
#             print("{} is an even number".format(num))
#     else:#for odd above 2
#         if(num/num == 1):
#             print("{} is an odd number and a prime number".format(num))
#         else:
#             print("{} is an odd number".format(num))
# -----------------------------------------------------------------------------
# import math
# start=int(input("Enter the start value for the range: "));
# end=int(input("Enter the end value for the range: "));
# for num in range(start, (end+1)):
#     print("{}! = {} ".format(num,math.factorial(num)))
# --------------------------------------------------------------------------


# =================================================================================
#                                for
# =================================================================================
# for i in range(5):
#   print("(",i+1,") python")


# start=int(input("Enter the start value for the range: "));
# end=int(input("Enter the end value for the range: "));
# for i in range(start,(end+1)):
#     print("({}) {}".format(i,"hello python"))

# fname = ["princewill","Grace","Bayero","Nkoyo","Tony","chidinma"]
# for n in range(len(fname)):
#     print("({0}) {1}".format(n+1,fname[n]))
# for n in fname:
#     print(n)

# fname = ["princewill","Grace","Bayero","Nkoyo","Tony","chidinma"]
# lname = ["opah","jude","anthony","coco","lolaa","opara"]
# for n in range(len(fname)):
#     print("({0}) {1} {2}".format(n+1,fname[n],lname[n]))

# emails = ['tata@gmail.com','theff@yahoo.com','rere@yahoo','tali@yahoo','plkj@gmail']
# for em in emails:
#     if "yahoo" in em:
#         print(em)
# =================================================================================
#                                while
# =================================================================================
# fname = ["princewill","Grace","Bayero","Nkoyo","Tony","chidinma"]
# lname = ["opah","jude","anthony","coco","lolaa","opara"]
# n=0;
# while(n<len(fname)):
#     print("({0}) {1} {2}".format(n + 1, fname[n], lname[n]))
#     n=n+1;
# =================================================================================
#                                while
# =================================================================================



# -----------------------------------

# if condtion:
#     do whatever you want to do
# ---------------------------------------
# if condtion:
#     do whatever you want to dodo
# else:
#     do something else

# -------------------------------------

# if condition:
#     do whatever you want to dodo
# elif condition:
#     do something else
# elif condition:
#       do something else
# elif condition:
#   do something else
# elif condition:
#   do something else
   
# --------------------------

# if condition:
#     do whatever you want to dodo
# elif condition:
#     do something else
# elif condition:
#       do something else
# elif condition:
#   do something else
# elif condition:
#   do something else
# else:
#     do something else


# ===========================
# CONDITIONS
# ========================
# Equals: a == b
# Not Equals: a != b
# Less than: a < b
# Less than or equal to: a <= b
# Greater than: a > b
# Greater than or equal to: a >= b

# =====================================
# EXAMPLES
# =====================================

# Lola = 14
# Bukky = 10

# if 200 < 114:  # false
#     print("Bukky will go beat up my troublemaker")
# elif 9 > 10: #  / false
#     print("Lola will go beat up my troublemaker")
# elif 9 > 10: # false
#     print("Tayo will go beat up my troublemaker")
# elif 3 >= 10: # false
#     print("Bose will go beat up my troublemaker")
# elif 6 > 10: #false
#     print("James will go beat up my troublemaker")
# else:  # true
#     print("Ada will go beat up my troublemaker")



# if False:  # false
#     print("Bukky will go beat up my troublemaker")
# elif True: #  / false
#     print("Lola will go beat up my troublemaker")
# elif False: # false
#     print("Tayo will go beat up my troublemaker")
# elif True: # false
#     print("Bose will go beat up my troublemaker")
# elif False: #false
#     print("James will go beat up my troublemaker")
# else:  # true
#     print("Ada will go beat up my troublemaker")

# a = 33
# b = 33
# if b > a:
#   print("b is greater than a")
# elif a == b:
#   print("a and b are equal")


# a = 200
# b = 33
# if b > a:
#   print("b is greater than a")
# elif a == b:
#   print("a and b are equal")
# else:
#   print("a is greater than b")



# a = 200
# b = 33
# if b > a:
#   print("b is greater than a")
# else:
#   print("b is not greater than a")

# ==============================
#  and | or
# =============================
# True and False = False    #  (14 > 5) and (14 > 20) = False
# False and True = False    #  (14 > 20) and (14 > 5) = False
# False and False = False   #  (14 > 20) and (15 > 20) = False
# True and True = True      #  (14 < 20) and (20 > 16) = True

# True or False = True      #  (14 > 5) or (14 > 20) = True
# False or True = True      #  (14 > 20) or (14 > 5) = True
# True or True = True       #  (14 < 20) or (20 > 16) = True
# False or False = False    #  (14 > 20) or (15 > 20) = False

# if False:  
#     print("Dan is okay")
# elif True: 
#     print("Brad is okay")
# elif False:
#     print("Tom is okay")
# elif True:
#     print("Charlse is okay")
# else:  
#     print("Greg is okay")

# if False and False:  
#     print("Dan is okay")
# elif True and False: 
#     print("Brad is okay")
# elif False and True:
#     print("Tom is okay")
# elif True and True:
#     print("Charlse is okay")
# else:  
#     print("Greg is okay")

# Tom = 20; Jack = 28; Paul = 14; Joe = 25; Mike = 33; Greg = 25;

# if (Greg > Paul) and (Joe > Greg): # (25 > 14) and (25 > 25) == TRUE and FALSE == FALSE
#     print(" Print orange")
# elif (Joe >= Jack) and (Joe <= Greg): # (Joe >= Jack) and (Joe <= Greg) == (25 >= 28) and  = FALSE  and TRUE  = FALSE
#     print("Pineapple")
# elif (Mike > Tom) or (Joe <= Greg): # (33 >= 20) or (25 <= 25) = TRUE or TRUE = TRUE
#     print("Mango")
# else:
#     print("Whatever!")

# 
# A=50; B=38; C=49; D=11; E=44; F=A-B; G=C-40;
# if (B >= C) and (F >= G): # (25 > 14) and (25 > 25) == TRUE and FALSE == FALSE
#     print("Orange")
# elif (B >= F) and (A <= D): # (38 >= 12) and (50 <= 11) == (25 >= 28) and  = FALSE  and TRUE  = FALSE
#     print("Pineapple")
# elif (C > F) or (G <= A): # (49 >= 12) or (9 <= 50) = TRUE or TRUE = TRUE
#     print("Apple")
# elif (D >= F) or (D == F): # (11 >= 12) or (11 == 12) = FALSE or FALSE = FALSE
#     print("Mango")
# else:
#     print("Whatever!")



# ( age < 13)
# ( age >=13) and (age <= 19)
# (age >= 20)

# questions:
# ----------------------------
# question 1
# Write an if-elif-else statement that prints:
# "You are a child" if age is less than 13,
# "You are a teenager" if age is between 13 and 19,
# "You are an adult" if age is 20 or older.
# age = 10

# ------------------------
# question 2
# Write an if statement that prints "x is greater than y" if x is greater than y.
# x = 5
# y = 3
# -----------------------------
# question 3
# Write an if-else statement that checks if a number is even or odd and prints "Even" or "Odd".
# number = 7

# -----------------------------
# question 4
# Write an if-elif-else statement that prints "Positive" if a number is positive,
# "Negative" if it is negative, and "Zero" if it is zero.
# number = -5

# Solution: 
# print(f"Enter your number :")
# num = int(input())

# if( num > 0):
#     print(f"{num} is Positive")
# else:
#     print(f"{num} is Nagative")

# -----------------------------
# question 5
# Write an if statement that prints "Vowel" if the variable letter is a vowel (a, e, i, o, u).
# letter = 'a'

# -----------------------------
# question 6
# Write an if-else statement that prints "Access Granted" if the password is "python123",
# otherwise prints "Access Denied".
# password = "python123"
# -----------------------------
# question 7
# Write an if statement that prints "Number is in range" if number is between 1 and 10 (inclusive).
# number = 7

# -----------------------------
# question 8

# Write an if-elif-else statement that prints:
# "Grade A" if score is 90 or above,
# "Grade B" if score is 80-89,
# "Grade C" if score is 70-79,
# "Grade D" if score is 60-69,
# "Grade F" if score is below 60.
# score = 85
# ----
# # Solution:
# print(f"Enter your Math score:")
# score = int(input())

# if(score == 90) or (score > 90): # 90 and above
#     print(f"Your Math scor is {score} and your Grade is A")
# elif(score >= 80) and (score <= 89): # 80-89,
#     print(f"Your Math scor is {score} and your Grade is B")
# elif(score >= 70) and (score <= 79): #70-79,
#     print(f"Your Math scor is {score} and your Grade is C")
# elif(score >= 60) and (score <= 69):  # 60-69,
#     print(f"Your Math scor is {score} and your Grade is D")
# elif(score >= 50) and (score <= 59): 
#     print(f"Your Math scor is {score} and your Grade is E")
# elif(score <= 50):
#     print(f"Your Math scor is {score} and you Failed. your score is below 50")
# else:
#     print("You grade is not out yet")














































print()
print()
print()
