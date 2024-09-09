import os
os.system('cls')
print("----------------------------------------------------------------------------------------")
print(" RESULTS")
print("----------------------------------------------------------------------------------------")
print()
print()











# num1 = int(input("Enter first number: "))
# num2 = int(input("Enter second number: "))

# add            = num1 + num2
# print(f"{num1} + {num2} = {add}")

# subtract       = num1 - num2
# print(f"{num1} - {num2} = {subtract}")

# multiplication = num1 * num2
# print(f"{num1} x {num2} = {multiplication}")


# if num2 == 0:
#     division  = None 
# else:
#    division = num1 / num2 
# print(f"{num1} / {num2} = {division}")

# ------------------------------------------------

# num1 = int(input("Enter first number: "))
# num2 = int(input("Enter second number: "))
# print()
# print(f"Type one of the following: add or sub or multiply or divide ")
# type_of_calculation = input()
# type_of_calculation = type_of_calculation.lower()

# print()
# if type_of_calculation == "add":
#     print(f"{num1} + {num2} = {num1+num2}")
# elif type_of_calculation == "sub":
#     print(f"{num1} - {num2} = {num1-num2}")
# elif type_of_calculation == "multiply":
#     print(f"{num1} x {num2} = {num1*num2}")
# elif type_of_calculation == "divide":
#     if num2 == 0:
#        answer = "No number is divisible by zero. Choose a real number BUT NOT ZERO"
#     else:
#        answer =  num1/num2
#     print(f"{num1} / {num2} = {answer}")
# else:
#     print(f"Sorry! '{type_of_calculation}' is not one of the operations i asked you to type. The opeartions are | add | sub | divide | multiply |")


# --------------------------



print(f"""You can find the areas of the following shapes:
Triangle       
rectangle  
circle       
sqaure      
trapozium   
Parallelogram """)
print()
user_shape = input("Now, enter the shape whose area you want to find: ")
user_shape = user_shape.lower()

if user_shape == "circle":
    r = int(input("Provide the Radius of the circle: "))
    answer = 3.14 * r * r 
    print(f"the area of a circle whose radius is {r}metre is {answer}metre")
elif user_shape == "rectangle":
    l = int(input("Provide the length of the rectangle: "))
    w = int(input("Provide the width of the rectangle: "))
    answer = l * w 
    print(f"For a Rectangle whose width is {w}metre and Length is {l}metre, the area is {answer} metre squre")



# Triangle       =  ½ base × height
# rectangle      =  lenght x width
# circle         =  pii x radius x radius
# sqaure         =  lenght x lenght
# trapozium      =  ½(lenght + base ) × heigth
# Parallelogram  = base x height


















































































































































































print()
print()
print()
print()
print("----------------------------------------------------------------------------------------")
