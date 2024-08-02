print()
print()
print()
print()



# def justPrint():
#     print("i am a function")
# justPrint()
# --------------------------------------------------------------
# def just(n):
#     print(n);
# just("i am from just")
# --------------------------------------------------------------
# def basicOp(n1,n2):
#     print("{} + {} = {}".format(n1,n2,(n1+n2)))
#     print("{} - {} = {}".format(n1, n2, (n1 - n2)))
#     print("{} x {} = {}".format(n1, n2, (n1 * n2)))
#     print("{} / {} = {}".format(n1, n2, (n1 / n2)))
# basicOp(20,5)
# basicOp(2,5)
# ---------------------------------------------------------------
# def simple(p,t):
#     amount = 0
#     print("{0:5} {1:9} {2:6}".format("month","principal","amount"))
#     for i in range(1, t+1):
#         interest = p * 0.05 * t
#         amount =amount + p + interest
#         print("({0:1}) {1:9}  {2:8}".format(i, interest, amount))

# pp=int(input("Enter Principal: "))
# tt=int(input("Enter Number of Month: "))
# simple(pp,tt)
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
# greet()
# greet("john","grace")
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
# ------------ list comprehension ---------------------------
# myy = [n**2 for n in range(1,26)]
# print(myy)
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
















