# class Circle():
#     pi=3.142
#     def __init__(self,radius=1):
#         self.radius = radius
#
#     def setRadius(self,newR):
#         self.radius = newR
#     def getRadius(self):
#         return self.radius
#
#     def area(self):
#         return self.radius * self.radius * Circle.pi
#
# myc = Circle(5)
# print("the area of radius {}, is {}".format(myc.radius,myc.area()))
#
# myc.radius=10
# print("the area of radius {}, is {}".format(myc.radius,myc.area()))
# myc.setRadius(15)
# newr=myc.getRadius()
# print("the area of radius {}, is {}".format(newr,myc.area()))
# ====================================================================================================
# class Employees:
#     name2 = "Jude"
#     destination = "Sales Executive"
#     target = 5
#     def hasMetTarget(self):
#         if(self.target>=10):
#            return "has met his target"
#         else:
#             return "has not met his target"
#
# first = Employees()
# print("{} {} {} with {} points".format(first.destination,first.name2,first.hasMetTarget(),first.target))
# second = Employees()
# second.name2="ben"
# print("{} {} {} with {} points".format(second.destination,second.name2,second.hasMetTarget(),second.target))
# print("{} {} {} with {} points".format(first.destination,first.name2,first.hasMetTarget(),first.target))
# print("{} {} {} with {} points".format(second.destination,second.name2,second.hasMetTarget(),second.target))
# Employees.name2="tony"
# print("{} {} {} with {} points".format(first.destination,first.name2,first.hasMetTarget(),first.target))
# print("{} {} {} with {} points".format(second.destination,second.name2,second.hasMetTarget(),second.target))
# first.name2 = "magidi"
# print("{} {} {} with {} points".format(first.destination,first.name2,first.hasMetTarget(),first.target))
# print("{} {} {} with {} points".format(second.destination,second.name2,second.hasMetTarget(),second.target))
# Employees.name2="tonyyyyyy"
# print("{} {} {} with {} points".format(first.destination,first.name2,first.hasMetTarget(),first.target))
# print("{} {} {} with {} points".format(second.destination,second.name2,second.hasMetTarget(),second.target))
#------------------------------------inheritance----------------------------------------------
# class vehicle:
#     def __init__(self,VIN,weight,manufacturer):
#         self.vin_number = VIN
#         self.weight = weight
#         self.manufacturer = manufacturer
#
#     def getVin(self):
#         return self.vin_number
#     def getWeight(self):
#         return elf.weight
#     def getManufacturer(self):
#         return self.manufacturer
#     def vehicleType(self):
#         pass
#
# class Car(vehicle):
#     def __init__(self, VIN, weight, manufacturer, seats):
#         self.vin_number = VIN
#         self.weight = weight
#         self.manufacturer = manufacturer
#         self.seats = seats
#     def numberOfSeats(self):
#         return self.seats
#
#     def vehicleType(self):
#         return "CAR"
#
# class Truck(vehicle):
#     def __init__(self, VIN, weight, manufacturer, capacity):
#         self.vin_number = VIN
#         self.weight = weight
#         self.manufacturer = manufacturer
#         self.capacity = capacity
#     def TruckCapacity(self):
#         return self.capacity
#
#     def vehicleType(self):
#         return "TRUCK"
#
# obj = vehicle("231200",578,"Mecedis Benz")
# print("Vin Number: {}, Weight: {}, Manufacturer: {}".format(obj.vin_number,obj.weight,obj.manufacturer))
# a = Car("ABC1",1000,"FORD",4)
# b = Car("BCD2",1000,"BMW",4)
# c = Truck("DEF3",1200,"MAN",1000)
# d = Truck("FGH4",1500,"MECEDES",1500)
# print(a.vin_number,b.numberOfSeats(),c.getManufacturer(),d.vehicleType())
# ======================================================================================================
# calling method of a class from another class
# ------------------------------------------------------------------------
# class Calc:
#     def add(self,x,y):
#         return x+y
# class displsy:
#     def disp(self):
#        return Calc.add(self,5,7)#note add() needs 3 paras
# dis=displsy()
# print("result is {}".format(dis.disp()))






# ===================================================================================================================
# ===================================================================================================================
# ========================    THE FOUR PILLARS OF OBJECT ORIENTED PROGRAMMING    ====================================
# ===================================================================================================================
# ===================================================================================================================

# ======================== instatnce attribute and class attribute ===================================================
# class Employees:
#     name2 = "Jude"
#     destination = "Sales Executive"
#     target = 5
#     def hasMetTarget(self):
#         if(self.target>=10):
#            return "has met his target"
#         else:
#             return "has not met his target"
#
# first = Employees()
# print("{} {} {} with {} points".format(first.destination,first.name2,first.hasMetTarget(),first.target))
# second = Employees()
# second.name2="ben"
# print("{} {} {} with {} points".format(second.destination,second.name2,second.hasMetTarget(),second.target))
# print("{} {} {} with {} points".format(first.destination,first.name2,first.hasMetTarget(),first.target))
# print("{} {} {} with {} points".format(second.destination,second.name2,second.hasMetTarget(),second.target))
# Employees.name2="tony"
# print("{} {} {} with {} points".format(first.destination,first.name2,first.hasMetTarget(),first.target))
# print("{} {} {} with {} points".format(second.destination,second.name2,second.hasMetTarget(),second.target))
# first.name2 = "magidi"
# print("{} {} {} with {} points".format(first.destination,first.name2,first.hasMetTarget(),first.target))
# print("{} {} {} with {} points".format(second.destination,second.name2,second.hasMetTarget(),second.target))
# Employees.name2="tonyyyyyy"
# print("{} {} {} with {} points".format(first.destination,first.name2,first.hasMetTarget(),first.target))
# print("{} {} {} with {} points".format(second.destination,second.name2,second.hasMetTarget(),second.target))

# ===============================instance methods/ static methods-=====================================================
# class employee:
#     def nameOfEmployee(self):
#         self.name="ben"
#     def printName(self):
#         print("your name is {}".format(self.name))
#     @staticmethod#denoting welcomMsg() is a static method and doesnot take any parameter
#     def welcomMsg():
#         print("u re welcome")
# obj=employee()
# obj.nameOfEmployee()#must be defined before instance attributes re used
# obj.printName()
# print("my name is ",obj.name)
# obj.welcomMsg()

# ===================================  __init__(self)===========================================
# init method is for initializing and not necessarily defined it befor used
# class employee:
#     def __init__(self):
#         self.name="ben"
#     def printName(self):
#         print("your name is {}".format(self.name))
#     @staticmethod#denoting welcomMsg() is a static method and doesnot take any parameter
#     def welcomMsg():
#         print("u re welcome")
# obj=employee()
# # obj.nameOfEmployee()#must be defined before instance attributes re used
# obj.printName()
# print("my name is ",obj.name)
# obj.welcomMsg()
# --------------------------------------------------------------------------------------------------------
# class employee:
#     def __init__(self, name,dob):
#         self.name=name
#         self.age=2018-dob
#     def printInfo(self):
#         print("{} is {} years old".format(self.name,self.age))
#     def printInfo2(self):
#         return "{} is {} years old".format(self.name,self.age)
#     def printName(self):
#         return self.name
#     def printAge(self):
#         return self.age
# person1 = employee("Tony1",1980)
# person2 = employee("Tony2",1980)
# person3 = employee("Tony3",1980)
# person4 = employee("Tony4",1980)
# print("{} is {} years old".format(person1.name,person1.age))
# person2.printInfo()
# print(person3.printInfo2())
# print("{} is {} years old".format(person4.printName(),person4.printAge()))
# ======================================== task  ========================================================
#        Implimentation of a Library System Management
# =======================================================================================================
# (1) customer should be able to display all available books in the labrary
# (2) handle the process when a customer request a book
# (3) update the library collection when the customer returns the book
# ----------
# class library: desplay available book / to lend a book / to add a book
# class customer: request a book / return a book
# ----------------
# class library:
#     def __init__(self,listOfBook):
#         self.availableBook = listOfBook
#
#     def displayBook(self):
#         print()
#         print("AVAILABLE BOOKS")
#         for book in self.availableBook:
#             print(book)
#     def lendBook(self,requesrbook):
#         if requesrbook in self.availableBook:
#             print("you have now borrowed \"{}\"".format(requesrbook))
#             self.availableBook.remove(requesrbook)
#         else:
#             print("sorry, we dont have \"{}\" in our collection".format(requesrbook))
#     def addBook(self,returnedBook):
#         self.availableBook.append(returnedBook)
#         print("thank you for returning the book")
#
# class customer:
#     def requestBook(self):
#         print("Enter the title of the book you want to borrow")
#         self.book = input()
#         return self.book
#     def returnBook(self):
#         print("Enter the title of the book you want to return")
#         self.book = input()
#         return self.book
#
# lib=library(['The 48 Laws of Power','Arts of Seduction','Power Of The Subconscious Mind','The art of war'])
# cus=customer()
# while True:
#   print()
#   print("Enter 1 to display available books")
#   print("Enter 2 to request a book")
#   print("Enter 3 to return a book")
#   print("Enter 4 to exit")
#   userChoice=int(input())
#   if userChoice is 1:
#     lib.displayBook()
#   if userChoice is 2:
#     req=cus.requestBook()
#     lib.lendBook(req)
#   if userChoice is 3:
#     ret = cus.returnBook()
#     lib.addBook(ret)
#   if userChoice is 4:
#     exit()
# ============================IMPROVED VERSION =============================

# class library:
#     def __init__(self,listOfBook):
#         self.availableBook = listOfBook
#     #     self.allBooks = listOfBook
#     #
#     # def comparebook(self):
#     #     return self.allBooks
#
#     def displayBook(self):
#         print("    AVAILABLE BOOKS")
#         print("    ===============")
#         for book in range(len(self.availableBook)):
#             print("({}) {}".format(book+1,self.availableBook[book]))
#     def lendBook(self,requesrbook):
#         if requesrbook in self.availableBook:
#             print("you have now borrowed \"{}\"".format(requesrbook))
#             self.availableBook.remove(requesrbook)
#         else:
#             print("sorry, we dont have \"{}\" in our collection".format(requesrbook))
#     def addBook(self,returnedBook):
#         self.availableBook.append(returnedBook)
#         print("thank you for returning the book")
#
# class customer:
#     def requestBook(self):
#         print("Enter the title of the book you want to borrow")
#         self.book = input()
#         return self.book
#     def returnBook(self):
#         print("Enter the title of the book you want to return")
#         self.book = input()
#         # if self.book in library.comparebook(self):
#         return self.book
#
#
#
# lib=library(['The 48 Laws of Power','Arts of Seduction','Power Of The Subconscious Mind','The art of war'])
# cus=customer()
# while True:
#   print()
#   print("Enter 1 to display available books")
#   print("Enter 2 to request a book")
#   print("Enter 3 to return a book")
#   print("Enter 4 to exit")
#   userChoice=int(input())
#   if userChoice is 1:
#     lib.displayBook()
#   if userChoice is 2:
#     req=cus.requestBook()
#     lib.lendBook(req)
#   if userChoice is 3:
#     ret = cus.returnBook()
#     lib.addBook(ret)
#   if userChoice is 4:
#     exit()

# ================================================================================================
#                            INHERITANCE
# ================================================================================================
# class Father:
#     tribe = "Cross River"
#     sex = "male"
#     def showDetail(self):
#         return self.tribe
# class Son(Father):
#     def __init__(self):
#         self.yearOfBirth = 1980
#         self.name = "princewill"
#     def depl(self):
#         print("{} is a {} yesr old {} from {}".format(self.name,2018-self.yearOfBirth,self.sex,self.showDetail()))
# cc = Son()
# cc.depl()
# --------------------multiple inheritance -------------------------
# class operatingSystem:
#     name = "Mac OS"
#     type = "multitasking"
# class Apple:
#     website = "www.apple.com"
#     name = "Apple OS"
# class MacBook(operatingSystem,Apple):
#     def disp(self):
#          print("{} is a {} from {} ".format(self.name,self.type, self.website))
#
# hh = MacBook()
# hh.disp()
# --------------------------multilevel inheritance--------------------------uugnjcghcgchgchgchgchgcgcgcghgchubbjyvhfhybjjjjjjgvhgfhgcfgfgyfyggfhfgjfygfhgcjgcfgc
# class physics:
#     def vel(self,x,t):
#         return x/t
#     def acc(self,tt):
#       return self.vel()/tt
#
#
# class math(physics):
#     def force(self):

#
#
# class display:
#     pass
# ==============================polymorphism------------------------------------------------------------------
# class employee:
#     def setNumOfWorkingHours(self):
#         self.numOfWorkingHrs = 40
#     def display(self):
#         print("number of working hrs is {}:".format(self.numOfWorkingHrs))
#
# class trainee(employee):
#     def setNumOfWorkingHours(self):
#         self.numOfWorkingHrs = 45
#     def reserNum(self):
#         super().setNumOfWorkingHours()
#
# emp = employee()
# emp.setNumOfWorkingHours()
# emp.display()
#
# tre = trainee()
# tre.setNumOfWorkingHours()
# tre.display()
# # after reset
# tre.reserNum()
# tre.display()
# --------------------------------poly -----------------------------------------------------------------
# class A:
#     def method(self):
#         print("from A")
#
#
# class B(A):
#     def method(self):
#         print("from B")
#
#
# class C(A):
#     def method(self):
#         print("from C")
#
#
# class D(C,B):
#     pass
# ob = D()
# ob.method()
# ob.method()
# ----------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------

# class Delivery:
#     service_charge = 1.5

#     def __init__(self):
#         self.menu = {1:["coconut curry",7.50],
#                      2: ["spicy tofu", 5.50],
#                      3: ["veg noddles", 8.70]
#                      }
#         self.order = []
#     def choose_in_menu(self):
#         for i in range(1,len(self.menu)+1):
#             print(i,self.menu[i][0]+" $"+str(self.menu[i][1]))

# d=Delivery()
# d.choose_in_menu()
















