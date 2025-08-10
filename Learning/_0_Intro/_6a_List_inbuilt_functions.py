import os
os.system('clear')
print("----------------------------------------------------------------------------------------")
print(" RESULTS")
print("----------------------------------------------------------------------------------------")
print()
print()

import random









num = [1, 4, 2, 9, 7, 8, 9, 3, 1]
# generate numbers of numbers of 30 items 
# generate a list of 30 random integers between 1 and 10
num = [random.randint(1, 10) for _ in range(30)]
# num = [1, 4, 2, 9, 7, 8, 9, 3, 1]  # Example list for demonstration
# Original list
print("Original list:", num)

# Sort the list in ascending order
num.sort()
print("Sorted list (ascending):", num)

# Sort the list in descending order
num.sort(reverse=True)
print("Sorted list (descending):", num)

# Append 4 to the list
num.append(4)
print("After appending 4:", num)

# Count the occurrences of 1 in the list
count_ones = num.count(1)
print("Count of 1:", count_ones)

# Extend the list by adding another list [4]
num.extend([4])
print("After extending with [4]:", num)

# Insert 4 at index 3
num.insert(3, 4)
print("After inserting 4 at index 3:", num)

# Find the index of the first occurrence of 2
index_of_2 = num.index(2)
print("Index of 2:", index_of_2)

# Remove the first occurrence of 2
num.remove(2)
print("After removing the first occurrence of 2:", num)

# Pop the element at index 2
popped_element = num.pop(2)
print("Element popped from index 2:", popped_element)
print("List after popping element at index 2:", num)

# Reverse the list
num.reverse()
print("List after reversing:", num)

# Make a copy of the list
num_copy = num.copy()
print("Copy of the list:", num_copy)

# Length of the list
length = len(num)
print("Length of the list:", length)

# Minimum value in the list
min_value = min(num)
print("Minimum value in the list:", min_value)

# Maximum value in the list
max_value = max(num)
print("Maximum value in the list:", max_value)

# Clear the list
num.clear()
print("List after clearing:", num)

# provide other functions not here
# Additional functions not included in the original code:

# - pop()
# - copy()



# Explanation:
# 1. Original list: Print the original list.
# 2. Sorting:
#     - Sort the list in ascending order and print it.
#     - Sort the list in descending order and print it.
# 3. Append: Add 4 to the end of the list and print the result.
# 4. Count: Count the occurrences of 1 in the list and print the count.
# 5. Extend: Add elements of [4] to the end of the list and print the result.
# 6. Insert: Insert 4 at index 3 and print the result.
# 7. Index: Find the index of the first occurrence of 2 and print the index.
# 8. Remove: Remove the first occurrence of 2 from the list and print the result.
# 9. Pop: Remove and print the element at index 2. Also, print the list after popping the element.
# 10. Reverse: Reverse the list and print it.
# 11. Copy: Make a copy of the list and print the copied list.
# 12. Length: Print the length of the list.
# 13. Min and Max: Print the minimum and maximum values in the list.
# 14. Clear: Clear the list and print the result.



print()
print()
print()
print()
print("----------------------------------------------------------------------------------------")