"""
Introduction to Tuples in Python
Tuples are a type of data structure in Python that allow you to store a sequence of immutable objects. 
They are similar to lists but have some key differences, primarily that tuples cannot be changed after they are created.
"""

"""

Tuple Methods
Tuples have only two built-in methods:
    count(): Returns the number of times a specified value appears in the tuple.
    index(): Searches the tuple for a specified value and returns the position of where it was found.


Why Use Tuples?
    Immutability: Useful for data that should not be changed throughout the program.
    Performance: Tuples can be slightly more memory-efficient than lists.
    Keys for Dictionaries: Tuples can be used as keys in dictionaries because they are immutable and hashable.

Immutability of Tuples
Tuples are immutable, meaning you cannot change, add, or remove elements after the tuple is created:
    my_tuple = (1, 2, 3)
    # The following operations would raise errors
    # my_tuple[0] = 10      # TypeError: 'tuple' object does not support item assignment
    # my_tuple.append(4)    # AttributeError: 'tuple' object has no attribute 'append'
    # my_tuple.remove(2)    # AttributeError: 'tuple' object has no attribute 'remove'



Summary
    Tuples are ordered, immutable collections of items.
    Created using parentheses: my_tuple = (1, 2, 3).
    Accessed via indexing and slicing: my_tuple[0], my_tuple[1:3].
    Can be unpacked into variables: a, b, c = my_tuple.
    Methods: count() and index().
    Tuples are immutable: cannot change elements after creation.
    Useful for data that should not change, and can be used as dictionary keys.
"""




####  -----------------------------------------------------------------------------------------------------------
####   SOME GENERAL FACT ABOUT PYTHON COLLECTIONS(ARRAY)
####  -----------------------------------------------------------------------------------------------------------
####  There are four collection data types in the Python programming language:
#### 
#### (1) List is a collection which is ordered and changeable. Allows duplicate members.
#### (2) Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
#### (3) Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
#### (4) Dictionary is a collection which is ordered** and changeable. No duplicate members.
#### (5) Although, Set items are unchangeable, but you can remove and/or add items whenever you like.



####  -----------------------------------------------------------------------------------------------------------
#### 
####  -----------------------------------------------------------------------------------------------------------


##### Creating a tuple
# my_tuple = (1, 2, 3, 4, 5) 
# print(my_tuple)

##### Empty tuple
# empty_tuple = ()  
# print(empty_tuple)

##### Single-element tuple
# single_element_tuple = (1,) 
# print(single_element_tuple)

##### Accessing elements
# my_tuple = (1, 2, 3, 4, 5)
# print(my_tuple[0])  # Output: 1
# print(my_tuple[3])  # Output: 4

##### Slicing a tuple
# my_tuple = (1, 2, 3, 4, 5)
# print(my_tuple[1:3])  # Output: (2, 3)
# print(my_tuple[:3])   # Output: (1, 2, 3)
# print(my_tuple[2:])   # Output: (3, 4, 5)


##### Tuple unpacking
# my_tuple = (1, 2, 3)
# a, b, c = my_tuple
# print(a)  # Output: 1
# print(b)  # Output: 2
# print(c)  # Output: 3


##### Nested tuples
# nested_tuple = (1, 2, (3, 4), 5)
# print(nested_tuple)
# print(nested_tuple[2])    # Output: (3, 4)
# print(nested_tuple[2][1]) # Output: 4



# my_tuple = (1, 2, 3, 1, 2, 1)
# print(my_tuple.count(1))  # Output: 3
# print(my_tuple.index(3))  # Output: 2


# # Function that returns multiple values
# def get_person_info():
#     name = "John Doe"
#     age = 30
#     city = "New York"
#     return name, age, city  ## when returning multiple values, they are returned as tuples

# # Unpacking the returned tuple
# person_name, person_age, person_city = get_person_info()

# print(f"Name: {person_name}")
# print(f"Age: {person_age}")
# print(f"City: {person_city}")



####  -----------------------------------------------------------------------------------------------------------
#### 
####  -----------------------------------------------------------------------------------------------------------
####  -----------------------------------------------------------------------------------------------------------
#### 
####  -----------------------------------------------------------------------------------------------------------
####  -----------------------------------------------------------------------------------------------------------
#### 
####  -----------------------------------------------------------------------------------------------------------