# class Student:
#     grades=[]
#     def __init__(self,name,id):
#         self.name=name
#         self.id=id
#     def addGrade(self,grade):
#         self.grades.append(grade)
#     def showGrade(self):
#         grd=""
#         for g in self.grades:
#             grd=grd+str(g)+" "
#         return grd
#     # def show(self):
#     #     for g in self.grades:
#     #         print(g,end=" ")
#     def studentInfo(self):
#         return "Name: %s \nId: %s\nGrades: %s"%(self.name,self.id,self.showGrade())
#     def average(self):
#         total=0
#         for each_grade in self.grades:
#             total=total+each_grade
#         return "Average: %.2f"%(total/len(self.grades))
#
#
# stu=Student("james","123")
# stu.addGrade(87)
# stu.addGrade(67)
# stu.addGrade(34)
# print(stu.showGrade())
# print(stu.studentInfo())
# print(stu.average())
# ===========================pin card===================================
# import time
# from random import randint as r
# class RechargeCard:
#     def randi(self):
#         return r(1111, 9999)
#     def currenttime(self):
#         return time.time()
#     def totalTime(self,stat,end):
#         diff=int(end-stat)
#         sec = int(diff % 60)
#         min = int(diff / 60)
#         print("Total time taken:  %s(min):%s(sec)" % (str(min), str(sec).zfill(2)))
#
#     def For3(self,num):
#         if num is 1:
#             return "%d-%d-%d-%d"%(self.randi(),self.randi(),self.randi(),self.randi())
#         elif num is 2:
#             return "%d-%d-%d" % (self.randi(),self.randi(), self.randi())
#     def displayFor3(self, num):
#         try:
#            c=0
#            amount=int(input("how many card to print: "))
#            start=self.currenttime()
#         except:
#             print("Enter only integers")
#         else:
#             for n in range(1, amount + 1):
#                print(self.For3(num))
#                c+=1
#             end = self.currenttime()
#             print("Total pin(s) printed: %d"%c)
#             self.totalTime(start,end)
#             print("")
#
# obj = RechargeCard()
# while True:
#     try:
#         ans1 = int(input("Enter 1 to generate desired pin or 2 to quit: "))
#     except ValueError:
#         print("plzzzzzz,just enter 1 or 2, mr OLU")
#     else:#exception else
#         if ans1 is 1:
#             try:
#               ans2 = int(input("Enter 1 for 16-pin or 2 for 12-pin: "))
#             except:
#               print("i saiiiiiid,just enter 1 or 2, mr Taiwo")
#               # ans2 = int(input("Enter 1 for 16-pin or 2 for 12-pin: "))
#             else:  # sub exception else
#               obj.displayFor3(ans2)
#         elif ans1 is 2:
#             print("bye")
#             quit()
#         else:
#             print("you entered the wrong input")
#             quit()
# ==================== ABSTRACTION AND INHERITANC==========================
#          PROBLEM STATEMENT
# 1. implementing a library management system with the following tasks:
#     (a)the customer should be able to display all th books available in the library
#     (b) handle the process when a customer request to borrow a book
#     (c) update the library collection when a customer returns a book

# class Library:
#     def __init__(self,avaBook):
#         self.availableBooks=avaBook
#     def displayAvailableBooks(self):
#         print("-----------------------------------")
#         print("          Available Books")
#         print("-----------------------------------")
#         c=1
#         for bk in self.availableBooks:
#             print("(%d) %s"%(c,bk))
#             c+=1
#     def lendBook(self,requestedBook):
#         if requestedBook in self.availableBooks:
#             print("You have now borrowed the book")
#             self.availableBooks.remove(requestedBook)
#         else:
#             print("This book is not available")
#     def addBook(self,requestedBook):
#         self.availableBooks.append(requestedBook)
#         print("You have now returned the book")
#
# class Customer:
#     def requestBook(self):
#        print("Enter the name of books you wanna borrow")
#        self.book=input()
#        return self.book
#     def returnBook(self):
#         print("Enter the name of books you wanna return")
#         self.book = input()
#         # if self.book in
#         return self.book
#
# lib=Library(["The Mafia Manager","48 Laws of Power","Art of Seduction","Art of War"])
# cus=Customer()
# admin=int(input("Enter 1 for MANAGER or 2 for STAFF: "))
# if admin==1:
#     password = input("Enter password: ")
#     if password=="prince":
#         print("You are welcome, boss")
#     else:
#         print("You are a very big Thief")
#     quit()
# elif admin==2:
#     while True:
#         print()
#         print("Enter 1 to display the available books: ")
#         print("Enter 2 to request a books: ")
#         print("Enter 3 to return books: ")
#         print("Enter 4 to exit ")
#
#         userChoice = int(input())
#         if userChoice is 1:
#             lib.displayAvailableBooks()
#         elif userChoice is 2:
#             reqBook = cus.requestBook()
#             lib.lendBook(reqBook)
#         elif userChoice is 3:
#             retBook = cus.returnBook()
#             lib.addBook(retBook)
#         elif userChoice is 4:
#             print("Thank you. Good Buy")
#             quit()
#         else:
#             print("You entered a wrong input")

#
# ========================= SIMULATE A BANKING SYSTEM ===============================
#                          Problem statement
# (1) Give a prompt to the user asking if they wish to create a new Savings Account or access  an existing one
# (2) If the user would like to create a new account, accept their name and initial deposit, and create
#     a 5 digit random number and make it as the account number of their new Savings Account
# (3) if they are accessing an existing account, accept their name and account number to
#     validate the user, and give them options to withdraw, deposit or display their available balance

# from abc import ABCMeta,abstractmethod
# from random import randint
# class Account(metaclass=ABCMeta):
#     @abstractmethod
#     def createAccount():
#         return 0
#
#     @abstractmethod
#     def authenticate():
#         return 0
#
#     @abstractmethod
#     def withdraw():
#         return 0
#
#     @abstractmethod
#     def deposit():
#         return 0
#
#     @abstractmethod
#     def displayBalance():
#         return 0
#
# class SavingsAccount(Account):
#     def __init__(self):
#         self.savingsAccount={}
#     def createAccount(self, name, initialDeposit):
#         self.accountNumber=randint(10000, 99999)
#         self.savingsAccount[self.accountNumber]=[name,initialDeposit]
#     def authenticate(self, name, accountNumber):
#         pass
#     def withdraw(self, withdrawalAmount):
#         pass
#     def deposit(self, name, initialDeposit):
#         pass
#     def displayBalance(self):
#         pass