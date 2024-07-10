
print()
print()
print()
print()




# -----------------------------------------------------------------------------------------------------------
#
# -----------------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------
#
# -----------------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------
#
# -----------------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------
#
# -----------------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------
#  SOME GENERAL FACT ABOUT PYTHON COLLECTIONS(ARRAY)
# -----------------------------------------------------------------------------------------------------------
# There are four collection data types in the Python programming language:
#
#(1) List is a collection which is ordered and changeable. Allows duplicate members.
#(2) Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
#(3) Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
#(4) Dictionary is a collection which is ordered** and changeable. No duplicate members.
#(5) Although, Set items are unchangeable, but you can remove and/or add items whenever you like.



# --------------------------------------------------------------

# students = {
#     'student_1': {'name': 'Grace', 'sex': 'Female', 'age': 8},
#     'student_2': {'name': 'Adam', 'sex': 'Male', 'age': 15},
#     'student_3': {'name': 'Paul', 'sex': 'Male', 'age': 5},
#     'student_4': {'name': 'Linda', 'sex': 'Female', 'age': 14},
#     'student_5': {'name': 'Joseph', 'sex': 'Male', 'age': 10},
#     'student_6': {'name': 'Peter', 'sex': 'Male', 'age': 19},
#     'student_7': {'name': 'Kevin De Bruyne', 'sex': 'Male', 'age': 7},
#     'student_8': {'name': 'Kunle', 'sex': 'Male', 'age': 6},
#     'student_9': {'name': 'Mathew', 'sex': 'Male', 'age': 13},
#     'student_10': {'name': 'Olivia', 'sex': 'Female', 'age': 12},
#     'student_11': {'name': 'Sophia', 'sex': 'Female', 'age': 17},
#     'student_12': {'name': 'Emma', 'sex': 'Female', 'age': 3},
#     'student_13': {'name': 'Lucas', 'sex': 'Male', 'age': 16},
#     'student_14': {'name': 'Olivia', 'sex': 'Female', 'age': 2},
#     'student_15': {'name': 'Liam', 'sex': 'Male', 'age': 8},
#     'student_16': {'name': 'Mason', 'sex': 'Male', 'age': 20},
#     'student_17': {'name': 'Anna', 'sex': 'Female', 'age': 18},
#     'student_18': {'name': 'John', 'sex': 'Male', 'age': 9},
#     'student_19': {'name': 'Mike', 'sex': 'Male', 'age': 11},
#     'student_20': {'name': 'Alice', 'sex': 'Female', 'age': 4},
#     'student_21': {'name': 'Robert Lewandowski', 'sex': 'Male', 'age': 14},
#     'student_22': {'name': 'Lionel Messi', 'sex': 'Male', 'age': 13},
#     'student_23': {'name': 'Eden Hazard', 'sex': 'Male', 'age': 15},
#     'student_24': {'name': 'Cristiano Ronaldo', 'sex': 'Male', 'age': 12},
#     'student_25': {'name': 'Kevin De Bruyne', 'sex': 'Male', 'age': 7},
#     'student_26': {'name': 'Mohamed Salah', 'sex': 'Male', 'age': 19},
#     'student_27': {'name': 'Kylian Mbappé', 'sex': 'Male', 'age': 8},
#     'student_28': {'name': 'Neymar Jr.', 'sex': 'Male', 'age': 10},
#     'student_29': {'name': 'Mary', 'sex': 'Female', 'age': 5},
#     'student_30': {'name': 'Jennifer', 'sex': 'Female', 'age': 6},
#     'student_31': {'name': 'Linda', 'sex': 'Female', 'age': 11},
#     'student_32': {'name': 'Patricia', 'sex': 'Female', 'age': 16},
#     'student_33': {'name': 'Elizabeth', 'sex': 'Female', 'age': 20},
#     'student_34': {'name': 'Barbara', 'sex': 'Female', 'age': 1},
#     'student_35': {'name': 'Susan', 'sex': 'Female', 'age': 7},
#     'student_36': {'name': 'Jessica', 'sex': 'Female', 'age': 15},
#     'student_37': {'name': 'Sarah', 'sex': 'Female', 'age': 14},
#     'student_38': {'name': 'Karen', 'sex': 'Female', 'age': 4},
#     'student_39': {'name': 'Alice', 'sex': 'Female', 'age': 9},
#     'student_40': {'name': 'Karen', 'sex': 'Female', 'age': 13},
#     'student_41': {'name': 'Many', 'sex': 'Female', 'age': 18},
#     'student_42': {'name': 'Banabas', 'sex': 'Male', 'age': 17},
#     'student_43': {'name': 'Smart', 'sex': 'Male', 'age': 3},
#     'student_44': {'name': 'Joe', 'sex': 'Male', 'age': 6},
#     'student_45': {'name': 'Smith', 'sex': 'Male', 'age': 11},
#     'student_46': {'name': 'Ken', 'sex': 'Male', 'age': 19},
#     'student_47': {'name': 'Apolo', 'sex': 'Male', 'age': 5},
#     'student_48': {'name': 'Paul', 'sex': 'Male', 'age': 2},
#     'student_49': {'name': 'Jennifer', 'sex': 'Female', 'age': 7},
#     'student_50': {'name': 'Tom', 'sex': 'Male', 'age': 15}
# }
# --------------------------------------------------------------------------------------

# import random

# # List of names
# names = ["Tom", "Grace", "Paul", "Lans", "Many", "Kunle", "Ade", "Olumide", "Adam", "Joseph", "Leo", "Peter", "Evans", 
#          "Mathew", "Banabas", "Smart", "Joe", "Smith", "Ken", "Apolo", "Paul", "Mary", "Jennifer", "Linda", "Patricia", 
#          "Elizabeth", "Barbara", "Susan", "Jessica", "Sarah", "Karen", "Alice", "Robert Lewandowski", "Lionel Messi", 
#          "Eden Hazard", "Cristiano Ronaldo", "Kevin De Bruyne", "Mohamed Salah", "Kylian Mbappé", "Neymar Jr.",
#          "Anna", "John", "Mike", "Sophia", "Emma", "Lucas", "Olivia", "Liam", "Mason"]

# # Ensure we have at least 50 unique names
# random.shuffle(names)
# names = names[:50]

# # Create the dictionary of persons
# persons = {}
# for i, name in enumerate(names):
#     sex = random.choice(["Male", "Female"])
#     age = random.randint(1, 20)
#     persons[f"person_{i+1}"] = {"name": name, "sex": sex, "age": age}

# # Filter the dictionary to only include females
# female_persons = {}
# for key, value in persons.items():
#     if value['sex'] == 'Female':
#         female_persons[key] = value

# # Print the original dictionary
# print("Original Dictionary:")
# for key, value in persons.items():
#     print(f"{key}: {value}")

# # Print the filtered dictionary
# print("\nFiltered Dictionary (Only Females):")
# for key, value in female_persons.items():
#     print(f"{key}: {value}")

# -----------
# Explanation:
# Creating the persons Dictionary:

# We first create a dictionary with 50 persons, each having a name, sex, and age.
# The sex is randomly assigned as either "Male" or "Female" and the age is a random integer between 1 and 20.
# Filtering the Dictionary:

# We use a for loop to iterate through each key-value pair in the persons dictionary.
# If the sex of the person is "Female", we add that entry to the female_persons dictionary.
# Printing the Dictionaries:

# We print the original dictionary and the filtered dictionary using for loops to show the contents.
# ------------------------------------------------------------------------------------

# numbers = {10:"Ten", 20:"Twenty", 30:"Thirty",40:"Forty"}

# for x in numbers:
#    print (x)

# print ()

# for x in numbers:
#    print (x,":",numbers[x])

# print ()

# for x in numbers.items():
#    print (x)

# ------------------------------------------------------------------------------------














































print()
print()
print()
print()
