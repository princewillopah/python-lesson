# # Lists are used to store multiple items in a single variable.
# # The list is changeable, meaning that we can change, add, and remove items in a list after it has been created
# # Since lists are indexed, lists can have items with the same value //["apple", "banana", "cherry", "apple", "cherry"]
# # List items can be of any data type:
# #         list1 = ["apple", "banana", "cherry"]
# #         list2 = [1, 5, 7, 9, 3]
# #         list3 = [True, False, False]
# # A list can contain different data types # list1 = ["abc", 34, True, 40, "male"]
# # It is also possible to use the list() constructor when creating a new list:
# #            thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
# # -----------------------------------------------------------------------------------------------------------
# #  ACCESSING ITEMS OF THE LIST
# # -----------------------------------------------------------------------------------------------------------
# # we could use list[first-index:end-index]
# # Note: The search will start at first-index (included) and end at end-index  (not included)
# # Note: for nagative indexes, list[-first-index:-end-index], The search will start at first-index (included) and end-index (included), from the very last index of the list
# thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
# print(f" thislist => {thislist}") # ['apple', 'banana', 'cherry', 'orange', 'kiwi', 'melon', 'mango']
# print(f" thislist[:] => {thislist[:]}") # ['apple', 'banana', 'cherry', 'orange', 'kiwi', 'melon', 'mango']
# print(f" thislist[2] => {thislist[2]}") # cherry
# print(f" thislist[:5] => {thislist[:5]}") # ['apple', 'banana', 'cherry', 'orange', 'kiwi']
# print(f" thislist[2:] => {thislist[2:]}") # ['cherry', 'orange', 'kiwi', 'melon', 'mango']
# print(f" thislist[2:5] => {thislist[2:5]}") # ['cherry', 'orange', 'kiwi']
# print(f" thislist[-4:-1] => {thislist[-4:-1]}") #  ['orange', 'kiwi', 'melon']
#
# # print(f" thislist[:] => {thislist[:]}")
# # print(f" thislist[:] => {thislist[:]}")
# # -----------------------------------------------------------------------------------------------------------
# # OTHER VERY IMPORTANT USECASES
# # -----------------------------------------------------------------------------------------------------------
# # ____________ Check if Item Exists _________________________
# # thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
# if "apple" in thislist:
#   print("Yes, 'apple' is in the fruits list") # Yes, 'apple' is in the fruits list
#
#
# # -----------------------------------------------------------------------------------------------------------
# # UPDATE LIST
# # -----------------------------------------------------------------------------------------------------------
# # thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
# thislist[4] = "grapes"
# print(thislist) # ['apple', 'banana', 'cherry', 'orange', 'grapes', 'melon', 'mango']
# # ---------------
# # thislist = ["apple", "banana", "cherry", "orange", "grapes", "mango"]
# thislist[1:3] = ["blackcurrant", "watermelon"]
# print(thislist) # ['apple', 'blackcurrant', 'watermelon', 'orange', 'grapes', 'melon', 'mango']
# # --------------------------------
# # If you insert more items than you replace, the new items will be inserted where you specified, and the remaining items will move accordingly:
# # thislist = ['apple', 'blackcurrant', 'watermelon', 'orange', 'grapes', 'melon', 'mango']
# thislist[1:3] = ["blueberries", "banana","kiwi","carrot"] # you specified that you wanna change just 2 items thislist[1:3] i.e 'blackcurrant', 'watermelon' but you brought 4 replacement. the 4 will be added and shift the other to next index
# print(thislist) #['apple', 'blueberries', 'banana', 'kiwi', 'carrot', 'orange', 'grapes', 'melon', 'mango']
# # ----------------------------
# # If you insert less items than you replace, the new items will be inserted where you specified, and the remaining items will move accordingly:
# # thislist = ['apple', 'blueberries', 'banana', 'kiwi', 'carrot', 'orange', 'grapes', 'melon', 'mango']
# thislist[1:3] = ["watermelon"] # you specified you want to replace 'blueberries', 'banana', but you only provided an item instead of 2, the second item you wanted to replace will be removed from the list
# print(thislist) #['apple', 'watermelon', 'kiwi', 'carrot', 'orange', 'grapes', 'melon', 'mango']
# # ----------------
# # thislist = ['apple', 'watermelon', 'kiwi', 'carrot', 'orange', 'grapes', 'melon', 'mango']
# # use insert() function to place an element in a particular position
# thislist.insert(2, "green pear") # put it in index 3
# print(thislist) #['apple', 'watermelon', 'green pear', 'kiwi', 'carrot', 'orange', 'grapes', 'melon', 'mango']
#

# # -----------------------------------------------------------------------------------------------------------
# # More on addition to list
# # -----------------------------------------------------------------------------------------------------------
# # append() method add an item to the end of the list
# # insert() method insert a list item at a specified index
# # extend() method append elements from another list to the current list
# # The extend() method does not have to append lists you can add any iterable object (tuples, sets, dictionaries etc.).
# # examples
# thislist = ["apple", "banana", "cherry"]
# thislist.append("orange")
# print(thislist) #["apple", "banana", "cherry", "orange"]
# # -----------
# thislist = ["apple", "banana", "cherry"]
# thislist.insert(2, "orange")
# print(thislist) #["apple", "banana", "orange", "cherry"]
# # --------------
# thislist = ["apple", "banana", "cherry"]
# tropical = ["mango", "pineapple", "papaya"]
# thislist.extend(tropical)
# print(thislist) # ["apple", "banana", "cherry","mango", "pineapple", "papaya"]
# # --------------
# # The extend() method does not have to append lists, you can add any iterable object (tuples, sets, dictionaries etc.).
# thislist = ["apple", "banana", "cherry"]
# thistuple = ("kiwi", "orange")
# thislist.extend(thistuple)
# print(thislist) #  ['apple', 'banana', 'cherry', 'kiwi', 'orange']


# -----------------------------------------------------------------------------------------------------------
#  index() || copy() || count() || list()
# -----------------------------------------------------------------------------------------------------------

# The count() method returns the number of times an elements occures in a list.
points = [1, 4, 2, 9, 7, 8, 9, 3, 1]
x = points.count(9)
print(x) # 2 that is, 9 occurs twice

# --------------------------
# The index() method returns the position at the first occurrence of the specified value.
fruits = [4, 55, 64, 32, 16, 32]
x = fruits.index(32)
print(x) # 3

# -----------------------------------------
# he copy() method returns a copy of the specified list.
fruits = ["apple", "banana", "cherry"]
x = fruits.copy()
print(x) # ["apple", "banana", "cherry"]
# -----------------------------------------
# Make a copy of a list with the list() method:
thislist = ["apple", "banana", "cherry"]
mylist = list(thislist)
print(mylist)



# -----------------------------------------------------------------------------------------------------------
#  REMOVE ITEMS FROM LIST
# -----------------------------------------------------------------------------------------------------------
# The remove() method removes the specified item.
# The pop() method removes the specified index. If you do not specify the index, the pop() method removes the last item.
# The del keyword also removes the specified index: it can also Delete the entire list
# The clear() method empties the list.  The list still remains, but it has no content.
# # examples:
# thislist = ["apple", "banana", "cherry"]
# thislist.remove("banana") # if the item you want to remove is not in the list, this throws an error. this find it first before removal
# print(thislist) #  ["apple",  "cherry"]
# -------
# thislist = ["apple", "banana", "cherry"]
# thislist.pop(1)
# print(thislist)# ["apple",  "cherry"]
# # -------------------------------
# thislist = ["apple", "banana", "cherry"]
# thislist.pop()
# print(thislist)#['apple', 'banana']
# # -----------------
# thislist = ["apple", "banana", "cherry"]
# del thislist[1]
# print(thislist)#['apple', 'cherry']
# --------------------------
# thislist = ["apple", "banana", "cherry"]
# del thislist
# print(thislist) #NameError: name 'thislist' is not defined
# ------------------
# thislist = ["apple", "banana", "cherry"]
# thislist.clear()
# print(thislist) #[]
# -----------------------------------------------------------------------------------------------------------
#  LOOP THROUGH LIST
# -----------------------------------------------------------------------------------------------------------
# for x in ['apple', 'watermelon', 'green pear', 'kiwi', 'carrot', 'orange', 'grapes', 'melon', 'mango']:
#     print(x)
# OR
# thislist = ['apple', 'watermelon', 'green pear', 'kiwi', 'carrot', 'orange', 'grapes', 'melon', 'mango']
# for x in thislist:
#   print(x)
# # -------------
# thislist = ["apple", "banana", "cherry"]
# for i in range(len(thislist)): # that is, for x in range(3) i.e for x in [0, 1, 2]
#   print(thislist[i])
# -------------loop through a list of turple -----------------
# gradebook = [('Math 212', 'Linear Algebra', 'Fall 2012', 'B'),
#              ('CS 130', 'Python', 'Spring 2013', 'A')]
# for id, name, semester, grade in gradebook:
#     print(id, name, semester, grade)
#
# for x in gradebook:
#     print( x[0], x[1])
# -----------------------------------------------------------------------------------------------------------
#  List comprehension -- it offers a shorter syntax when you want to create a new list based on the values of an existing list.
# -----------------------------------------------------------------------------------------------------------
# newlist = [expression for item in iterable if condition == True]
#     where:
#           - The condition is like a filter that only accepts the items that valuate to True. e.g if x != "apple", if "a" in x,
#           - The condition if x != "apple"  will return True for all elements other than "apple", making the new list contain all fruits except "apple".
#           - The condition is optional and can be omitted: thus you have newlist = [expression for item in iterable]
#           - The iterable can be any iterable object, like a list, tuple, set etc.
#           - You can use the range() function to create an iterable: e.g. newlist = [x for x in range(10)]
#           - The expression is the current item in the iteration, but it is also the outcome, which you can manipulate before it ends up like a list item in the new list: eg [x.upper() for x in fruits] or ['hello' for x in fruits]
#           - The expression can also contain conditions, not like a filter, but as a way to manipulate the outcome: eg [x if x != "banana" else "orange" for x in fruits] which says "Return the item if it is not banana, if it is banana return orange".

# EXAMPLES using both the normal way and the list comprehension way
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# # EXAMPLES1: Based on a list of fruits, you want a new list, containing only the fruits with the letter "e" in the name.
# fruits = ['apple', 'watermelon', 'green pear', 'kiwi', 'carrot', 'orange', 'grapes', 'melon', 'mango']
# newlist = []
# for x in fruits: # loop through each item in the list
#   if "e" in x: # if the current looped item contains "a"
#     newlist.append(x) #append it to the new list
# print(newlist) # ['apple', 'watermelon', 'green pear', 'orange', 'grapes', 'melon']
# # ---List comprehension way---------
# newlist = [x for x in fruits if "e" in x] # [ x | for x in fruits | if "e" in x] this [x] in [] represent the new list
# print(newlist) #['apple', 'watermelon', 'green pear', 'orange', 'grapes', 'melon']
# # +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# ## EXAMPLES1: Only accept items that are not "apple":
# fruits = ['apple', 'watermelon', 'green pear', 'kiwi', 'carrot', 'orange', 'grapes', 'melon', 'mango']
# newlist = []
# for x in fruits:
#     if x != "apple":
#         newlist.append(x)
# print(newlist) # ['watermelon', 'green pear', 'kiwi', 'carrot', 'orange', 'grapes', 'melon', 'mango']
# # # ---List comprehension way---------
# newlist = [x for x in fruits if x != "apple"]
# print(newlist) # ['watermelon', 'green pear', 'kiwi', 'carrot', 'orange', 'grapes', 'melon', 'mango']

# # +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# ## EXAMPLES1: produce new list without any condition":
# fruits = ['apple', 'watermelon', 'green pear', 'kiwi', 'carrot', 'orange', 'grapes', 'melon', 'mango']
# newlist = []
# for x in fruits:
#         newlist.append(x)
# print(newlist) # ['apple', 'watermelon', 'green pear', 'kiwi', 'carrot', 'orange', 'grapes', 'melon', 'mango']
# # # ---List comprehension way---------
# newlist = [x for x in fruits]
# print(newlist) # ['apple', 'watermelon', 'green pear', 'kiwi', 'carrot', 'orange', 'grapes', 'melon', 'mango']

# # +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
## EXAMPLES4: The iterable can be any iterable object, like a list, tuple, set etc.":
# mytuple = ('apple', 'watermelon', 'green pear', 'kiwi', 'carrot', 'orange', 'grapes', 'melon', 'mango')
# newlist = []
# for x in mytuple:
#         newlist.append(x)
# print(newlist) # ['apple', 'watermelon', 'green pear', 'kiwi', 'carrot', 'orange', 'grapes', 'melon', 'mango']
# # # ---List comprehension way---------
# newlist = [x for x in mytuple]
# print(newlist) # ['apple', 'watermelon', 'green pear', 'kiwi', 'carrot', 'orange', 'grapes', 'melon', 'mango']
# # +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# ## EXAMPLES4: it works with range also.":
# newlist = []
# for x in range(10):
#         newlist.append(x)
# print(newlist) # [0, 1, 2, 3, 4,5,6,7,8,9]
# # # ---List comprehension way---------
# newlist = [x for x in range(10)]
# print(newlist) # [0, 1, 2, 3, 4,5,6,7,8,9]
# # # +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# # ## EXAMPLES6: Accept only numbers lower than 5:
# newlist = []
# for x in range(10):
#     if x < 5:
#         newlist.append(x)
# print(newlist) # [0, 1, 2, 3, 4]
# # # ---List comprehension way---------
# newlist = [x for x in range(10) if x < 5]
# print(newlist) # [0, 1, 2, 3, 4]
# # # +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# ## EXAMPLES1: generate a new list without apples or fruit names without "a", and Set the values in the new list to upper case:
# fruits = ['apple', 'watermelon', 'green pear', 'kiwi', 'carrot', 'orange', 'grapes', 'melon', 'mango']
# newlist = []
# for x in fruits:
#     if x != "apple": #['watermelon', 'green pear', 'kiwi', 'carrot', 'orange', 'grapes', 'melon', 'mango']
#         if "a" not in x: #['kiwi', 'melon']
#             x = x.upper() # change each item here
#             newlist.append(x) #['KIWI', 'MELON']
# print(newlist) # ['watermelon', 'green pear', 'kiwi', 'carrot', 'orange', 'grapes', 'melon', 'mango']
# # # ---List comprehension way---------
# newlist = [x.upper() for x in fruits if x != "apple" if "a" not in x] # you can cain number of conditions
# print(newlist) # ['watermelon', 'green pear', 'kiwi', 'carrot', 'orange', 'grapes', 'melon', 'mango']
# # # # +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# # ## EXAMPLES1: generate a new list without apples or fruit names without "a", and Set the values in the new list to upper case:
# fruits = ['apple', 'watermelon', 'green pear', 'kiwi', 'carrot', 'orange', 'grapes', 'melon', 'mango']
# newlist = []
# for x in fruits:
#     if x != "apple": #['watermelon', 'green pear', 'kiwi', 'carrot', 'orange', 'grapes', 'melon', 'mango']
#         if "a" not in x: #['kiwi', 'melon']
#
#             x = x.replace(x[0],x[-1]).upper() # replace the first letter with the last letter, and change to uppercase
#             newlist.append(x) #['KIWI', 'MELON']
# print(newlist) # ['watermelon', 'green pear', 'kiwi', 'carrot', 'orange', 'grapes', 'melon', 'mango']
# # # ---List comprehension way---------
# newlist = [ x.replace(x[0],x[-1]).upper()  for x in fruits if x != "apple" if "a" not in x] # you can cain number of conditions
# print(newlist) # ['watermelon', 'green pear', 'kiwi', 'carrot', 'orange', 'grapes', 'melon', 'mango']
# # # +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# ## EXAMPLES1: Return "orange" instead of "banana"
# fruits = ['apple', 'watermelon', 'green pear', 'kiwi', 'carrot', 'orange', 'grapes', 'banana', 'mango']
# newlist = []
# for x in fruits:
#     if x != "banana": #['watermelon', 'green pear', 'kiwi', 'carrot', 'orange', 'grapes', 'melon', 'mango']
#         newlist.append(x)
#     else: # if the current elemt is == banaba, then
#        newlist.append("orange") #append orange it in place
# print(newlist) # ['watermelon', 'green pear', 'kiwi', 'carrot', 'orange', 'grapes', 'melon', 'mango']
# # # ---List comprehension way---------
# newlist = newlist = [x if x != "banana" else "orange" for x in fruits] # "Return the item if it is not banana, if it is banana return orange".
# print(newlist)

# -----------------------------------------------------------------------------------------------------------
# #  List sort
# # -----------------------------------------------------------------------------------------------------------
# # NOTE:
# # By default, the sort() sorts strings or numbers in accending office. to have it sort in descending order, use .sort(reverse = True)
# # By default the sort() method is case sensitive, resulting in all capital letters being sorted before lower case. thus,
# #
# #
# # method -- will sort the list alphanumerically, ascending, by default:
# thislist = ['apple', 'watermelon', 'green pear', 'kiwi', 'carrot', 'orange', 'grapes', 'banana', 'mango']
# thislist.sort()
# print(thislist)  # ['apple', 'banana', 'carrot', 'grapes', 'green pear', 'kiwi', 'mango', 'orange', 'watermelon']
# # ---------------------------------------------------------------------------------------
# # sort() method -- will sort the list alphanumerically, ascending, by default:
# thislist = [100, 50, 65, 82, 23, -34.4, 34.5, 34]
# thislist.sort()
# print(thislist)  # [-34.4, 23, 34, 34.5, 50, 65, 82, 100]
# # ---------------------------------------------------------------------------------------
# # sort() IN DESCENDING
# thislist = ['apple', 'watermelon', 'green pear', 'kiwi', 'carrot', 'orange', 'grapes', 'banana', 'mango']
# thislist.sort(reverse=True)
# print(thislist)  # ['watermelon', 'orange', 'mango', 'kiwi', 'green pear', 'grapes', 'carrot', 'banana', 'apple']
# # ---------------------------------------------------------------------------------------
# # sort() IN DESCENDING
# thislist = [100, 50, 65, 82, 23, -34.4, 34.5, 34]
# thislist.sort(reverse=True)
# print(thislist)  # [100, 82, 65, 50, 34.5, 34, 23, -34.4]
# # -----------------------------------------
# # Reverse Order
# thislist = ["banana", "Orange", "Kiwi", "cherry"]
# thislist.reverse()
# print(thislist)
# # ---------
# thislist = [100, 50, 65, 82, 23, -34.4, 34.5, 34]
# thislist.reverse()
# print(thislist)
# # ----------------------------------------------------
# # By default the sort() method is case sensitive, resulting in all capital letters being sorted before lower case letters:
# # Case sensitive sorting can give an unexpected result:
# thislist = ['apple', 'Watermelon', 'green pear', 'Kiwi', 'carrot', 'orange', 'grapes', 'Orange', 'banana', 'mango']
# thislist.sort()
# print(
#     thislist)  # ['Kiwi', 'Orange', 'Watermelon', 'apple', 'banana', 'carrot', 'grapes', 'green pear', 'mango', 'orange']
# # to fix this unpected result, use thislist.sort(key = str.lower)
# thislist = ['apple', 'Watermelon', 'green pear', 'Kiwi', 'carrot', 'orange', 'grapes', 'Orange', 'banana', 'mango']
# thislist.sort(key=str.lower)
# print(
#     thislist)  # ['Kiwi', 'Orange', 'Watermelon', 'apple', 'banana', 'carrot', 'grapes', 'green pear', 'mango', 'orange']
#
# # ---------sorted()-------------------------------------------
# # it returns a list
# words_to_sort = "LearnPython.com is awesome to learn about custom sort functions in Python"
# result = sorted(words_to_sort.split(), key=str.lower)
# print(result)
#

# ----------------------------------------------
# CUSTIMIZED SORT FUNCTION
# Sort the list based on how close the number is to 50:
def myfunc(n):
    return abs(n - 50)


thislist = [100, 50, 65, 82, 23]
thislist.sort(key=myfunc)
print(thislist)  # [50, 65, 23, 82, 100]

# The abs() built-in Python function returns the absolute value of a number.
# In mathematics, the absolute value of a number refers to that number's distance from zero.
# Essentially, it is how far away that number is from zero on the number line.
# For example, the absolute value of the number five is five since the distance from zero to five is five units.
# ----------------------------------------------

def compare(x, y):
  return x ** 3 - y ** 3

l = sorted([10,2,15,30,1000,24,74,81,19], key=lambda x: compare(x, 0))
print(l)


def numeric_compare(x, y):
  return x - y

l = sorted([10,2,15,30,1000,24,74,81,19], key=lambda x: numeric_compare(x, 0))
print(l)


# ------------------------------------
l = sorted([10,2,15,30,1000,24,74,81,19])
print(l)
l = sorted([10,2,15,30,1000,24,74,81,19], key=lambda x: x)
print(l)


# def numeric_compare(x, y): #
#   if x < y:
#     return -1
#   elif x == y:
#     return 0
#   else:
#     return 1
# # l = sorted([5, 2, 4, 1, 3], key=numeric_compare)
# l = sorted([10,2,15,-30,1000,24,74,81,19], key=lambda x: numeric_compare(x))
# print(l) #[5, 2, 4, 1, 3]

# --------- among the list of items, and during the soring, where key= func in sorted, return "orange as 0 index, and apple as index 1 and the rest can be anythin
# fruits = ["apple", "banana", "orange", "pear", "kiwi"]  # Define a list of strings

# ===============================================================================
#
#
# def my_sort_key(fruit):  # Define a custom sort order
#     if fruit == "orange":
#         return 0
#     elif fruit == "apple":
#         return 1
#     else:
#         return 2
#
#
# sorted_fruits = sorted(fruits, key=my_sort_key)  # Sort the list using the custom sort order
# print(sorted_fruits)  # Print the sorted list
# # using lambda
# sorted_fruits = sorted(fruits, key=lambda fruit: 0 if fruit == "orange" else 1 if fruit == "apple" else 1)  # Sort the list using the custom sort order
# print(sorted_fruits)  # Print the sorted list
# # ----------------sort a normal list-------------------------
# list_of_nums = [12, 23, 13, 12, 45, 34, 56, 23, 5, 78, 97]
#
#
# def num_func(n):
#     return n
#
#
# # both using of normal function or lambda function,
# # the key=num_func or key=lambda x: x work with the individual elements in the list passed in sorted()
# sorted_num = sorted(list_of_nums, key=num_func)
# print(sorted_num)
# sorted_num1 = sorted(list_of_nums, key=lambda x: x)
# print(sorted_num1)
# # -----------------
# # -------------------sort a list of tuple ----------------------------
#
# def func(x):
#   return x[1]
#
# people = [("Alice", 25), ("Bob", 20), ("Charlie", 30), ("Grace", 20), ("Andrew", 44)]
# #to sort by default uses the first item of the tuple
# sorted_people = sorted(people, key=lambda x: x)
# print(sorted_people) #[('Alice', 25), ('Andrew', 44), ('Bob', 20), ('Charlie', 30), ('Grace', 20)]
# #to sort based on name
# sorted_people = sorted(people, key=lambda x: x[0])
# print(sorted_people) #[('Alice', 25), ('Andrew', 44), ('Bob', 20), ('Charlie', 30), ('Grace', 20)]
# #to sort based on age
# sorted_people = sorted(people, key=lambda x: x[1])
# print(sorted_people) #[('Alice', 25), ('Andrew', 44), ('Bob', 20), ('Charlie', 30), ('Grace', 20)]
# #using normal funcion
# sorted_people = sorted(people, key=func)
# print(sorted_people) #[('Alice', 25), ('Andrew', 44), ('Bob', 20), ('Charlie', 30), ('Grace', 20)]


# ----------------------------------------------------------


# -----------------------------------------------------------------------------------------------------------
#  SOME GENERAL FACT ABOUT PYTHON COLLECTIONS(ARRAY)
# -----------------------------------------------------------------------------------------------------------
# There are four collection data types in the Python programming language:
#
# (1) List is a collection which is ordered and changeable. Allows duplicate members.
# (2) Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
# (3) Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
# (4) Dictionary is a collection which is ordered** and changeable. No duplicate members.
# (5) Although, Set items are unchangeable, but you can remove and/or add items whenever you like.


# ------------------------------------------------------------------------------------
