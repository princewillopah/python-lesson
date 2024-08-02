print()


#








# ===================================================================================================================
# 
# ===================================================================================================================

# num1 = 11     # 11
# num2 = num1   # 11
# num3 = num1   # 11
# num4 = num2   # 11

# print(f"num1 = {num1} and {num1} is stored in a storage place with address number {id(num1)}")    # num1 = 11
# print(f"num2 = {num2} and {num2} is stored in a storage place with address number {id(num2)}")    # num2 =  11
# print(f"num3 = {num3} and {num3} is stored in a storage place with address number {id(num3)}")    # num3 =  11
# print(f"num4 = {num4} and {num4} is stored in a storage place with address number {id(num4)}")    # num4 =  11
# print()

# num1 = 12  
# print(f"num1 = {num1} and {num1} is stored in a storage place with address number {id(num1)}")    # num1 = 12
# print(f"num2 = {num2} and {num2} is stored in a storage place with address number {id(num2)}")    # num2 =  11
# print(f"num3 = {num3} and {num3} is stored in a storage place with address number {id(num3)}")    # num3 =  11
# print(f"num4 = {num4} and {num4} is stored in a storage place with address number {id(num4)}")    # num4 =  11
# print()


# num2 = 13
# print(f"num1 = {num1} and {num1} is stored in a storage place with address number {id(num1)}")    # num1 = 12
# print(f"num2 = {num2} and {num2} is stored in a storage place with address number {id(num2)}")    # num2 =  13
# print(f"num3 = {num3} and {num3} is stored in a storage place with address number {id(num3)}")    # num3 =  11
# print(f"num4 = {num4} and {num4} is stored in a storage place with address number {id(num4)}")    # num4 =  11
# print()

# num3 = 14; num4 = num3
# print(f"num1 = {num1} and {num1} is stored in a storage place with address number {id(num1)}")    # num1 = 12
# print(f"num2 = {num2} and {num2} is stored in a storage place with address number {id(num2)}")    # num2 =  13
# print(f"num3 = {num3} and {num3} is stored in a storage place with address number {id(num3)}")    # num3 =  11
# print(f"num4 = {num4} and {num4} is stored in a storage place with address number {id(num4)}")    # num4 =  11
# print()

"""
The above illustrated that a storage place is created for the data 11 when 11 was initially assigned to num1.
when num2 is made equla to num1, num2 was also pointing to that storage place ans so are num3 and num4(via num2)
when num1 was now assigned another value(12), num1 stopped pointing to the storage place(where 11 was tsord), leaving the rest to keep pointing to where 11 is stored
likewise, when num2 was assigned a new value(12), it stopped point to the new storage place where 12 is stored, leaving num4 to keep pointing to the place where 11 is stored, even when num4 pointed to the same 11 position throuhg num2
if num3 and num4 are now assigned a new value, the place" 140720434772728" where 11 is stored will now be 
removed by python through a process called "Gabagge collector". this is because there is now was someone can access 11 and no variable is using it or assigned to it. it will only be wasting more storage place
the reason for the above is because intergers are immutatioble(that is thay can not be changed). once you put a number(e.g. 11) in a place in memory, it can not be changed in that memory place
"""

# # ============================================================

# list1 = [1,2,3,4,5]
# list2 = list1
# list3 = list1
# list4 = list2

# print(f"list1 = {list1} and {list1} is stored in a storage place with address number {id(list1)}")    # num1 =  [1,2,3,4,5]
# print(f"list2 = {list2} and {list2} is stored in a storage place with address number {id(list2)}")    # num2 =   [1,2,3,4,5]
# print(f"list3 = {list3} and {list3} is stored in a storage place with address number {id(list3)}")    # list3 =   [1,2,3,4,5]
# print(f"list4 = {list4} and {list4} is stored in a storage place with address number {id(list4)}")    # list4 =   [1,2,3,4,5]
# print()

# list1[0] = 10
# list4[1] = 20

# print(f"list1 = {list1} and {list1} is stored in a storage place with address number {id(list1)}")    # num1 =   [10, 20, 3, 4, 5]
# print(f"list2 = {list2} and {list2} is stored in a storage place with address number {id(list2)}")    # num2 =    [10, 20, 3, 4, 5]
# print(f"list3 = {list3} and {list3} is stored in a storage place with address number {id(list3)}")    # list3 =    [10, 20, 3, 4, 5]
# print(f"list4 = {list4} and {list4} is stored in a storage place with address number {id(list4)}")    # list4 =   [10, 20, 3, 4, 5]
# print()

# list1 = [4,5,6,7]

# print(f"list1 = {list1} and {list1} is stored in a storage place with address number {id(list1)}")    # num1 = 11
# print(f"list2 = {list2} and {list2} is stored in a storage place with address number {id(list2)}")    # num2 =  11
# print(f"list3 = {list3} and {list3} is stored in a storage place with address number {id(list3)}")    # list3 =  11
# print(f"list4 = {list4} and {list4} is stored in a storage place with address number {id(list4)}")    # list4 =  11
# print()

# list2 = [9,10,11,12]
# print(f"list1 = {list1} and {list1} is stored in a storage place with address number {id(list1)}")    # num1 = 11
# print(f"list2 = {list2} and {list2} is stored in a storage place with address number {id(list2)}")    # num2 =  11
# print(f"list3 = {list3} and {list3} is stored in a storage place with address number {id(list3)}")    # list3 =  11
# print(f"list4 = {list4} and {list4} is stored in a storage place with address number {id(list4)}")    # list4 =  11
# print()

#### list acts like integer

# # ============================================================

# dict1 = {"value1":11}
# dict2 = dict1
# print(f"dict1 = {dict1} and {dict1} is stored in a storage place with address number {id(dict1)}")    # dict1 = {'value1': 11} in 1879663125888
# print(f"dict2 = {dict2} and {dict2} is stored in a storage place with address number {id(dict2)}")    # dict2 = {'value1': 11} in 1879663125888
# print()

# dict2["value1"] = 22

# print(f"dict1 = {dict1} and {dict1} is stored in a storage place with address number {id(dict1)}")    # dict1 = {'value1': 22} in 1879663125888
# print(f"dict2 = {dict2} and {dict2} is stored in a storage place with address number {id(dict2)}")    # dict2 = {'value1': 22} in 1879663125888
# print()


# dict1["value1"] = 33

# print(f"dict1 = {dict1} and {dict1} is stored in a storage place with address number {id(dict1)}")    # dict1 = {'value1': 22} in 1879663125888
# print(f"dict2 = {dict2} and {dict2} is stored in a storage place with address number {id(dict2)}")    # dict2 = {'value1': 22} in 1879663125888
# print()

# dict1 = {"number":44}
# print(f"dict1 = {dict1} and {dict1} is stored in a storage place with address number {id(dict1)}")    # dict1 = {'value1': 22} in 1879663125888
# print(f"dict2 = {dict2} and {dict2} is stored in a storage place with address number {id(dict2)}")    # dict2 = {'value1': 22} in 2763890567424   -  new address space when a new dictionary is assigned
# print()


"""
from the above, it shows that the address space(1879663125888) where {"value1":11} is stored still remains the same even when the value is
changed by dicts, and both dict1 and dict2 are pointing to the same address place (1879663125888) thus having the same values
so no matter what, whether the value of dict1 is changed, or the value of dict2 is changed, their value will stall be the same and they will always have the same address space 
However, when any of dict1, or dict, has an entirely new dictionary, it value and adrress will change
"""  















print()