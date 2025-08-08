

import os
os.system('clear')
print("----------------------------------------------------------------------------------------")
print(" RESULTS")
print("----------------------------------------------------------------------------------------")
print()
print()



# def justPrint():
#     print("i am a function")

# justPrint()
# --------------------------------------------------------------
# def greet_user(name):
#     print(f"Hello, {name}!")

# greet_user("Alice")  # Output: Hello, Alice!
# greet_user("Bob")    # Output: Hello, Bob!

# --------------------------------------------------------------
# def basicOp(n1,n2):
#     print("{} + {} = {}".format(n1,n2,(n1+n2)))
#     print("{} - {} = {}".format(n1, n2, (n1 - n2)))
#     print("{} x {} = {}".format(n1, n2, (n1 * n2)))
#     print("{} / {} = {}".format(n1, n2, (n1 / n2)))

# basicOp(20,5)
# print()
# basicOp(2,5)
# --------------------------------------------------------------
# # --------------- default--------------------------------------------
# def person(fn,sn=" opah"):
#     print("you re welcome, mr {} {}".format(fn,sn))
# person("prince")
# person("prince","ujukwa")
# # -------------------------------------------------------------------
# def greet(*names):
#     for i in names:
#         print("hello {}".format(i))


# greet("monica","tony","john","grace")
# print()

# greet()
# print()

# greet("john","grace")

# ---------------------------------------------------------------
# def output(list_of_names):
#     for name in list_of_names:
#         print(f"Hello, {(name.capitalize())}!")

# list_names = ["alice", "bob", "charlie"]
# output(list_names)  # Output: Hello, Alice! Hello, Bob! Hello, Charlie

# -------------------------------------------

# def filter():
#     """
#     Filters a list of names to include only those that start with 'A'.
    
#     :param names: List of names
#     :return: Filtered list of names starting with 'A'
#     """
#     names = ["Alice", "Bob", "Charlie", "David", "Eve"]
#     filtered_names = [name for name in names if name.startswith('A')]
#     return filtered_names


# # Example usage
# filtered_list = filter()
# print("Filtered names starting with 'A':", filtered_list)  # Output: ['Alice']

# ---------------------------------------------------------------------------

# def sum_of_array(arr):
#     sum = 0;
#     for i in arr:
#         sum  = sum + i
#     return sum

# def filter(All_numbers):
#     prime_numbers = []
#     even_numbers = []
#     odd_numbers = []
  
#     for num in All_numbers:
#         if num % 2 == 0:
#             even_numbers.append(num)
#         else:
#             odd_numbers.append(num)
#         if num > 1:
#             for i in range(2, int(num**0.5) + 1):
#                 if num % i == 0:
#                     break
#             else:
#                 prime_numbers.append(num)
#     return prime_numbers, even_numbers, odd_numbers, sum_of_array(All_numbers), sum_of_array(prime_numbers), sum_of_array(even_numbers), sum_of_array(odd_numbers)

# # Example usage
# All_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
# prime_numbers, even_numbers, odd_numbers, sum_of_num, sum_of_prime_array, sum_of_even_array, sum_of_odd_array = filter(All_numbers)
# print("Prime numbers:", prime_numbers)  # Output: Prime numbers: [2, 3, 5, 7, 11, 13, 17, 19]
# print("Even numbers:", even_numbers)    # Output: Even numbers: [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
# print("Odd numbers:", odd_numbers)      # Output: Odd numbers: [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]  
# print("Sum of all numbers:", sum_of_num)  # Output: Sum of all numbers: 210
# print("Sum of prime numbers:", sum_of_prime_array)  # Output: Sum of prime numbers: 77
# print("Sum of even numbers:", sum_of_even_array)    # Output: Sum of even numbers: 110
# print("Sum of odd numbers:", sum_of_odd_array)      # Output: Sum of odd numbers: 105

# print()

# print("Sum of prime numbers:", sum_of_array(prime_numbers))  # Output: Sum of prime numbers: 77
# print("Sum of even numbers:", sum_of_array(even_numbers))    # Output: Sum of even numbers: 110
# print("Sum of odd numbers:", sum_of_array(even_numbers))      # Output: Sum of odd numbers: 105



# ---------------------------------------------------------------


# --------simple interest-------------------------------------------------------
# def simple(p,t):
#     amount = 0
#     print("{0:5} {1:9} {2:6}".format("month","principal","amount"))
#     for i in range(1, t+1):
#         interest = p * 0.05 * t  # Assuming 5% interest rate // principal * rate * time
#         amount =amount + p + interest
#         print("({0:1}) {1:9}  {2:8}".format(i, interest, amount))

# pp=int(input("Enter Principal: "))
# tt=int(input("Enter Number of Month: "))

# ## calling the function 
# simple(pp,tt)


## ----------------------------------------------------------------
# def calInterest(principal, time, rate=0.05):
#     """
#     Calculate simple interest.
    
#     :param principal: The principal amount
#     :param time: The time period in years
#     :param rate: The interest rate (default is 5%)
#     :return: The calculated interest
#     """
#     interest =  principal * rate * time
#     amount = principal + interest
#     return interest , amount


# # Example usage
# principal = int(input("Enter Principal: ")) # Principal amount
# time = int(input("Enter Time in years: "))  # Time period in years

# #Calculate interest and total amount
# interest, total_amount = calInterest(principal, time)
# print(
#     f"""Interest: {interest}, 
# Total Amount: {total_amount}
# """)
# -------------------------details---------------------

# def simple(principal,duration,rate):
#     total_interest = 0
#     amount = principal

#     print(f"{'Month':<8}{'Interest':<12}{'Amount':<12}")

#     for month in range(1, duration+1):
#         monthly_interest = principal * rate * month  # Assuming 5% interest rate // principal * rate * time
#         total_interest = total_interest + monthly_interest   # Cumulative interest
#         amount = principal + total_interest
#         # print("{0:1} {1:9}  {2:8}".format(i, interest, amount))
#         print(f"({month}){'' if month >= 10 else ' '}"  # Extra space for single-digit months
#               f"{'':<4}"
#               f"{total_interest:<12.1f}"
#               f"{amount:<12.1f}")
        


# principal = float(input("Enter Principal: "))
# num_months = int(input("Enter Number of Months: "))
# rate_per_year = 0.05  # 5% annual interest rate
# print()
# print("-" * 50)
# print()
# ## calling the function 
# simple(principal,num_months,rate_per_year)



# ---------------------------------------------------------------

# -----------------------fac--------------------------------------------
# def fac(num):
#    if(num==0 | num==1):
#        return 1
#    else:
#        return num*fac(num-1)
# n = int(input("Enter number: "))
# print("{}! = {}".format(n,fac(5)))
# ------------------------------------------------------------------------
# def exp(x):
#     return x*x
# print(exp(5))
# exp2=lambda x: x*x
# print(exp2(5))
# --------------------------------------------------------------------------------------------------------------------
# def vel(dist,time):
#     return dist/time
# def acc(vel,time):
#     return vel/time
# def force(acc,mass):
#     return mass*acc
# def kinetic_energy(vel,mass):
#     return (vel*vel*mass)/2
# def phy(d,m,t):
#     velocity=vel(d,t)
#     acceleration=acc(velocity,t)
#     forcess=force(acceleration,m)
#     K_E=kinetic_energy(velocity,m)
#     print("the velocity {}m and {}s is {}m/s".format(d,t,velocity))
#     print("the acceleration {}m/s and {}s is {}m/s/s".format(velocity, t, acceleration))
#     print("the force of {}m/s/s and {}kg is {}N".format(acceleration,m,forcess))
#     print("the kinetic energy {}m/s and {}kg is {} joules".format(velocity,m,K_E))
# dist=int(input("Enter Distance covered by object: "))
# time=int(input("Enter Time taken by object during movement: "))
# mass=int(input("Enter Mass of object: "))
# phy(dist,mass,time)
# -----------------------------------------*arg-----------------------------------------------
# def total(*args):
#     s=0
#     for x in args:
#         s=s+x
#     return s
# tot=total(45,67,34,89)
# print(tot)

#----------------------------------------------lambda function ---------------------------------------------------------------------
# add = lambda x,y: x+y
# sub = lambda x,y: x-y
# max = lambda x,y: x if x > y  else y
# fn=int(input("ENTER FIRST NUMBER: "))
# sn=int(input("ENTER SECOND NUMBER: "))
# print("maximum of {} and {} is {}".format(fn,sn,max(fn,sn)))
# print("sum and difference of {} and {} are {} and {} respectively".format(fn,sn,add(fn,sn),sub(fn,sn)))

# largest_num = lambda a,b,c : a if a>b and a>c else b if b>a and b>c else c if c>a and c>b else a
# ---------------------------------------map------------------------------------------------------------------------
# mylist = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25];
# def square(lis):
#     lis2 = []
#     for eachNum in lis:
#         lis2.append(eachNum**2)
#     return lis2
# print("Original list: ",mylist)
# print("Squared list: ",square(mylist))
# square2 = list(map(lambda x:x**2,mylist))
# print("Squared map list: ",square2)

# --------------------------------------------filter------------------------------------------------------------------------------------
# mylist = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25];
# def even(num):
#     return num%2==0
# result=filter(even,mylist)
# print(list(result))
# result2=filter(lambda x:(x%3==0),mylist)
# print(list(result2))
# ---------------------------------generators-------------------------------------------------------------------
# mylist = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25];
# def square(lis):
#      for n in lis:
#          yield (n**2)

# result = square(mylist)
# for x in result:
#     print(x, end=" ")
# ------------ list comprehension(List Manipulation in Functions) ---------------------------
# myy = [n**2 for n in range(1,26)]
# print(myy)
# ----------
# def girls(girls_names):
#     girls = [girl.capitalize() for girl in girls_names  ]
#     return girls

# def girls_that_start_with_J(names):
#     girls = [girl for girl in names if girl.lower().startswith("j")]
#     return girls


# names_of_girls = ["monica","rachel","phoebe","jennifer","lisa", "julia","sandra","jane", "mary","jessica", "susan","karen","linda","laura","sarah","emma","olivia","ava","isabella","mia"]
# mygirls = girls(names_of_girls)
# J_girls = girls_that_start_with_J(names_of_girls)
# print(mygirls) # ['Monica', 'Rachel', 'Phoebe', 'Jennifer', 'Lisa', 'Julia', 'Sandra', 'Jane', 'Mary', 'Jessica', 'Susan', 'Karen', 'Linda', 'Laura', 'Sarah', 'Emma', 'Olivia', 'Ava', 'Isabella', 'Mia']
# print(J_girls) 
# ----------------- closure -----------------------------------
#
# def outer_func(name):
#     message = "Hi"
#     def inner_func():
#         print(message,name)
#     return inner_func()
# # # outer_func()  # returns HIIII
# # my_func = outer_func
# # my_func("prince")
# #     or
# my_func = outer_func("prince")
# my_func
#-------------------------decorator-----------------------------------------

# def greet():
#     print("I am from external function")
# def decorFunc(externalFunc):
#     print("i am from decorator main")
#     def innerdecor():
#         print("i am from inner decorator")
#         externalFunc()
#         print("i am from inner decor 2")
#     return innerdecor

# aa=decorFunc(greet)
# aa()
# #





































































































print()
print()
print()
print()
print("----------------------------------------------------------------------------------------")






