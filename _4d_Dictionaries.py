
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
# numbers = {10:"Ten", 20:"Twenty", 30:"Thirty",40:"Forty"}

# for x in numbers:
#    print (x)

# print ()

# for x in numbers:
#    print (x,":",numbers[x])

# print ()

# for x in numbers.items():
#    print (x)
# ----------------------------------------------------------------------------------
# students = {
#             'student_1': {'name': 'Grace', 'sex': 'Female', 'age': 8},
#             'student_2': {'name': 'Adam', 'sex': 'Male', 'age': 15},
#             'student_3': {'name': 'Paul', 'sex': 'Male', 'age': 5},
#             'student_4': {'name': 'Linda', 'sex': 'Female', 'age': 14},
#             'student_5': {'name': 'Joseph', 'sex': 'Male', 'age': 10},
#             'student_6': {'name': 'Peter', 'sex': 'Male', 'age': 19},
#             'student_7': {'name': 'Kevin De Bruyne', 'sex': 'Male', 'age': 7},
#             'student_8': {'name': 'Kunle', 'sex': 'Male', 'age': 6},
#             'student_9': {'name': 'Mathew', 'sex': 'Male', 'age': 13},
#             'student_10': {'name': 'Olivia Adams', 'sex': 'Female', 'age': 12},
#             'student_11': {'name': 'Sophia', 'sex': 'Female', 'age': 17},
#             'student_12': {'name': 'Emma', 'sex': 'Female', 'age': 3},
#             'student_13': {'name': 'Lucas', 'sex': 'Male', 'age': 16},
#             'student_14': {'name': 'Olivia Grey', 'sex': 'Female', 'age': 2},
#             'student_15': {'name': 'Liam', 'sex': 'Male', 'age': 8},
#             'student_16': {'name': 'Mason', 'sex': 'Male', 'age': 20},
#             'student_17': {'name': 'Anna', 'sex': 'Female', 'age': 18},
#             'student_18': {'name': 'John', 'sex': 'Male', 'age': 9},
#             'student_19': {'name': 'Mike', 'sex': 'Male', 'age': 11},
#             'student_20': {'name': 'Alice', 'sex': 'Female', 'age': 4},
#             'student_21': {'name': 'Robert Lewandowski', 'sex': 'Male', 'age': 14},
#             'student_22': {'name': 'Lionel Messi', 'sex': 'Male', 'age': 13},
#             'student_23': {'name': 'Eden Hazard', 'sex': 'Male', 'age': 15},
#             'student_24': {'name': 'Cristiano Ronaldo', 'sex': 'Male', 'age': 12},
#             'student_25': {'name': 'Kevin De Bruyne', 'sex': 'Male', 'age': 7},
#             'student_26': {'name': 'Mohamed Salah', 'sex': 'Male', 'age': 19},
#             'student_27': {'name': 'Kylian Mbappé', 'sex': 'Male', 'age': 8},
#             'student_28': {'name': 'Neymar Jr.', 'sex': 'Male', 'age': 10},
#             'student_29': {'name': 'Mary', 'sex': 'Female', 'age': 5},
#             'student_30': {'name': 'Jennifer', 'sex': 'Female', 'age': 6},
#             'student_31': {'name': 'Linda', 'sex': 'Female', 'age': 11},
#             'student_32': {'name': 'Patricia', 'sex': 'Female', 'age': 16},
#             'student_33': {'name': 'Elizabeth', 'sex': 'Female', 'age': 20},
#             'student_34': {'name': 'Barbara', 'sex': 'Female', 'age': 1},
#             'student_35': {'name': 'Susan', 'sex': 'Female', 'age': 7},
#             'student_36': {'name': 'Jessica', 'sex': 'Female', 'age': 15},
#             'student_37': {'name': 'Sarah', 'sex': 'Female', 'age': 14},
#             'student_38': {'name': 'Karen', 'sex': 'Female', 'age': 4},
#             'student_39': {'name': 'Alice', 'sex': 'Female', 'age': 9},
#             'student_40': {'name': 'Karen', 'sex': 'Female', 'age': 13},
#             'student_41': {'name': 'Many', 'sex': 'Female', 'age': 18},
#             'student_42': {'name': 'Banabas', 'sex': 'Male', 'age': 17},
#             'student_43': {'name': 'Smart', 'sex': 'Male', 'age': 3},
#             'student_44': {'name': 'Joe', 'sex': 'Male', 'age': 6},
#             'student_45': {'name': 'Smith', 'sex': 'Male', 'age': 11},
#             'student_46': {'name': 'Ken', 'sex': 'Male', 'age': 19},
#             'student_47': {'name': 'Apolo', 'sex': 'Male', 'age': 5},
#             'student_48': {'name': 'Paul', 'sex': 'Male', 'age': 2},
#             'student_49': {'name': 'Jennifer', 'sex': 'Female', 'age': 7},
#             'student_50': {'name': 'Tom', 'sex': 'Male', 'age': 15}
# }

# for details in students:
#      print(details, students[details])

# # for student, details in students.items():
# #     if details['sex'] == 'Female' or details['age'] >= 8:
# #         print(f"{student} [NAME: {details['name']}, AGE: {details['name']}, SEX: {details['name']}] ")

# for id, (student, details) in enumerate(students.items(), 1):
#     if details['sex'] == 'Female' or details['age'] >= 8:
#         print(f"{id}. {student} [NAME: {details['name']}, AGE: {details['age']}, SEX: {details['sex']}] ")





# --------------------------------------------------------------------------------------

#  --------------------------------------------------------------------------------------

# import random

# # Example list of names
# names = [
#     "John Smith", "Jane Johnson", "Michael Williams", "Sarah Brown", "David Jones", "Emily Garcia",
#     "Robert Miller", "Laura Davis", "James Rodriguez", "Jessica Martinez", "Daniel Hernandez", "Mary Lopez",
#     "Paul Gonzalez", "Jennifer Wilson", "Mark Anderson", "Linda Thomas", "Chris Taylor", "Elizabeth Moore",
#     "Andrew Jackson", "Susan Martin", "Matthew Lee", "Angela Perez", "Joshua Thompson", "Karen White",
#     "Kevin Harris", "Lisa Sanchez", "Brian Clark", "Nancy Ramirez", "Charles Lewis", "Margaret Robinson",
#     "Steven Walker", "Sandra Young", "Anthony Allen", "Ashley King", "Donald Wright", "Kimberly Scott",
#     "Timothy Torres", "Michelle Nguyen", "Jason Hill", "Deborah Flores", "Joseph Green", "Laura Adams",
#     "George Nelson", "Helen Baker", "Thomas Hall", "Cynthia Rivera", "Frank Campbell", "Donna Mitchell",
#     "Patrick Carter", "Carol Roberts", "John Lee", "Jane Thompson", "Michael White", "Sarah Harris",
#     "David Sanchez", "Emily Clark", "Robert Ramirez", "Laura Lewis", "James Robinson", "Jessica Walker",
#     "Daniel Young", "Mary Allen", "Paul King", "Jennifer Wright", "Mark Scott", "Linda Torres",
#     "Chris Nguyen", "Elizabeth Hill", "Andrew Flores", "Susan Green", "Matthew Adams", "Angela Nelson",
#     "Joshua Baker", "Karen Hall", "Kevin Rivera", "Lisa Campbell", "Brian Mitchell", "Nancy Carter",
#     "Charles Roberts", "Margaret Smith", "Steven Johnson", "Sandra Williams", "Anthony Brown", "Ashley Jones",
#     "Donald Garcia", "Kimberly Miller", "Timothy Davis", "Michelle Rodriguez", "Jason Martinez", "Deborah Hernandez",
#     "Joseph Lopez", "Laura Gonzalez", "George Wilson", "Helen Anderson", "Thomas Thomas", "Cynthia Taylor",
#     "Frank Moore", "Donna Jackson", "Patrick Martin", "Carol Lee"
# ]

# # # # Ensure we have at least 50 unique names
# random.shuffle(names) # Shuffle the list of names
# names = names[:50] # Take the first 50 elements of the shuffled list
# # print(names) # Print the resulting list

# # # # Create the dictionary of persons from the above shuffled list of 50 names
# persons = {}
# for i, name in enumerate(names):
#     sex = random.choice(["Male", "Female"])
#     age = random.randint(10, 18)
#     persons[f"person_{i+1}"] = {"name": name, "sex": sex, "age": age}

# # # Print the original dictionary
# print("Original Created Dictionary:")
# for key, value in persons.items():
#     print(f"{key}: {value}")

# # Filter the dictionary to only include females
# female_persons = {}
# for key, value in persons.items():
#     if value['sex'] == 'Female':
#         female_persons[key] = value

# # # Print the filtered dictionary
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



# ------------------------------------------------------------------------------------














































print()
print()
print()
print()
