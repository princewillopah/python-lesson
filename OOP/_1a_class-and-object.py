# ---------------ex 1 -

# class MyClass:
#   x = 5

# p1 = MyClass()
# print(p1.x)

# -----ex 2--------------------
# class Person:
#   def __init__(self, name, age):
#     self.name = name
#     self.age = age

# p1 = Person("John", 36)

# print(p1.name)
# print(p1.age)
# ----ex 3------------------
# class Person:
#   def __init__(self, name, age):
#     self.name = name
#     self.age = age

#   def __str__(self):
#     return f"{self.name}({self.age})"

# p1 = Person("John", 36)

# print(p1)

# ------ex 4 ------------------
## Objects can also contain methods. Methods in objects are functions that belong to the object

# class Person:
#   def __init__(self, name, age):
#     self.name = name
#     self.age = age

#   def myfunc(self):
#     print(f"Hello my name is {self.name} and i am {self.age} years old")

# p1 = Person("John", 36)
# p2 = Person("Tony", 20)
# p1.myfunc()
# p2.myfunc()

# ------ex 5 ------------------
### Use the words mysillyobject and abc instead of self:
# class Person:
#   def __init__(mysillyobject, name, age): # here mysillyobject acts as self
#     mysillyobject.name = name
#     mysillyobject.age = age

#   def myfunc(abc): #HERE abc acts as self
#     print("Hello my name is " + abc.name)

# p1 = Person("John", 36)
# p1.myfunc()


# ------ex 6 ------------------
# # You can modify properties on objects like this
# p1.age = 40
# # Delete the age property from the p1 object:
# del p1.age
# # You can delete objects by using the del keyword
# del p1
# ------ex 7 ------------------
## class definitions cannot be empty, but if you for some reason have a class definition with no content, put in the pass statement to avoid getting an error.

# class Person:
#   pass
# ------ex 4 ------------------
class Circle():
    pi=3.142
    def __init__(self,radius=1):
        self.radius = radius

    def setRadius(self,newR):
        self.radius = newR
    def getRadius(self):
        return self.radius

    def area(self):
        return self.radius * self.radius * Circle.pi

myc = Circle(5)
print("the area of radius {}, is {}".format(myc.radius,myc.area()))

myc.radius=10
print("the area of radius {}, is {}".format(myc.radius,myc.area()))
myc.setRadius(15)
newr=myc.getRadius()
print("the area of radius {}, is {}".format(newr,myc.area()))

# ------ex 4 ------------------

# ------ex 4 ------------------

# ------ex 4 ------------------

# ------ex 4 ------------------
# ------ex 4 ------------------
# ------ex 4 ------------------
# ------ex 4 ------------------
# ------ex 4 ------------------
# ------ex 4 ------------------
# ------ex 4 ------------------
# ------ex 4 ------------------
# ------ex 4 ------------------
# ------ex 4 ------------------

# ------ex 4 ------------------
# ------ex 4 ------------------
# ------ex 4 ------------------
# ------ex 4 ------------------
# ------ex 4 ------------------
# ------ex 4 ------------------
# ------ex 4 ------------------


# ------ex 4 ------------------
# ------ex 4 ------------------
# ------ex 4 ------------------
# ------ex 4 ------------------
# ------ex 4 ------------------


# ============================================================
# Points
# ============================================================

# - All classes have a function called __init__(), which is always executed when the class is being initiated. ex 1
# - Use the __init__() function to assign values to object properties, or other operations that are necessary to do when the object is being created ex 2
# - The __init__() function is called automatically every time the class is being used to create a new object - ex 2
# - The __str__() function controls what should be returned when the class object is represented as a string - ex 3
# - Objects can also contain methods. Methods in objects are functions that belong to the object - ex 4
# - The self parameter is a reference to the current instance of the class, and is used to access variables that belongs to the class
#       However,It does not have to be named self , you can call it whatever you like, but it has to be the first parameter of any function in the class - ex 5
# - make modofications 
# - class definitions cannot be empty, but if you for some reason have a class definition with no content, put in the pass statement to avoid getting an error. - ex 7

# ----------------------------------------------
# EXAMPLES:
# --------------------------------------

# class Employee:
#    "Common base class for all employees"
#    empCount = 0

#    def __init__(self, name, salary):
#       self.name = name
#       self.salary = salary
#       Employee.empCount += 1  # whenever this class is call, this get incremented - The __init__() function is called automatically every time the class is being used to create a new object
   
#    def displayCount(self):
#      print ("Total Employee %d" % Employee.empCount)

#    def displayEmployee(self):
#       print ("Name : ", self.name,  ", Salary: ", self.salary)

# # This would create first object of Employee class
# emp1 = Employee("Zara", 2000)
# # This would create second object of Employee class
# emp2 = Employee("Paul", 5000)
# emp3 = Employee("Tuna", 7000)
# emp4 = Employee("Grace", 5500)
# emp1.displayEmployee()
# emp2.displayEmployee()
# emp3.displayEmployee()
# emp4.displayEmployee()
# print ("Total Employee %d" % Employee.empCount) 

# -------------------

class Employee:
   # class attribute    
   empCount = 0
   def __init__(self, name, age):
      self.__name = name
      self.__age = age
      # modifying class attribute
      Employee.empCount += 1
      print ("Name:", self.__name, ", Age: ", self.__age)
      # accessing class attribute
      print ("Employee Count:", Employee.empCount)

e1 = Employee("Bhavana", 24)
print()
e2 = Employee("Rajesh", 26)
print()
Employee("xxx", 77) # you are calling them with arguments
print()

