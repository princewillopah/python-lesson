# The word "polymorphism" means "many forms", and in programming it refers to methods/functions/operators with the same name that can be executed on many objects or classes.
# it allows objects of different types to be treated as if they were of the same type
# Polymorphism is often used in Class methods, where we can have multiple classes with the same method name.
# If a method in a parent class is overridden with different business logic in its different child classes, the base class method is a polymorphic method


## examples-------------------
## Python's built-in functions like len() demonstrate polymorphism. It works on different data types:
# my_list = [1, 2, 3]
# my_string = "hello"
# my_dict = {"a": 1, "b": 2}

# print(len(my_list))  # Output: 3
# print(len(my_string))  # Output: 5
# print(len(my_dict))  # Output: 2

### -----------------------------------------------
# Polymorphism with Inheritance
## -----------------------------------------------
## Consider a base class Animal and derived classes Dog and Cat:

# class Animal:
#     def make_sound(self):
#         print("Generic animal sound")

# class Dog(Animal):
#     def make_sound(self):
#         print("Woof!")

# class Cat(Animal):
#     def make_sound(self):
#         print("Meow!")

# def animal_sound(animal):
#     animal.make_sound()

# # Create objects
# dog = Dog()
# cat = Cat()

# # Call the function with different objects
# animal_sound(dog)  # Output: Woof!
# animal_sound(cat)  # Output: Meow!

### -----------------------------------------------
# Polymorphism with Inheritance
## -----------------------------------------------

# class Vehicle:
#   def __init__(self, brand, model):
#     self.brand = brand
#     self.model = model

#   def move(self):
#     print("Move!")

# class Car(Vehicle):
#   pass

# class Boat(Vehicle):
#   def move(self):
#     print("Sail!")

# class Plane(Vehicle):
#   def move(self):
#     print("Fly!")

# car1 = Car("Ford", "Mustang") #Create a Car object
# boat1 = Boat("Ibiza", "Touring 20") #Create a Boat object
# plane1 = Plane("Boeing", "747") #Create a Plane object

# for x in (car1, boat1, plane1):
#   print(x.brand)
#   print(x.model)
#   x.move() 
#   print()

### ---------- ex3
# class Animal:
#     def make_sound(self):
#         pass

# class Dog(Animal):
#     def make_sound(self):
#         print("Woof!")

# class Cat(Animal):
#     def make_sound(self):
#         print("Meow!")

# # Example usage:
# animals = [Dog(), Cat()]
# for animal in animals:
#     animal.make_sound()  # Polymorphic call to make_sound
###v---ex4 --------------------
# class Payment:
#     def process_payment(self, amount):
#         raise NotImplementedError("You should implement this method.")

# class CreditCardPayment(Payment):
#     def process_payment(self, amount):
#         return f"Processing credit card payment of {amount}."

# class PayPalPayment(Payment):
#     def process_payment(self, amount):
#         return f"Processing PayPal payment of {amount}."

# # Real-life example: Processing different types of payments
# payments = [CreditCardPayment(), PayPalPayment()]

# for payment in payments:
#     print(payment.process_payment(100)) 
 


# -----------------------------------------------
# -----------------------------------------------

## examples---- Polymorphism with Duck Typing ---------------
## Python's dynamic nature allows for duck typing, where the object's type is less important than the methods it supports.

# def fly(bird):
#     bird.fly()

# class Duck:
#     def fly(self):
#         print("Duck flying")

# class Sparrow:
#     def fly(self):
#         print("Sparrow flying")

# duck = Duck()
# sparrow = Sparrow()

# fly(duck)  # Output: Duck flying
# fly(sparrow)  # Output: Sparrow flying

# -----------------------------------------------
# -----------------------------------------------

# class File:
#     def open(self):
#         raise NotImplementedError("You should implement this method.")
    
#     def close(self):
#         raise NotImplementedError("You should implement this method.")

# class TextFile(File):
#     def open(self):
#         return "Opening a text file"
    
#     def close(self):
#         return "Closing a text file"

# class ImageFile(File):
#     def open(self):
#         return "Opening an image file"
    
#     def close(self):
#         return "Closing an image file"

# class AudioFile(File):
#     def open(self):
#         return "Opening an audio file"
    
#     def close(self):
#         return "Closing an audio file"

# # Function that uses polymorphism
# def manage_file(file: File):
#     print(file.open())
#     print(file.close())

# # Creating objects of different file types
# files = [TextFile(), ImageFile(), AudioFile()]

# # Using the polymorphic function
# for file in files:
#     manage_file(file)


# -----------------------------------------------
# -----------------------------------------------


# class Car:
#   def __init__(self, brand, model):
#     self.brand = brand
#     self.model = model

#   def move(self):
#     print("Drive!")

# class Boat:
#   def __init__(self, brand, model):
#     self.brand = brand
#     self.model = model

#   def move(self):
#     print("Sail!")

# class Plane:
#   def __init__(self, brand, model):
#     self.brand = brand
#     self.model = model

#   def move(self):
#     print("Fly!")

# car1 = Car("Ford", "Mustang")       #Create a Car class
# boat1 = Boat("Ibiza", "Touring 20") #Create a Boat class
# plane1 = Plane("Boeing", "747")     #Create a Plane class

# for x in (car1, boat1, plane1):
#   x.move()

# # # ===================================================================
# # Duck Typing in Python
# # # ==================================================================
# # Duck typing is a concept where the type or class of an object is less important than the methods it defines. Using this concept, you can call any method on an object without checking its type, as long as the method exists.
# # This term is defined by a very famous quote that states: Suppose there is a bird that walks like a duck, swims like a duck, looks like a duck, and quaks like a duck then it probably is a duck

# class Duck:
#    def sound(self):
#       return "Quack, quack!"

# class AnotherBird:
#    def sound(self):
#       return "I'm similar to a duck!"

# def makeSound(duck):
#    print(duck.sound())

# # creating instances
# duck = Duck()
# anotherBird = AnotherBird()
# # calling methods
# makeSound(duck)   
# makeSound(anotherBird) 

# # # ===================================================================
# # Method Overriding in Python
# # # ==================================================================
# # In method overriding, a method defined inside a subclass has the same name as a method in its superclass but implements a different functionality.
# from abc import ABC, abstractmethod
# class shape(ABC):
#    @abstractmethod
#    def draw(self):
#       "Abstract method"
#       return

# class circle(shape):
#    def draw(self):
#       super().draw()
#       print ("Draw a circle")
#       return

# class rectangle(shape):
#    def draw(self):
#       super().draw()
#       print ("Draw a rectangle")
#       return

# shapes = [circle(), rectangle()]
# for shp in shapes:
#    shp.draw()

# # # -------ex2-------------------------
# # # Problem:
# # #     - You're building a shape calculator and want to calculate areas for different shapes (circle, rectangle, triangle).
# # # Solution:
# # #     - Create a base Shape class with an area method, and then derived classes for specific shapes that override the area method.

# import math

# class Shape:
#     def area(self):
#         pass  # Abstract method

# class Circle(Shape):
#     def __init__(self, radius):
#         self.radius = radius

#     def area(self):
#         return math.pi * self.radius**2

# class Rectangle(Shape):
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height

#     def area(self):
#         return self.width * self.height

# # Example usage:
# circle = Circle(5)
# rectangle = Rectangle(4, 3)

# print(circle.area())  # Output: 78.53981633974483
# print(rectangle.area())  # Output: 12

# # # or

# # shapes = [Circle(5),Rectangle(4, 3)]
# # for shape in shapes:
# #      print(shape.area())
# g

# # # -------ex3-------------------------
# # # Banking System with Account Interest Calculation
# # # Method overriding allows a subclass to provide a specific implementation of a method already defined in its superclass..

# class Account:
#     def __init__(self, balance):
#         self.balance = balance

#     def interest(self):
#         return self.balance * 0.02

#     def __str__(self):
#         return "Regular Account"

# class SavingsAccount(Account):
#     def interest(self):
#         return self.balance * 0.05

#     def __str__(self):
#         return "Savings Account"

# class FixedAccount(Account):
#     def interest(self):
#         return self.balance * 0.10

#     def __str__(self):
#         return "Fixed Account"

# accounts = [Account(1000), SavingsAccount(1000), FixedAccount(1000)]

# for account in accounts:
#      print(f"{account}: ${account.interest()}")

### OR  Direct access for individual accounts

# # Real-life example: Calculating interest for different account types
# account = Account(1000)
# savings_account = SavingsAccount(1000)
# fixed_account = FixedAccount(1000)

# print("Regular Account Interest:", account.interest())  # Output: 20.0
# print("Savings Account Interest:", savings_account.interest())  # Output: 50.0
# print("Fixed Account Interest:", fixed_account.interest())  # Output: 50.0




# # # ===================================================================
# #  Method Overloading in Python
# # # ==================================================================
### Python does not support traditional method overloading like other languages. However, you can achieve similar behavior using default arguments or variable-length arguments.
### 
### 

### ex1 -------------------
# class AreaCalculator:
#     def calculate_area(self, shape, *args):
#         if shape == "circle" and len(args) == 1:
#             return 3.14 * args[0] ** 2
#         elif shape == "rectangle" and len(args) == 2:
#             return args[0] * args[1]
#         elif shape == "triangle" and len(args) == 2:
#             return 0.5 * args[0] * args[1]
#         else:
#             return "Invalid shape or arguments"

# # Real-life example: Calculating area of different shapes
# calculator = AreaCalculator()

# print("Circle Area:", calculator.calculate_area("circle", 5))  # Output: 78.5
# print("Rectangle Area:", calculator.calculate_area("rectangle", 4, 5))  # Output: 20
# print("Triangle Area:", calculator.calculate_area("triangle", 3, 6))  # Output: 9

### ex2 --------------------

# def add(*nums):
#    return sum(nums)

# # Call the function with different number of parameters
# result1 = add(10, 25)
# result2 = add(10, 25, 35)

# print(result1)  
# print(result2) 


 ### ex3----------------------
### Here's an example of method overloading in Python using interest rate calculations for different types of payments: monthly, quarterly, and yearly. 
### Note that Python doesn't support method overloading directly, but you can achieve similar functionality by using default arguments or variable-length arguments

# class Payment:
#     def __init__(self, principal):
#         self.principal = principal

#     def calculate_interest(self, rate, period="yearly"):
#         if period == "yearly":
#             return self.principal * (1 + rate)
#         elif period == "quarterly":
#             return self.principal * (1 + rate / 4) ** 4
#         elif period == "monthly":
#             return self.principal * (1 + rate / 12) ** 12
#         else:
#             raise ValueError("Unsupported period. Choose 'yearly', 'quarterly', or 'monthly'.")

# # Example usage:
# principal = 1000
# annual_rate = 0.05  # 5%

# payment = Payment(principal)

# yearly_interest = payment.calculate_interest(annual_rate)
# quarterly_interest = payment.calculate_interest(annual_rate, "quarterly")
# monthly_interest = payment.calculate_interest(annual_rate, "monthly")

# print(f"Yearly Interest: ${yearly_interest:.2f}")    # Output: Yearly Interest: $1050.00
# print(f"Quarterly Interest: ${quarterly_interest:.2f}")  # Output: Quarterly Interest: $1050.95
# print(f"Monthly Interest: ${monthly_interest:.2f}")  # Output: Monthly Interest: $1051.16



 ### ex4----------------------

# def calculate_interest(principal, interest_rate, time_period, payment_frequency=None):
#   """Calculates interest based on given parameters.

#   Args:
#     principal: The initial amount.
#     interest_rate: The annual interest rate.
#     time_period: The time period in years.
#     payment_frequency: Optional, the number of payments per year.

#   Returns:
#     The calculated interest.
#   """

#   if payment_frequency is None:
#     # Simple interest calculation
#     return principal * interest_rate * time_period
#   else:
#     # Compound interest calculation
#     # Assuming annual compounding for simplicity
#     return principal * (1 + interest_rate / payment_frequency) ** (payment_frequency * time_period) - principal

# # Example usage:
# simple_interest = calculate_interest(1000, 0.05, 2)
# compound_interest = calculate_interest(1000, 0.05, 2, 12)

# print(simple_interest)  # Output: 100.0
# print(compound_interest)  # Output: 105.11627907794472


# # # # ===================================================================
# # # Overloading Operators in Python
# # # # ==================================================================
# # - Suppose you have created a Vector class to represent two-dimensional vectors, what happens when you use the plus operator to add them? Most likely Python will yell at you.
# # - You could, however, define the __add__ method in your class to perform vector addition and then the plus operator would behave as per expectation −

# class Vector:
#    def __init__(self, a, b):
#       self.a = a
#       self.b = b

#    def __str__(self):
#       return 'Vector (%d, %d)' % (self.a, self.b)
   
#    def __add__(self,other):
#       return Vector(self.a + other.a, self.b + other.b)

# v1 = Vector(2,10)
# v2 = Vector(5,-2)
# print (v1 + v2)


# # # ----ex2---------------
# # v
# h

# class Complex:
#     def __init__(self, real, imag):
#         self.real = real
#         self.imag = imag

#     def __add__(self, other):
#         return Complex(self.real + other.real, self.imag + other.imag)

#     def __sub__(self, other):
#         return Complex(self.real - other.real, self.imag - other.imag)

#     def __str__(self):
#         return f"{self.real} + {self.imag}i"

# # Real-life example: Adding and subtracting complex numbers
# c1 = Complex(3, 2)
# c2 = Complex(1, 7)

# print("Addition:", c1 + c2)  # Output: 4 + 9i
# print("Subtraction:", c1 - c2)  # Output: 2 - 5i

# ----------ex3-----------------------

# import math

# class Vector:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

#     def __add__(self, other):
#         return Vector(self.x + other.x, self.y + other.y)

#     def __sub__(self, other):
#         return Vector(self.x - other.x, self.y - other.y)

#     def magnitude(self):
#         return math.sqrt(self.x**2 + self.y**2)

# # Example usage:
# v1 = Vector(3, 4)
# v2 = Vector(1, 2)

# result_sum = v1 + v2  # Overloaded + operator
# result_difference = v1 - v2  # Overloaded - operator

# print(result_sum.x, result_sum.y)  # Output: 4 6
# print(result_difference.x, result_difference.y)  # Output: 2 2




# =======================================================================
# =======================================================================
# Summary
# These examples demonstrate different aspects of OOP in Python:
# - Operator Overloading: Allows custom behavior for operators, useful for complex number calculations.
# - Method Overriding: Allows a subclass to provide a specific implementation, useful in banking systems.
# - Method Overloading: Achieved using default or variable-length arguments, useful for area calculations.
# - Polymorphism with Inheritance: Allows a single interface to represent different underlying forms, useful in payment processing systems.