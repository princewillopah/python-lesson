
# # List is a collection of items
# num1 = [5, 10, 13, 15, 16, 13, 26, 48, 34, 67, 89, 30, 42, 35, 30, 13, 13, 25, 15, 15, 15]
# #       0  1   2   3   4   5   6   7   8   9   10  11  12  13  14  15  16  17  18  19  20
# #     -21 -20 -19 -18 -17 -16 -15 -14 -13 -12 -11 -10  -9  -8  -7  -6  -5  -4  -3  -2  -1  

# # Append an element
# num1.append(100)
# print("After append:", num1)

# # Extend the list
# num1.extend([101, 102])
# print("After extend:", num1)

# # Insert an element
# num1.insert(2, 200)
# print("After insert:", num1)

# # Remove an element - this will remove this first occurencies of 13
# num1.remove(13)
# print("After remove:", num1)

# # Pop an element
# popped_element = num1.pop()
# print("After pop:", num1, "Popped element:", popped_element)
# popped_element = num1.pop(5)
# print("After pop:", num1, "Popped element:", popped_element)
# # Get the index of an element
# index = num1.index(15)
# print("Index of 15:", index)

# index = num1.index(30,13,17) # index(search-item,startinf-index,ending-index)
# print(f"Index of 30 between {num1[13:17]}:", index)
# index = num1.index(30,13)
# print(f"Index of 30 between {num1[13:17]}:", index)
# # Count the occurrences of an element
# count_15 = num1.count(15)
# print("Count of 15:", count_15)

# # Sort the list
# num1.sort()
# print("After sort:", num1)

# # Reverse the list
# num1.reverse()
# print("After reverse:", num1)

# # Copy the list
# num1_copy = num1.copy()
# print("Copy of num1:", num1_copy)


# del num1_copy[1]
# print(f"After deleting iem with index of 1:",num1_copy)

# del num1_copy[:5]
# print(f"After deleting {num1_copy[:5]}:",num1_copy)

# # Clear the list
# num1_copy.clear()
# print("After clear:", num1_copy)





# # Length of the list
# length = len(num1)
# print("Length of num1:", length)

# # List comprehension
# squares = [x**2 for x in num1]
# print("Squares:", squares)

# print()
# # Check for element existence
# exists = 15 in num1
# print("15 exists in num1:", exists)

# # Concatenate lists
# num2 = [200, 300]
# combined = num1 + num2
# print("Combined list:", combined)

# # Repeat lists
# repeated = num1 * 2
# print("Repeated list:", repeated)

# # Find the maximum value
# max_value = max(num1)
# print("Maximum value:", max_value)

# # Find the minimum value
# min_value = min(num1)
# print("Minimum value:", min_value)

# # Sum of elements
# total_sum = sum(num1)
# print("Sum of elements:", total_sum)

# # Convert list to string
# num1_str = ' '.join(map(str, num1))
# print("List as string:", num1_str)

# # Convert string to list
# s = "1,2,3,4,5"
# num_list = s.split(',')
# print("String to list:", num_list)

# # List comprehension with condition
# even_squares = [x**2 for x in num1 if x % 2 == 0]
# print("Squares of even numbers:", even_squares)

# # Nested list comprehension
# matrix = [[i + j for j in range(3)] for i in range(3)]
# print("3x3 matrix:", matrix)

# # Flatten a nested list
# nested_list = [[1, 2, 3], [4, 5], [6, 7, 8]]
# flat_list = [item for sublist in nested_list for item in sublist]
# print("Flattened list:", flat_list)

# # Filter elements in a list
# filtered = list(filter(lambda x: x > 20, num1))
# print("Filtered elements greater than 20:", filtered)

# # Map function
# doubled = list(map(lambda x: x * 2, num1))
# print("Doubled elements:", doubled)

# # Reduce function
# from functools import reduce
# product = reduce(lambda x, y: x * y, num1)
# print("Product of all elements:", product)





####  ------------------------------------------------------------------------------------------------------------------
####  find the sum and avarage of a list of items
####  ------------------------------------------------------------------------------------------------------------------
# num1 = [5, 10, 13, 15, 16, 13, 26, 48, 34, 67, 89, 30, 42, 35, 30, 13, 13, 25, 15, 15, 15]

# def mysum(my_list):
#     sum = 0
#     for i in my_list:
#         sum += i  #sum=sum+1
#     return sum

# def my_average(mylist):
#     return mysum(mylist)/len(mylist)

# print(f"List of Items: {num1}")
# print(f"Sum: {mysum(num1)}")
# print(f"Average: {my_average(num1)}")

####  ------------------------------------------------------------------------------------------------------------------
####  Return 2 list - odd list and even list from a general list
####  ------------------------------------------------------------------------------------------------------------------
# num1 = [5, 10, 13, 15, 16, 13, 26, 48, 34, 67, 89, 30, 42, 35, 30, 13, 13, 25, 15, 15, 15]

# def my_even_fun(mylist):
#     even_list = []
#     odd_list = []
#     for i in mylist:
#         if i%2==0:
#             even_list.append(i)
#         else:
#             odd_list.append(i)
#     return even_list,odd_list   # Return the two lists as a tuple --  ([10, 16, 26, 48, 34, 30, 42, 30], [5, 13, 15, 13, 67, 89, 35, 13, 13, 25, 15, 15, 15])


# even_list, odd_list = my_even_fun(num1)   # Call the function and unpack the returned tuple into two separate lists

# print(f"Main List: {num1}")
# print(f"Even List: {even_list}")
# print(f"Odd List: {odd_list}")



####  ------------------------------------------------------------------------------------------------------------------
####  get the largest/smllest item from a list
####  ------------------------------------------------------------------------------------------------------------------
# num1 = [5, 10, 13, 15, 16, 13, 26, 48, 34, 67, 89, 30, 42, 35, 30, 13, 13, 25, 15, 15, 15]
# def getSmallestNum(list,compared_num):
#     larger_numbers_list = []
#     smaller_numbers_list = []

#     for i in list:
#         if i <= compared_num:
#             smaller_numbers_list.append(i)
#         else:
#             larger_numbers_list.append(i)
#     return smaller_numbers_list,larger_numbers_list

# large_list,small_list = getSmallestNum(num1,16)
# print(f"Main List: {num1}")
# print(f"smaller Numbers List: {large_list}")
# print(f"larger Numbers List: {small_list}")


####  ------------------------------------------------------------------------------------------------------------------
####  largest number and smallest
####  ------------------------------------------------------------------------------------------------------------------
# num1 = [5, 10, 13, 15, 16, 13, 26, 48, 34, 67, 89, 30, 42, 35, 30, 13, 13, 25, 15, 15, 2, 15]
# def getSmallestNum(list):
#    if not list:  ##this part handles situation when list is empty by returing nothing
#         return None
#    else:
#     largest_num = num1[0]   #  assigned the first item
#     smallestNum = num1[0]   #  assigned the first item

#     for i in list:

#         if largest_num < i: # this means that if i(e.g equals 10 for second iteration) is greater than largest_num(which is initially 5 in the second iteration) then
#             largest_num = i  ## make largest_num(which is 5 in the second iteration) = to the i(i = 10 here). therefor largest_num = 10 here in the second iteration
#         if smallestNum > i:  
#             smallestNum = i  
#     return largest_num,smallestNum

# largest_num, smallestNum =  getSmallestNum(num1)
# print(f"Main List: {num1}")
# print(f"Smalleest Number in the  List: {smallestNum}")
# print(f"Largest number in the list: {largest_num}")


# -------------------------------
# def largest(numbers):
#     if len(numbers) < 1:   # Check if there is at least one number
#         raise ValueError("List must contain at least 1 number")
     
#     unique_numbers = list(set(numbers))   # Remove duplicates to handle cases where the list has repeated elements
    
#     unique_numbers.sort(reverse=True)    # Sort the unique numbers in descending order
#     largest_num = unique_numbers[0]      # Get the largest number

#     unique_numbers.sort()                # Sort the unique numbers in ascending order
#     smallest_num = unique_numbers[0]     # Get the smallest number
    
#     return largest_num, smallest_num     # Return the largest and smallest numbers

# # Example usage:
# num1 = [5, 10, 13, 15, 16, 13, 26, 48, 34, 67, 89, 30, 42, 35, 30, 13, 13, 25, 15, 15, 15]
# largest_num, smallest_num = largest(num1)
# print(f"Main List: {num1}")
# print(f"Largest Number: {largest_num}")
# print(f"Smallest Number: {smallest_num}")





####  ------------------------------------------------------------------------------------------------------------------
####  second largeest and smalest
####  ------------------------------------------------------------------------------------------------------------------

###  my method ####################################################################
# num1 = [5, 10, 13, 15, 16, 13, 26, 48, 34, 67, 89, 30, 42, 35, 30, 13, 13, 25, 15, 15, 2, 15]
# num1 = []
# num1 = [20,10,5,6,7,5,20,10]
# num1 = [10.10,10,10,10]
# def getSmallestNum(list):
#    if not list: 
#         return None
#    elif len(list) <= 1:
#        return None
#    else:
#     largest_num = num1[0]   
#     smallestNum = num1[0]   
#     sec_largest = num1[0]
#     sec_smallest = num1[0]
#     for i in list:
#         if largest_num < i: # this means that if i(e.g equals 10 for second iteration) is greater than largest_num(which is initially 5 in the second iteration) then
#             largest_num = i  ## make largest_num(which is 5 in the second iteration) = to the i(i = 10 here). therefor largest_num = 10 here in the second iteration
#         if smallestNum > i:  
#             smallestNum = i  
#     list.remove(largest_num)
#     list.remove(smallestNum)
#     for i in list:
#         if sec_largest < i: # this means that if i(e.g equals 10 for second iteration) is greater than largest_num(which is initially 5 in the second iteration) then
#             sec_largest = i  ## make largest_num(which is 5 in the second iteration) = to the i(i = 10 here). therefor largest_num = 10 here in the second iteration
#         if sec_smallest > i:  
#             sec_smallest = i 
#     return sec_largest,sec_smallest

# largest_num, smallestNum =  getSmallestNum(num1)
# print(f"Main List: {num1}")
# print(f"Smalleest Number in the  List: {smallestNum}")
# print(f"Largest number in the list: {largest_num}")

################ -------------
################ Method2 : 0(n) + 0(n)
################ -------------

# num1 = [5, 10, 13, 15, 16, 13, 26, 48, 34, 67, 89, 30, 42, 35, 30, 13, 13, 25, 15, 15, 2, 15]

# def getMax(list):
#     if not list: 
#         return None
#     elif len(list) <= 1:
#        return None
#     else:
#      max = list[0]
#      for i in list:
#         if max < i:
#            max = i
#      return max

# def getSecondMax(list):
#     if not list: 
#         return None
#     elif len(list) <= 1:
#        return None
#     else:
#         largest_num = getMax(list)  # Find the largest number in the list using the getMax function
#         second_largest = None       # Initialize second_largest to None

#         # Loop through each number in the list
#         for i in list:
#             if i != largest_num:    # Check if the current number is not equal to the largest number  
#                 if second_largest == None:
#                     second_largest = i  # If second_largest is None, assign the current number to it  --- -- First check: If second_largest is None, it means we have not found any potential second largest number yet. In this case, we assign the current number i to second_largest.
#                 else:
#                     second_largest = max(second_largest, i)  # Update second_largest to be the larger of the current second_largest and the current number    ----    Otherwise: If second_largest already has a value, we update it to the larger of the current second_largest and the current number i. This ensures that second_largest always holds the second largest number found so far in the list.

#     return second_largest

# print(f"Main List: {num1}")
# print(f"Largest number in the list: {getMax(num1)}")
# print(f"Second Largest number in the list: {getSecondMax(num1)}")

################ -------------
################ Methodx
################ -------------

# def first_second_largests(numbers):
 
#     unique_numbers = list(set(numbers))   # Remove duplicates to handle cases where the list has repeated elements
    
#     if len(unique_numbers) < 2:   # Check if there are at least two unique numbers
#         raise ValueError("List must contain at least two unique numbers")

#     unique_numbers.sort(reverse=True)    # Sort the unique numbers in descending order
    
#     return unique_numbers[0], unique_numbers[1]    # Return the second largest number

# # Example usage:
# numbers = [5, 10, 13, 15, 16, 13, 26, 48, 34, 67, 89, 30, 42, 35, 30, 13, 13, 25, 15, 15, 15]

# largest, second_largest  = first_second_largests(numbers)
# print("Largest number is:", largest)
# print("Second largest number is:", second_largest)


################ -------------
################ Method3 : 0(n)
################ -------------

##### ------  ------------------------------------------

# def find_two_largest(numbers):
#     # Ensure the list is not empty and contains at least two numbers.
#     if not numbers:
#         raise ValueError("List must contain at least one number")
#     if len(numbers) == 1:
#         raise ValueError("List must contain at least two numbers")  

#     largest = second_largest = float('-inf')  # Use negative infinity to handle cases where the list contains negative numbers.

#     for number in numbers:
#         if number > largest:
#             second_largest = largest
#             largest = number
#         elif number > second_largest and number != largest:
#             second_largest = number

#     if second_largest == float('-inf'):
#         raise ValueError("List must contain at least two unique numbers")

#     return largest, second_largest

# # Example usage:
# num1 = [5, 10, 13, 15, 16, 13, 26, 48, 34, 67, 89, 30, 42, 35, 30, 13, 13, 25, 15, 15, 2, 15]
# largest, second_largest = find_two_largest(num1)
# print(f"Main List: {num1}")
# print(f"Largest number in the list: {largest}")
# print(f"Second Largest number in the list: {second_largest}")


# Step-by-Step Breakdown:
#1 Start of the Loop:
    # The loop iterates through each number in the numbers list.

#2 First Condition: if number > largest:
    # For each number, check if it is greater than the current largest.
    # If true, it means we have found a new largest number.
        # second_largest = largest
        # largest = number
    # Before updating largest, assign the current value of largest to second_largest. This ensures that second_largest holds the previous largest value.
    # Then, update largest to the new number.

# Second Condition: elif number > second_largest and number != largest:
    # This part only runs if the first condition is false (i.e., the current number is not greater than largest).
    # Check if the number is greater than second_largest and not equal to largest.
         # second_largest = number
    # If both conditions are true, update second_largest to the current number.



# Example Walkthrough:
# Consider the list [5, 10, 13, 15, 16].


# First Iteration:
# number = 5
# 5 > -inf (true), so:
# second_largest = -inf
# largest = 5
# Now, largest = 5 and second_largest = -inf.

# Second Iteration:
# number = 10
# 10 > 5 (true), so:
# second_largest = 5
# largest = 10
# Now, largest = 10 and second_largest = 5.

# Third Iteration:
# number = 13
# 13 > 10 (true), so:
# second_largest = 10
# largest = 13
# Now, largest = 13 and second_largest = 10.

# Fourth Iteration:
# number = 15
# 15 > 13 (true), so:
# second_largest = 13
# largest = 15
# Now, largest = 15 and second_largest = 13.

# Fifth Iteration:
# number = 16
# 16 > 15 (true), so:
# second_largest = 15
# largest = 16
# Now, largest = 16 and second_largest = 15.

# Summary:
# The loop ensures that largest always holds the highest number found so far.
# second_largest holds the second highest number found so far, updated only when a new largest is found or when a number greater than second_largest but not equal to largest is encountered.

####  ------------------------------------------------------------------------------------------------------------------
####  Check if a list is sorted or not
####  ------------------------------------------------------------------------------------------------------------------

# def check_if_sorted(numbers):
#     # Ensure the list is not empty and contains at least two numbers.
#     if not numbers:
#          return "yes"
#     if len(numbers) == 1:
#         return "yes"  

#     right = [0]
#     left= None

#     for number in numbers:
#         if number > largest:
#             second_largest = largest
#             largest = number
#         elif number > second_largest and number != largest:
#             second_largest = number

#     if second_largest == float('-inf'):
#         raise ValueError("List must contain at least two unique numbers")

#     return largest, second_largest

# # Example usage:
# num1 = [5, 10, 13, 15, 16, 13, 26, 48, 34, 67, 89, 30, 42, 35, 30, 13, 13, 25, 15, 15, 2, 15]
# largest, second_largest = check_if_sorted(num1)
# print(f"Main List: {num1}")
# print(f"Largest number in the list: {largest}")
# print(f"Second Largest number in the list: {second_largest}")


################ -------------
################ Method: ascending orther 
################ -------------

# def is_sorted(numbers):
#     for i in range(len(numbers) - 1):
#         if numbers[i] > numbers[i + 1]:
#             return False
#     return True

# # Example usage:
# numbers = [1, 2, 3, 4, 5]
# if is_sorted(numbers):
#     print("Yes")
# else:
#     print("No")

# numbers = [1, 3, 2, 4, 5]
# if is_sorted(numbers):
#     print("Yes")
# else:
#     print("No")

"""
for i in range(len(numbers) - 1)::

len(numbers) gives the total number of elements in the list numbers.
range(len(numbers) - 1) generates a sequence of numbers starting from 0 to len(numbers) - 2. This ensures that i goes up to the second-to-last index of the list.

For a list of length n, the indices range from 0 to n-1. We need to compare each element with the next one, so we stop at the second-to-last element to avoid going out of bounds.
if numbers[i] > numbers[i + 1]::
For each index i in the range, this line compares the current element numbers[i] with the next element numbers[i + 1].
If numbers[i] is greater than numbers[i + 1], it means the list is not sorted in non-decreasing order, so the function returns False.

return True:
If the loop completes without finding any element that is greater than the next one, it means the list is sorted. So, the function returns True.


Example Execution
Consider the list [1, 3, 2, 4, 5]:
len(numbers) is 5, so range(len(numbers) - 1) is range(4), which means the loop runs for i = 0, 1, 2, 3.
Iteration steps:
i = 0: Compare numbers[0] (1) with numbers[1] (3). Since 1 ≤ 3, continue to the next iteration.
i = 1: Compare numbers[1] (3) with numbers[2] (2). Since 3 > 2, the function returns False.

Consider the list [1, 2, 3, 4, 5]:
len(numbers) is 5, so range(len(numbers) - 1) is range(4), which means the loop runs for i = 0, 1, 2, 3.
Iteration steps:
i = 0: Compare numbers[0] (1) with numbers[1] (2). Since 1 ≤ 2, continue to the next iteration.
i = 1: Compare numbers[1] (2) with numbers[2] (3). Since 2 ≤ 3, continue to the next iteration.
i = 2: Compare numbers[2] (3) with numbers[3] (4). Since 3 ≤ 4, continue to the next iteration.
i = 3: Compare numbers[3] (4) with numbers[4] (5). Since 4 ≤ 5, continue to the next iteration.

Since the loop completes without finding any unordered pairs, the function returns True.


"""
################ -------------
################ Method : 
################ -------------
# def is_sorted(numbers):
#     i = 0
#     while i < len(numbers) - 1:
#         if numbers[i] > numbers[i + 1]:
#             return False
#         i += 1
#     return True

# # Example usage:
# numbers1 = [1, 2, 3, 4, 5]
# if is_sorted(numbers1):
#     print("Yes")
# else:
#     print("No")

# numbers2 = [1, 3, 2, 4, 5]
# if is_sorted(numbers2):
#     print("Yes")
# else:
#     print("No")

"""
Explanation:

i = 0:
Initialize the index i to 0, starting from the first element of the list.

while i < len(numbers) - 1::
This loop will continue as long as i is less than the length of the list minus one, ensuring we only compare elements within valid indices.

if numbers[i] > numbers[i + 1]::
For each index i, compare the current element numbers[i] with the next element numbers[i + 1].
If numbers[i] is greater than numbers[i + 1], it means the list is not sorted, so the function returns False.

i += 1:
Increment i to move to the next element in the list.

return True:
If the loop completes without finding any unordered pairs, it means the list is sorted, so the function returns True.
Example Execution

Consider the list [1, 3, 2, 4, 5]:
i = 0: Compare numbers[0] (1) with numbers[1] (3). Since 1 ≤ 3, continue to the next iteration (i becomes 1).
i = 1: Compare numbers[1] (3) with numbers[2] (2). Since 3 > 2, the function returns False.

Consider the list [1, 2, 3, 4, 5]:
i = 0: Compare numbers[0] (1) with numbers[1] (2). Since 1 ≤ 2, continue to the next iteration (i becomes 1).
i = 1: Compare numbers[1] (2) with numbers[2] (3). Since 2 ≤ 3, continue to the next iteration (i becomes 2).
i = 2: Compare numbers[2] (3) with numbers[3] (4). Since 3 ≤ 4, continue to the next iteration (i becomes 3).
i = 3: Compare numbers[3] (4) with numbers[4] (5). Since 4 ≤ 5, continue to the next iteration (i becomes 4).


Since the loop completes without finding any unordered pairs, the function returns True.
"""

################ -------------------------------------
################ Method : using sorted function
################ -------------------------------------
# while sort() modifies the list to give you the sorted list, sorted() creates a new sorted list 

# def is_sorted(mylist):
#     sorted_list = sorted(mylist)
#     # sorted_list = mylist.sort()
#     if sorted_list != mylist:
#         return False
#     return True

# numbers1 = [1, 2, 3, 4, 5]
# if is_sorted(numbers1):
#     print("Yes")
# else:
#     print("No")

# numbers2 = [1, 3, 2, 4, 5]
# if is_sorted(numbers2):
#     print("Yes")
# else:
#     print("No")


####  ------------------------------------------------------------------------------------------------------------------
####  Check if a list is sorted or not
####  ------------------------------------------------------------------------------------------------------------------

################ -------------
################ Method : 
################ -------------


################ -------------
################ Method : 
################ -------------

################ -------------
################ Method : 
################ -------------

####  ------------------------------------------------------------------------------------------------------------------
####  Missing number
####  ------------------------------------------------------------------------------------------------------------------
### Question:Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array

def find_missing_number(nums):
    n = len(nums)
    total_sum = n * (n + 1) // 2
    list_sum = sum(nums)
    missing_number = total_sum - list_sum
    return missing_number

# Example usage:
nums = [4,3,6,8,0,2]
print(find_missing_number(nums))  # Output: 2






################ -------------
################ Method : 
################ -------------


################ -------------
################ Method : 
################ -------------

################ -------------
################ Method : 
################ -------------

####  ------------------------------------------------------------------------------------------------------------------
####  
####  ------------------------------------------------------------------------------------------------------------------

################ -------------
################ Method : 
################ -------------


################ -------------
################ Method : 
################ -------------

################ -------------
################ Method : 
################ -------------

####  ------------------------------------------------------------------------------------------------------------------
####  
####  ------------------------------------------------------------------------------------------------------------------

################ -------------
################ Method : 
################ -------------


################ -------------
################ Method : 
################ -------------

################ -------------
################ Method : 
################ -------------

####  ------------------------------------------------------------------------------------------------------------------
####  
####  ------------------------------------------------------------------------------------------------------------------

################ -------------
################ Method : 
################ -------------


################ -------------
################ Method : 
################ -------------

################ -------------
################ Method : 
################ -------------

####  ------------------------------------------------------------------------------------------------------------------
####  
####  ------------------------------------------------------------------------------------------------------------------


####  ------------------------------------------------------------------------------------------------------------------
####  Check if a list is sorted or not
####  ------------------------------------------------------------------------------------------------------------------

################ -------------
################ Method : 
################ -------------


################ -------------
################ Method : 
################ -------------

################ -------------
################ Method : 
################ -------------

####  ------------------------------------------------------------------------------------------------------------------
####  
####  ------------------------------------------------------------------------------------------------------------------

################ -------------
################ Method : 
################ -------------


################ -------------
################ Method : 
################ -------------

################ -------------
################ Method : 
################ -------------

####  ------------------------------------------------------------------------------------------------------------------
####  
####  ------------------------------------------------------------------------------------------------------------------

################ -------------
################ Method : 
################ -------------


################ -------------
################ Method : 
################ -------------

################ -------------
################ Method : 
################ -------------

####  ------------------------------------------------------------------------------------------------------------------
####  
####  ------------------------------------------------------------------------------------------------------------------

################ -------------
################ Method : 
################ -------------


################ -------------
################ Method : 
################ -------------

################ -------------
################ Method : 
################ -------------

####  ------------------------------------------------------------------------------------------------------------------
####  
####  ------------------------------------------------------------------------------------------------------------------

################ -------------
################ Method : 
################ -------------


################ -------------
################ Method : 
################ -------------

################ -------------
################ Method : 
################ -------------

####  ------------------------------------------------------------------------------------------------------------------
####  
####  ------------------------------------------------------------------------------------------------------------------





####  ------------------------------------------------------------------------------------------------------------------
####  Check if a list is sorted or not
####  ------------------------------------------------------------------------------------------------------------------

################ -------------
################ Method : 
################ -------------


################ -------------
################ Method : 
################ -------------

################ -------------
################ Method : 
################ -------------

####  ------------------------------------------------------------------------------------------------------------------
####  
####  ------------------------------------------------------------------------------------------------------------------

################ -------------
################ Method : 
################ -------------


################ -------------
################ Method : 
################ -------------

################ -------------
################ Method : 
################ -------------

####  ------------------------------------------------------------------------------------------------------------------
####  
####  ------------------------------------------------------------------------------------------------------------------

################ -------------
################ Method : 
################ -------------


################ -------------
################ Method : 
################ -------------

################ -------------
################ Method : 
################ -------------

####  ------------------------------------------------------------------------------------------------------------------
####  
####  ------------------------------------------------------------------------------------------------------------------

################ -------------
################ Method : 
################ -------------


################ -------------
################ Method : 
################ -------------

################ -------------
################ Method : 
################ -------------

####  ------------------------------------------------------------------------------------------------------------------
####  
####  ------------------------------------------------------------------------------------------------------------------

################ -------------
################ Method : 
################ -------------


################ -------------
################ Method : 
################ -------------

################ -------------
################ Method : 
################ -------------

####  ------------------------------------------------------------------------------------------------------------------
####  
####  ------------------------------------------------------------------------------------------------------------------





####  ------------------------------------------------------------------------------------------------------------------
####  Check if a list is sorted or not
####  ------------------------------------------------------------------------------------------------------------------

################ -------------
################ Method : 
################ -------------


################ -------------
################ Method : 
################ -------------

################ -------------
################ Method : 
################ -------------

####  ------------------------------------------------------------------------------------------------------------------
####  
####  ------------------------------------------------------------------------------------------------------------------

################ -------------
################ Method : 
################ -------------


################ -------------
################ Method : 
################ -------------

################ -------------
################ Method : 
################ -------------

####  ------------------------------------------------------------------------------------------------------------------
####  
####  ------------------------------------------------------------------------------------------------------------------

################ -------------
################ Method : 
################ -------------


################ -------------
################ Method : 
################ -------------

################ -------------
################ Method : 
################ -------------

####  ------------------------------------------------------------------------------------------------------------------
####  
####  ------------------------------------------------------------------------------------------------------------------

################ -------------
################ Method : 
################ -------------


################ -------------
################ Method : 
################ -------------

################ -------------
################ Method : 
################ -------------

####  ------------------------------------------------------------------------------------------------------------------
####  
####  ------------------------------------------------------------------------------------------------------------------

################ -------------
################ Method : 
################ -------------


################ -------------
################ Method : 
################ -------------

################ -------------
################ Method : 
################ -------------

####  ------------------------------------------------------------------------------------------------------------------
####  
####  ------------------------------------------------------------------------------------------------------------------





####  ------------------------------------------------------------------------------------------------------------------
####  Check if a list is sorted or not
####  ------------------------------------------------------------------------------------------------------------------

################ -------------
################ Method : 
################ -------------


################ -------------
################ Method : 
################ -------------

################ -------------
################ Method : 
################ -------------

####  ------------------------------------------------------------------------------------------------------------------
####  
####  ------------------------------------------------------------------------------------------------------------------

################ -------------
################ Method : 
################ -------------


################ -------------
################ Method : 
################ -------------

################ -------------
################ Method : 
################ -------------

####  ------------------------------------------------------------------------------------------------------------------
####  
####  ------------------------------------------------------------------------------------------------------------------

################ -------------
################ Method : 
################ -------------


################ -------------
################ Method : 
################ -------------

################ -------------
################ Method : 
################ -------------

####  ------------------------------------------------------------------------------------------------------------------
####  
####  ------------------------------------------------------------------------------------------------------------------

################ -------------
################ Method : 
################ -------------


################ -------------
################ Method : 
################ -------------

################ -------------
################ Method : 
################ -------------

####  ------------------------------------------------------------------------------------------------------------------
####  
####  ------------------------------------------------------------------------------------------------------------------

################ -------------
################ Method : 
################ -------------


################ -------------
################ Method : 
################ -------------

################ -------------
################ Method : 
################ -------------

####  ------------------------------------------------------------------------------------------------------------------
####  
####  ------------------------------------------------------------------------------------------------------------------





####  ------------------------------------------------------------------------------------------------------------------
####  Check if a list is sorted or not
####  ------------------------------------------------------------------------------------------------------------------

################ -------------
################ Method : 
################ -------------


################ -------------
################ Method : 
################ -------------

################ -------------
################ Method : 
################ -------------

####  ------------------------------------------------------------------------------------------------------------------
####  
####  ------------------------------------------------------------------------------------------------------------------

################ -------------
################ Method : 
################ -------------


################ -------------
################ Method : 
################ -------------

################ -------------
################ Method : 
################ -------------

####  ------------------------------------------------------------------------------------------------------------------
####  
####  ------------------------------------------------------------------------------------------------------------------

################ -------------
################ Method : 
################ -------------


################ -------------
################ Method : 
################ -------------

################ -------------
################ Method : 
################ -------------

####  ------------------------------------------------------------------------------------------------------------------
####  
####  ------------------------------------------------------------------------------------------------------------------

################ -------------
################ Method : 
################ -------------


################ -------------
################ Method : 
################ -------------

################ -------------
################ Method : 
################ -------------

####  ------------------------------------------------------------------------------------------------------------------
####  
####  ------------------------------------------------------------------------------------------------------------------

################ -------------
################ Method : 
################ -------------


################ -------------
################ Method : 
################ -------------

################ -------------
################ Method : 
################ -------------

####  ------------------------------------------------------------------------------------------------------------------
####  
####  ------------------------------------------------------------------------------------------------------------------







################ -------------
################ Method : 
################ -------------

"""

"""

################ -------------
################ Method : 
################ -------------

"""

"""

################ -------------
################ Method : 
################ -------------

"""

"""

################ -------------
################ Method : 
################ -------------

"""

"""


################ -------------
################ Method : 
################ -------------

"""

"""

################ -------------
################ Method : 
################ -------------

"""

"""

################ -------------
################ Method : 
################ -------------

"""

"""

################ -------------
################ Method : 
################ -------------

"""

"""