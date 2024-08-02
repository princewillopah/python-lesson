# from random import randint
# class RechargeCardsGen:
#     count = 0
#     def generatedigits(self,pindigits,n,iterationlimit):
#         self.realdigits = int(pindigits/n)
#         while self.count < iterationlimit+1:
#             self.m = '-'.join(["%d" % randint(10**(n-1), (10**n)-1) for self.num in range(0, self.realdigits)])
#             print(self.m)
#             self.count += 1
# class UserEnd:
#     def takeuserpref(self):
#         print("How many digit pin do you wish to generate? ")
#         self.userPin = int(input())
#         return self.userPin
#
#     def takeuserpref1(self):
#         print("How many digits do you want to pin divided into: ")
#         self.userDiv = int(input())
#         return self.userDiv
#
#     def iterationset(self):
#         print("How many sets of recharge card do you want to generated: ")
#         userNumber = int(input())
#         return userNumber
# newrecharge = RechargeCardsGen()
# newuser = UserEnd()
# while True:
#     print("press 1 to generate desired pin")
#     print("press 2 to quit program")
#     decision = int(input())
#
#     if decision is 1:
#         digits = newuser.takeuserpref()
#         mydivision = newuser.takeuserpref1()
#         newiteration = newuser.iterationset()
#         newrecharge.generatedigits(digits,mydivision,newiteration)
#     elif decision is 2:
#         quit()
# ===============================olu===============================
from random import randint
# import csv
import time
class RechargeCardsGen:
    count = 0
    def generatedigits(self,iterationlimit, userDigits):
        while self.count < userDigits:
            self.m = '-'.join(["%d" % randint(1000, 9999) for self.num in range(0, iterationlimit)])
            print(self.m)
            self.count += 1
class UserEnd:
    def takeuserpref(self):
        print("Press 1 to generate 12-digit")
        print("Press 2 to generate 16-digit pin")
        self.userPin = int(input())
        if self.userPin is 1:
            self.realdigit = 3
        elif self.userPin is 2:
            self.realdigit = 4
        return self.realdigit
    def iterationset(self):
        try:
            print("How many sets of recharge card do you want to generated: ")
            self.userNumber = int(input())
        except ValueError:
            print("please enter an integer.")
            print("Knucklehead")
        try:
            return self.userNumber
        except AttributeError:
            print("Int type only")
newrecharge = RechargeCardsGen()
newuser = UserEnd()
while True:
    try:
        print("press 1 to generate desired pin")
        print("press 2 to quit program")
        decision = int(input())
    except ValueError as val:
        print("you have entered a wrong Value. This input only takes integers. Hence the", val)
    try:
        if decision is 1:
            digits = newuser.takeuserpref()
            newiteration = newuser.iterationset()
            print('The time before this iteration is', time.ctime())
            newrecharge.generatedigits(digits,newiteration)
            print('This is the time after iteration:',time.ctime())
        elif decision is 2:
            quit()
    except NameError as NE:
        print("Error detected. Program will self terminate")
        print("Please try again this time with only an integer. No decimal you knucklehead")
        print(NE)
# ===========================|random|==============================
# ===============
# import random
# class RandomGenerator:
#     def __init__(self):
#         self.min_number = 0
#         self.max_number = 100
#     def getMaxNumber(self):
#         return self.max_number
#     def getMinNumber(self):
#         return self.min_number
#     # def setMaxNumber(self, maxNum):
#     #     self.max_number = maxNum
#     # def setMinNumber(self, minNum):
#     #     self.min_number = minNum
#     def getRandom(self):
#         return random.randint(self.min_number, self.max_number)
# ran = RandomGenerator()  # INITIALS ARE ALREADY GENERATED
# for i in range(5):  # print it five times
#     print(ran.getRandom(),end=" ")
# =========================recharge card ===========
# from random import randint as r
# class RechargeCard:
#     n1=r(1111,9999)
#     n2=r(1111,9999)
#     n3=r(1111,9999)
#     n4=r(1111,9999)
#     # def setFor3(self,):
#     #     pass
#     # def setFor4(self):
#     #     pass
#     def getFor3(self,num):
#        print("%d-%d-%d"%(self.n1,self.n2,self.n3))
#     # def getFor4(self):
#     #     return "%d-%d-%d-%d" % (self.n1, self.n2, self.n3,self.n4)
#     # def displayFor3(self,num):
#     #     for n in range(1,num+1):
#     #      print(self.getFor3())
#     # def displayFor4(self,num):
#     #     for n in num:
#     #      print(self.getFor4())
# obj=RechargeCard()
# obj.getFor3(5)
# # obj. displayFor3(5)
# # while True:
# #     ans = int(input("Enter 1 to generate desired pin or 2 to quit"))
# #     if ans is 1:
# #         digits = newuser.takeuserpref()
# #         mydivision = newuser.takeuserpref1()
# #         newiteration = newuser.iterationset()
# #         newrecharge.generatedigits(digits,mydivision,newiteration)
# #     elif ans is 2:
# #         quit()
# #     else:
# #         print("you entered the wrong input")
# #         quit()

# from random import randint as r
# class RechargeCard:
#     def For3(self):
#         n1 = r(1111, 9999)
#         n2 = r(1111, 9999)
#         n3 = r(1111, 9999)
#         n4 = r(1111, 9999)
#         return "%d-%d-%d"%(n1,n2,n3)
#     def For3(self):
#         n1 = r(1111, 9999)
#         n2 = r(1111, 9999)
#         n3 = r(1111, 9999)
#         n4 = r(1111, 9999)
#         return "%d-%d-%d-%d" % (n1, n2, n3,n4)
#     def displayFor3(self,num):
#         for n in range(1,num+1):
#          print(self.getFor3())
    # def displayFor4(self,num):
    #     for n in num:
    #      print(self.getFor4())
# obj=RechargeCard()

# obj.getFor3(5)
# obj. displayFor3(5)
# while True:
#     ans = int(input("Enter 1 to generate desired pin or 2 to quit"))
#     if ans is 1:
#         digits = newuser.takeuserpref()
#         mydivision = newuser.takeuserpref1()
#         newiteration = newuser.iterationset()
#         newrecharge.generatedigits(digits,mydivision,newiteration)
#     elif ans is 2:
#         quit()
#     else:
#         print("you entered the wrong input")
#         quit()

