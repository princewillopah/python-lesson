
print()
print()



# animals = ['lion', 'elephant', 'tiger', 'zebra', 'giraffe', 'monkey', 'kangaroo', 'hippopotamus', 'cheetah', 'rhinoceros']
#            0        1           2        3         4        5          6            7            8             9

# colors = ['red', 'blue', 'green', 'yellow', 'orange', 'purple', 'pink', 'brown', 'black', 'white']

# people_names = ['Alice', 'Bob', 'Charlie', 'David', 'Eva', 'Frank', 'Grace', 'Hannah', 'Isaac', 'Jane']

# # prime_numbers = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]

# natural_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

# even_numbers = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40]

# mixed = ['apple', 5, 'banana', 8.7, True, 'orange', 12, False, 'grape', 3.14]

# # print(f'I have a list of animals\nThis is the list: {animals}\nthe list contains {len(animals)} animals')

# # print(animals[4])

# # print(animals[8])

# # print(f'I love {animals[5]} and {animals[1]}')

# # print(f"{people_names[9]} loves {colors[9]} {animals[2]} that she got {natural_numbers[3]} of them")

# # print(f"{people_names[-1]} loves {colors[-1]} {animals[2]} that she got {natural_numbers[3]} of them")

# # =========================================
# #  Filtering 
# # =========================================

# animals = ['lion', 'elephant', 'tiger', 'zebra', 'giraffe', 'monkey', 'kangaroo', 'hippopotamus', 'cheetah', 'rhinoceros']
# #             0        1         2         3        4         5           6          7                 8         9
# #             -10      -9        -8       -7        -6        -5         -4          -3             -2          -1

# print(animals)             #  
# print(animals[0])         #  
# print(animals[1])         #  
# print(animals[2])         #  
# print(animals[-1])         #  
# print(animals[-2])             #  
# print(animals[3:7])    #  'zebra','giraffe', 'monkey', 'kangaroo'
# print(animals[2:5])    # 'tiger', 'zebra', 'giraffe',
# print(animals[7:9])     # 'hippopotamus', 'cheetah',
# print(animals[1:6])     # 'elephant', 'tiger', 'zebra', 'giraffe', 'monkey'
# print(animals[-4:-1])    # 'kangaroo', 'hippopotamus', 'cheetah', 'rhinoceros'
# print()
# print(animals[:6])      # 'lion', 'elephant', 'tiger', 'zebra', 'giraffe', 'monkey'
# print(animals[3:])      #  'zebra', 'giraffe', 'monkey', 'kangaroo', 'hippopotamus', 'cheetah', 'rhinoceros'
# print(animals[:])        # ['lion', 'elephant', 'tiger', 'zebra', 'giraffe', 'monkey', 'kangaroo', 'hippopotamus', 'cheetah', 'rhinoceros']
# print()
# print(animals[-7:-3])       #    'zebra', 'giraffe', 'monkey', 'kangaroo', 
# print(animals[2:])          #   'tiger', 'zebra', 'giraffe', 'monkey', 'kangaroo', 'hippopotamus', 'cheetah', 'rhinoceros'
# print(animals[:6])          #   ['lion', 'elephant', 'tiger', 'zebra', 'giraffe', 'monkey'
# print(animals[4:6])         #   'giraffe', 'monkey'

# ============================================================================================
# animals = ['lion', 'elephant', 'tiger', 'zebra', 'giraffe', 'monkey', 'kangaroo', 'hippopotamus', 'cheetah', 'rhinoceros']

# print("Enter the animal that you want to search")
# my_search = input()

# if my_search in animals:
#   print(f"Yes, {my_search} is in the animals list")
# else:
#   print(f"No, {my_search} is in the animals list")

# ============================================================================================
#  change in the list  --- mordify/edit/update the list
# ============================================================================================
animals = ['lion', 'elephant', 'tiger', 'zebra', 'giraffe', 'monkey', 'kangaroo', 'hippopotamus', 'cheetah', 'rhinoceros']
# # #         0        1         2         3        4         5           6          7                 8         9
# # #             -10      -9        -8       -7        -6        -5         -4          -3             -2          -1


# print(animals[4:7])
animals[4:7] = ["goat","hen","cock","fly"]
print(animals)
# print(animals[9])
# print(animals[5:9])
# print(animals[5:10])
# print(animals[0:2])
# print(animals)
# animals[4] = "dog"
# print(animals)
# animals[5:8] = ["rat","goat","pig"]
# print(animals)
# animals[2:8] = ["rat","goat","pig"]
# print(animals)
# animals[5:7] = ['lion', 'elephant', 'tiger', 'zebra', 'giraffe', 'monkey', 'kangaroo', 'hippopotamus', 'cheetah', 'rhinoceros']
# print(animals)
# animals[-5] = "Chicken"
# print(animals)

# ============================================================================================
#  Add  Items to List
# ============================================================================================
# The insert() method inserts an item at the specified index:
# extend()
# MaleName = ['Bob', 'Charlie', 'David','Frank', 'Isaac']
# FemaleNmae = ['Alice',  'Eva', 'Grace', 'Hannah', 'Jane']

# print(FemaleNmae)
# # FemaleNmae[-3:-2] = ["Queen","Lola"]
# # FemaleNmae[3] = "Queen"
# # FemaleNmae[4] = "Lola"
# print(FemaleNmae[3:5])
# print(FemaleNmae)
# FemaleNmae.insert(2,"Amanda",)
# print(FemaleNmae)
# FemaleNmae.insert(0,"Joy")
# print(FemaleNmae)
# FemaleNmae.insert(3,["Peace","Gloriah","Agatha"])
# print(FemaleNmae)

# MaleName.extend(FemaleNmae)
# print(MaleName)









# ============================================================================================
#  Remove Items from List
# ============================================================================================
# ============================================================================================
#  Loop Through a List
# ============================================================================================
# ============================================================================================
#  Sort Lists
# ============================================================================================
# ============================================================================================
#   Copy Lists
# ============================================================================================
# ============================================================================================
#  Join Two Lists
# ============================================================================================
# ============================================================================================
#  List Comprehension
# ============================================================================================



























































print()
print()
print()
print()
print()
print()