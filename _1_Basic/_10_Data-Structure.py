# fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
# fruits.reverse()
# print(fruits)
# fruits.append('grape')
# print(fruits)
# fruits.sort()
# print(fruits)
# fruits.pop()
# print(fruits)
# fruits.insert(2,"grape")
# print(fruits)
# fruits.remove("kiwi")
# print(fruits)
# print(fruits.count("apple"))
# fruits.clear()
# ----------------------------------list compreehension-----------------------------------------
# x=[1,2,3,4,5]
# # sqr_x=[]
# # for n in x:
# #     sqr_x.append(n**2)
# # print(sqr_x)
# #
# sqr_xx=[n**3 for n in x]
# print(sqr_xx)
#
# a = [z**2 for z in range(10) if z>4]
# print(a)
#
# for z in range(10):
#     if z>4:
#         print(z**2,end=" ")
# =------------------------------------
# arr = [2,10,23,45,50,69,70]
# a=[x+1 if x>=50 else x+5 for x in arr]
# print(a)
# ar2=[]
# for x in arr:
#     if x>=50:
#         re=x+1
#     else:
#         re = x+5
#     ar2.append(re)
# print(ar2)
# ----------------------------------
## move=list(range(0,100))
#  move=[67,40,68,90,34,100,67,23,56,40,80,123]
#  move2=[]
#  for x in move:
#     if x<40:
#         re="Failed"
#     elif x>=40 and x<50:
#         re="Pass"
#     elif x>=50 and x<60:
#         re="Credit"
#     elif x>=60 and x<70:
#         re="Good"
#     elif x>=70 and x<=100:
#         re="Excellent"
#     else:
#         re="Mistake"
#     move2.append(re)
# print(move)
# print(move2)
# b=["Failed" if x<40 else "Pass" if x>=40 and x<50 else "Credit" if x>=50 and x<60 else "Good" if x>=60 and x<70 else "Excellent" if x>=70 and x<=100 else "Mistake" for x in move]
# print(b)


# -----------------------------------------------------------------------------------------------
