# Methods belongs to an object of a class and used to perform specific operations. 
# We have:
#     - class method:  
#         - this is a method that is bound to the class and not to the instance of the class
#         - It can be called on the class itself, rather than on an instance of the class
#         - There are two ways to create class methods in Python:
#             - Using classmethod() Function
#             - Using @classmethod Decorator
#     - instance 
#         - method: instance method can access the instance variables of the an object
#         - It can also access the class variable as it is common to all the objects
#     - static method: 
#         -  In Python, a static method is a type of method that does not require any instance to be called. 
#         -  It is very similar to the class method but the difference is that the static method doesn't have a mandatory argument like reference to the object − self or reference to the class − cls
#         - Static methods are used to access static fields of a given class. They cannot modify the state of a class since they are bound to the class, not instance.
#         - It can be called on the class itself
#         - static methods do not have access to the "cls" parameter and therefore it cannot modify the class state.
#         - There are two ways to create Python static methods:
                # - Using staticmethod() Function
                # - Using @staticmethod Decorator

# -----------------------
#  classmethod
# ----------------------
# class Employee:
#     empCount = 0
#     def __init__(self, name, age):
#       self.__name = name
#       self.__age = age
#       Employee.empCount += 1

#     def showcount(self):
#       print (f"From showcount: {self.empCount}")
      
#     counter = classmethod(showcount) # class method and can not be acceesed by instance of a class

#     @classmethod
#     def showcount2(cls):  # class method and can not be acceesed by instance of a class
#         print (f"From showcount2: {cls.empCount}")

#     @classmethod  # class method and can not be acceesed by instance of a class
#     def newemployee(cls, name, age):
#         return cls(name, age)

# e1 = Employee("Bhavana", 24)
# e2 = Employee("Rajesh", 26)
# e3 = Employee("John", 27)
# e4 = Employee.newemployee("Anil", 21)


# e1.showcount()
# Employee.counter()
# Employee.showcount2()

# -----------------------
# class Cloth:
   
#    price = 4000 # Class attribute

#    @classmethod
#    def showPrice(cls):
#       return cls.price
# # Accessing class attribute
# ex = Cloth()
# print(Cloth.showPrice())
# print(ex.showPrice())

# -----------------------
#  static method 
# ----------------------
# - Since a static method cannot access class attributes, it can be used as a utility function to perform frequently re-used tasks.
# - We can invoke this method using the class name. Hence, it eliminates the dependency on the instances.
# - A static method is always predictable as its behavior remain unchanged regardless of the class state.
# - We can declare a method as a static method to prevent overriding.

# class Employee:
#    empCount = 0
#    stdCount = 0
#    def __init__(self, name, age):
#       self.__name = name
#       self.__age = age
#       Employee.empCount += 1
#       Employee.stdCount += 2
   
#    # creating staticmethod
#    def showcount():
#       print (f"From showcount: {Employee.empCount}")
#       return
#    counter = staticmethod(showcount)

#    @staticmethod
#    def showcount2():
#         print (f"From showcount2: {Employee.stdCount}")



# e1 = Employee("Bhavana", 24)
# e2 = Employee("Rajesh", 26)
# e3 = Employee("John", 27)

# e1.counter()
# Employee.counter()

# Employee.showcount2()


# -----------------------------------------------------------------------------------------------------------
#  constructor 
# ---------------------------------------------------------------------------------------------------------
## Python constructor is an instance method in a class, that is automatically called whenever a new object of the class is created. 
## The constructor's role is to assign value to instance variables as soon as the object is declared@

# def __init__(self, parameters):
#initialize instance variables


class Employee:
    def __init__(self, sex, name="Bhavana", age=24, status=None):
        self.name = name
        self.age = age
        self.sex = sex  # this must be first since it has no defult value
        self.address = "Nigrian" # this need not be supplied
        if status:
            self.status = status
        else:
            self.status = "Unknown"  # or any default value you prefer

e1 = Employee("Female") # "Female" is for sex since sex has no default value | this can be expressed as Employee(sex = "Female")
e2 = Employee("Female", "Adanma", 30,"Single") #"Female" is for sex & it is compulsory since sex has no default value | "Adanma" is for name |  30 is for age | this can be wrinten as Employee(sex = "Female",name = "Adanma", age = 30)

print(f"Name: {e1.name}\nAge: {e1.age}\nSex: {e1.sex}\nAddress: {e1.address}\nStatus: {e1.status}")
print()
print(f"Name: {e2.name}\nAge: {e2.age}\nSex: {e2.sex}\nAddress: {e2.address}\nStatus: {e2.status}")

# ---------------------------------------------------------------------------------------------------------------------------------------------------------------
#  Access Modifier
# ---------------------------------------------------------------------------------------------------------------------------------------------------------------

# The Python access modifiers are used to restrict access to class members (i.e., variables and methods) from outside the class. 
      # Public members − A class member is said to be public if it can be accessed from anywhere in the program.
      # Protected members − They are accessible from within the class as well as by classes derived from that class.
      # Private members − They can be accessed from within the class only.
# Unlike C++ and Java, Python does not use the Public, Protected and Private keywords to specify the type of access modifiers. 
# By default, all the variables and methods in a Python class are public.
      # To indicate that an instance variable is private, prefix it with double underscore (such as "__age").
      # To imply that a certain instance variable is protected, prefix it with single underscore (such as "_salary").


### Example of Public members ################
# class Employee:
#    'Common base class for all employees'
#    def __init__(self, name="Bhavana", age=24):
#       self.name = name
#       self.age = age

# e1 = Employee()
# e2 = Employee("Bharat", 25)

# print ("Name: {}".format(e1.name))
# print ("age: {}".format(e1.age))
# print ("Name: {}".format(e2.name))
# print ("age: {}".format(e2.age))

# ------------------------
### Example of protected and private members ################
# class Employee:
#    def __init__(self, name, age, salary):
#       self.name = name # public variable
#       self.__age = age # private variable
#       self._salary = salary # protected variable
#    def displayEmployee(self):
#       print ("Name : ", self.name, ", age: ", self.__age, ", salary: ", self._salary)

# e1=Employee("Bhavana", 24, 10000)

# print (e1.name)
# print (e1._salary) # although this is protected, it will NOT fail
# print (e1.__age) # thi sis private and it will fail


# ---------Getters and Setter Methods---------------
# A getter method retrieves the value of an instance variable, usually named as get_varname, whereas 
# the setter method assigns value to an instance variable − named as set_varname.

### Example of protected and private members ################
# class Employee:
#    def __init__(self, name, age):
#       self.__name = name
#       self.__age = age

#    def get_name(self):
#       return self.__name
#    def get_age(self):
#       return self.__age
#    def set_name(self, name):
#       self.__name = name
#       return
#    def set_age(self, age):
#       self.__age=age

# e1=Employee("Bhavana", 24)
# print ("Name:", e1.get_name(), "age:", e1.get_age())
# e1.set_name("Archana")
# e1.set_age(21)
# print ("Name:", e1.get_name(), "age:", e1.get_age())

# -------------------
# class Employee:
#    def __init__(self, name, age):
#       self.__name = name
#       self.__age = age

#    def get_name(self):
#       return self.__name
#    def get_age(self):
#       return self.__age
#    def set_name(self, name):
#       self.__name = name
#       return
#    def set_age(self, age):
#       self.__age=age
#       return
#    name = property(get_name, set_name, "name") # if we want to use name instead of get_name() or set_name() as the previous example above
#    age = property(get_age, set_age, "age") # if we want to use name instead of get_name() or set_name() as the previous example above

# e1=Employee("Bhavana", 24)
# print ("Name:", e1.name, "age:", e1.age)

# e1.name = "Archana"
# e1.age = 23
# print ("Name:", e1.name, "age:", e1.age)




