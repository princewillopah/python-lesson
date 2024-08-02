# Inheritance allows us to define a class that inherits all the methods and properties from another class
# Parent class is the class being inherited from, also called base class.
# Child class is the class that inherits from another class, also called derived class.
# Note: 
    # - When you add the __init__() function, the child class will no longer inherit the parent's __init__() function.The child's __init__() function overrides the inheritance of the parent's __init__() function.
# Python also has a super() function that will make the child class inherit all the methods and properties from its parent:

# Summary
# Without __init__() in Child: The Parent's __init__() method is called, and the child class inherits the initialization behavior of the parent.
# With __init__() in Child: The Parent's __init__() method is overridden, and the child class does not inherit the parent's initialization behavior unless explicitly called using super().
# -------------------------------------------------------------
#  Ex1 - Parent Class Without Child __init__() Overriding
# -------------------------------------------------------------

# class Person:
#   def __init__(self, fname, lname):
#     self.firstname = fname
#     self.lastname = lname
#     self.age = 40

#   def printname(self):
#     print(self.firstname, self.lastname)

# class Student(Person): # it is not overriding the parrent class
#   pass  # here we dont want to overide anything from the parent or have anything extra

# c = Student("Mike", "Olsen")
# c.printname() # instance of the child class(Student) accessing the parent class(Person) method 
# print(f"My name is {c.firstname} {c.lastname} and i am {c.age}") # instance of the child class(Student) accessing the parent class(Person) properties  

# -------------------------------------------------------------
#  Ex1 - Parent Class With Child __init__() Overriding
# -------------------------------------------------------------
## In this example, the Child class defines its own __init__() method, which overrides the Parent class's __init__() method. When an instance of Child is created, the __init__() method of the Child class is called, and the name and school attributes are initialized. 
## However, the age attribute from the Parent class is not initialized because the Parent's __init__() method is not called.

# class Person:
#   def __init__(self, fname, lname):
#     self.firstname = fname
#     self.lastname = lname
#     self.age = 40 # since the child(Student)  used __init__() to override its parrents's, it would not have acess to this functions properties

# #   def printname(self): # since the child(Student)  used __init__() to override its parrents's, it would not have acess to this functions properties
# #     print(self.firstname, self.lastname) # this will throw error that Student has no attributes like firstname or lastname

# class Student(Person): # it is not overriding the parrent class
#     def __init__(self, fname, lname, school):
#         self.fst_name = fname
#         self.lname = lname
#         self.school = school
#         self.sex = "Female"
#         self.age = 40 

# c = Student("Mike", "Olsen", "Buku High school")
# # c.printname() # instance of the child class(Student) accessing the parent class(Person) method 
# print(f"My name is {c.fst_name} {c.lname}.\nI attend {c.school}.\nI am {c.sex} and {c.age}") 

# -------------------------------------------------------------
#  Ex3 - Parent Class Without Child __init__() Overriding
# -------------------------------------------------------------
##In this case, the Child's __init__() method calls super().__init__(name), which executes the Parent's __init__() method and initializes the name and age attributes. 
##Then, the Child's __init__() method continues and initializes the school attribute.

# class Person:
#   def __init__(self, fname, lname):
#     self.firstname = fname
#     self.lastname = lname
#     self.age = 40 # since the child(Student)  used __init__() to override its parrents's, it would not have acess to this functions properties

#   def printname(self): # since the child(Student)  used __init__() to override its parrents's, it would not have acess to this functions properties
#     print(self.firstname, self.lastname) # this will throw error that Student has no attributes like firstname or lastname

# class Student(Person): # it is not overriding the parrent class
#     def __init__(self, fname, lname, school):
#         super().__init__(fname, lname)  # Call the Parent's __init__()
#         self.fst_name = fname
#         self.lname = lname
#         self.school = school
#         self.sex = "Female"
#         self.age = 30 

# c = Student("Mike", "Olsen", "Buku High school")
# c.printname() # instance of the child class(Student) accessing the parent class(Person) method 
# print(f"My name is {c.fst_name} {c.lname}.\nI attend {c.school}.\nI am {c.sex} and {c.age}") 

# -------------------------------------------------------------
#  Ex4 - Multiple Inheritance
# -------------------------------------------------------------
# Multiple inheritance in Python allows you to construct a class based on more than one parent classes. 
# The Child class thus inherits the attributes and method from all parents. The child can override methods inherited from any parent
# class parent1:
#    #statements
   
# class parent2:
#    #statements
   
# class child(parent1, parent2):
#    #statements
# ----------------------------
# class division:
#    def __init__(self, a,b):
#       self.n=a
#       self.d=b
#    def divide(self):
#       return self.n/self.d
# class modulus:
#    def __init__(self, a,b):
#       self.n=a
#       self.d=b
#    def mod_divide(self):
#       return self.n%self.d
      
# class div_mod(division,modulus):
#    def __init__(self, a,b):
#       self.n=a
#       self.d=b
#    def div_and_mod(self):
#       divval=division.divide(self)
#       modval=modulus.mod_divide(self)
#       return (divval, modval)

# x=div_mod(10,3)
# print ("division:",x.divide())
# print ("mod_division:",x.mod_divide())
# print ("divmod:",x.div_and_mod())


# -------------------------------------------------------------
#  Ex1 - Python - Multilevel Inheritanceng
# -------------------------------------------------------------
# parent class
class Universe: 
   def universeMethod(self):
      print ("I am in the Universe")

# child class
class Earth(Universe): 
   def earthMethod(self):
      print ("I am on Earth")
      
# another child class
class India(Earth): 
   def indianMethod(self):
      print ("I am in India")      

# creating instance 
person = India()  
# method calls
person.universeMethod() 
person.earthMethod() 
person.indianMethod() 

# -------------------------------------------------------------
#  Ex1 - Python - Hierarchical Inheritance
# -------------------------------------------------------------
# parent class
class Manager: 
   def managerMethod(self):
      print ("I am the Manager")

# child class
class Employee1(Manager): 
   def employee1Method(self):
      print ("I am Employee one")
      
# second child class
class Employee2(Manager): 
   def employee2Method(self):
      print ("I am Employee two")      

# creating instances 
emp1 = Employee1()  
emp2 = Employee2()
# method calls
emp1.managerMethod() 
emp1.employee1Method()
emp2.managerMethod() 
emp2.employee2Method()  
# -------------------------------------------------------------
#  Ex1 - Python - Hybrid Inheritance
# -------------------------------------------------------------
# parent class
class CEO: 
   def ceoMethod(self):
      print ("I am the CEO")
      
class Manager(CEO): 
   def managerMethod(self):
      print ("I am the Manager")

class Employee1(Manager): 
   def employee1Method(self):
      print ("I am Employee one")
      
class Employee2(Manager, CEO): 
   def employee2Method(self):
      print ("I am Employee two")      

# creating instances 
emp = Employee2()
# method calls
emp.managerMethod() 
emp.ceoMethod()
emp.employee2Method()

# -------------------------------------------------------------
#  Ex1 - Parent Class Without Child __init__() Overriding
# -------------------------------------------------------------


# -------------------------------------------------------------
#  Ex1 - Parent Class Without Child __init__() Overriding
# -------------------------------------------------------------









# class Person:
#   def __init__(self, fname, lname):
#     self.firstname = fname
#     self.lastname = lname

#   def printname(self):
#     print(self.firstname, self.lastname)

# class Student(Person):
#   def __init__(self, fname, lname):
#     Person.__init__(self, fname, lname)

# x = Student("Mike", "Olsen")
# x.printname()


# class Person:
#   def __init__(self, fname, lname):
#     self.firstname = fname
#     self.lastname = lname

#   def printname(self):
#     print(self.firstname, self.lastname)

# class Student(Person):
#   def __init__(self, fname, lname):
#     super().__init__(fname, lname)
#     self.graduationyear = 2019

# x = Student("Mike", "Olsen")
# print(x.graduationyear)


# class Person:
#   def __init__(self, fname, lname):
#     self.firstname = fname
#     self.lastname = lname

#   def printname(self):
#     print(self.firstname, self.lastname)

# class Student(Person):
#   def __init__(self, fname, lname, year):
#     super().__init__(fname, lname)
#     self.graduationyear = year

# x = Student("Mike", "Olsen", 2019)
# print(x.graduationyear)






