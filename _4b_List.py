num = [1, 4, 2, 9, 7, 8, 9, 3, 1]

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
