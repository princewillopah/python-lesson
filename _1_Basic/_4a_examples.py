print()
print("----------------------------------------------------------------------------------------")
print()
# A list is a collection which is ordered and changeable. In Python lists are written with square brackets.
# Lists allow duplicate members.
# i need you to draft question that has solution based on the solution below
### ========================================================================================
### Lists in Python
### ========================================================================================
## Question:
# Given the list deployment_targets = ['us-east-1', 'eu-west-1', 'ap-southeast-2'], what happens when you run the following operations:
# 1. Print the first element.
# 2. Append 'us-west-2'.
# 3. Replace the second element with 'eu-central-1'.
# 4. Print the final list.

## Solution:
# deployment_targets = ['us-east-1', 'eu-west-1', 'ap-southeast-2']
# print(deployment_targets[0])
# deployment_targets.append('us-west-2')
# deployment_targets[1]= 'eu-central-1'
# print(deployment_targets)

### ========================================================================================
### 30 questions on List operations with solutions
### ========================================================================================
# 1. Merge and Sort: Merge two sorted lists A = [1, 3, 5] and B = [2, 4, 6]. Sort the result.
# 2. Remove Duplicates: Remove duplicates from [1, 2, 2, 3, 4, 4, 5].
# 3. Common Elements: Find common elements in [1, 2, 3, 4] and [3, 4, 5, 6].
# 4. Flatten List: Flatten [[1, 2], [3, 4], [5]] into [1, 2, 3, 4, 5].
# 5. Rotate List: Rotate [1, 2, 3, 4] right by 2 positions.
# 6. Find Missing: Find missing numbers in [1, 2, 4, 6] if sequence is 1-6.
# 7. Pair Sum: Find pairs in [1, 2, 3, 4, 5] that sum to 7.
# 8. Max Consecutive: Find max consecutive 1s in [1, 1, 0, 1, 1, 1].
# 9. Sublist Sum: Check if any sublist sums to 10 in [1, 2, 3, 4, 5].
# 10. Move Zeroes: Move zeroes to end of [1, 0, 2, 0, 3].

# 1. Merge Overlapping Intervals: Merge intervals in [[1, 3], [2, 4], [5, 7]].
# 2. Remove Duplicates in Place: Remove duplicates from [1, 1, 2, 2, 3] in-place, return new length.
# 3. Intersection of Three Lists: Find common in [1, 2, 3, 4], [2, 3, 4, 5], [3, 4, 5, 6].
# 4. Nested List Sum: Sum all numbers in [[1, 2], [3, [4]], 5].
# 5. Rotate Matrix: Rotate 2D list [[1, 2], [3, 4]] 90° clockwise.
# 6. Find Missing in Range: Find missing in [4, 2, 1, 5] if range is 1-5.
# 7. Three Sum: Find triplets in [1, 2, 3, 4, 5] summing to 9.
# 8. Longest Consecutive Sequence: Find longest in [1, 3, 5, 2, 4, 6].
# 9. Subarray with Given Sum: Find subarray summing to 7 in [1, 2, 3, 4, 5].
# 10. Group Anagrams: Group ['eat', 'tea', 'tan', 'ate'] by anagram.

# 1. Merge Overlapping CIDR Blocks: Merge [10.0.0.0/24, 10.0.1.0/24, 10.0.2.0/23].
# 2. Find Unused Subnets: Given VPC CIDR 10.0.0.0/16, find unused in [10.0.1.0/24, 10.0.2.0/24].
# 3. Group EC2 by Subnet: Group EC2 IDs by subnet from [{id: i-1, subnet: subnet-1}, {id: i-2, subnet: subnet-2}, {id: i-3, subnet: subnet-1}].
# 4. Prioritize Route Tables: Sort route tables by most specific CIDR [10.0.0.0/16, 10.0.1.0/24, 0.0.0.0/0].
# 5. Find Overlapping SG Rules: Find overlapping rules in SGs [{cidr: 10.0.0.0/16, port: 80}, {cidr: 10.0.1.0/24, port: 80}].
# 6. Subnet Allocation: Allocate next free /28 subnet in 10.0.0.0/16.
# 7. Missing AZs: Find missing AZs in [us-east-1a, us-east-1b] vs. VPC’s [us-east-1a, us-east-1b, us-east-1c].
# 8. SG Rule Cleanup: Remove redundant rules (e.g., 0.0.0.0/0 makes others redundant).
# 9. ENI Attachments: Group EC2 IDs by ENI from [{eni: eni-1, id: i-1}, {eni: eni-2, id: i-2}, {eni: eni-1, id: i-3}].
# 10. Route Optimization: Optimize routes [10.0.0.0/16 -> igw, 10.0.1.0/24 -> nat] (remove redundant).
































### ========================================================================================
### 
### ======================================================================================== 


# type()  --  finds the types of a list
# len()   --- finds the length of the list
# id()  --  finds the memory location of the list 
# list-name[:]   ---   slices the lis with an index
# index()   ---  find the index of an item in a list
# count()  --   counts the number of times an item is in a list


### ----------------------------------------------------------------------------------------------------------
### Modifying a list or chaning the item of the list
### ----------------------------------------------------------------------------------------------------------
# append(): Adds a single element to the end of the list.
# insert(): Inserts an element at a specified index.
# extend(): Adds all elements of an iterable to the end of the list.
# clear(): Removes all elements from the list.
# del(): Deletes an element or slice from the list.
# copy(): Returns a shallow copy of the list.
# remove(): Removes the first occurrence of a specified value.
# pop(): Removes and returns an element at a specified index (or the last item if no index is given).
# sort(): Sorts the list in ascending or custom order.
# reverse(): Reverses the elements of the list.



# append():




















### ========================================================================================
### 
### ========================================================================================

# my_list = [14, 79, 57, 72, 73, 93, 39, 58, 43, 100, 5, 97, 3, 1, 20, 88, 85, 88, 87, 52, 32, 14, 51, 28, 74, 22, 10, 88, 27, 80, 1, 23, 79]
# print(f"{my_list[2]} is at index 2")  #list[index] --  Fetches value at index 2 (30)
# print(f"first occurrence of 88 is at position {my_list.index(88)}") 
# print(f"88 appears {my_list.count(20)} times in the list")
# print(f"{20 in my_list}")  ## in -  return true because 20 is in the list
# print(f"id = {id(my_list)}")
# print(f"first occurrence of 20 is at position {my_list.index(20)}")
# print(f"first occurrence of 20 is at position {my_list.index(20)}")



### ----------------------------------------------------------------------------------------------------------
### append(): Adds a single element to the end of the list.
### ------------------------------------------------------------------------------------------------------------

# my_list = [1, 2, 3]
# my_list.append(4)
# print(my_list)  # [1, 2, 3, 4]





### ----------------------------------------------------------------------------------------------------------
### insert(): Inserts an element at a specified index.
### ------------------------------------------------------------------------------------------------------------
# my_list = [1, 2, 4]
# my_list.insert(2, 3)
# print(my_list)  # [1, 2, 3, 4]






### ----------------------------------------------------------------------------------------------------------
### extend(): Adds all elements of an iterable to the end of the list.
### ------------------------------------------------------------------------------------------------------------
# my_list = [1, 2]
# my_list.extend([3, 4])
# print(my_list)  # [1, 2, 3, 4]






### ----------------------------------------------------------------------------------------------------------
### clear(): Removes all elements from the list.
### ------------------------------------------------------------------------------------------------------------
# my_list = [1, 2, 3]
# my_list.clear()
# print(my_list)  # []






### ----------------------------------------------------------------------------------------------------------
### del(): Deletes an element or slice from the list.
### ------------------------------------------------------------------------------------------------------------
# my_list = [1, 2, 3, 4]
# del my_list[2]
# print(my_list)  # [1, 2, 4]






### ----------------------------------------------------------------------------------------------------------
### copy(): Returns a shallow copy of the list.
### ------------------------------------------------------------------------------------------------------------
# my_list = [1, 2, 3]
# new_list = my_list.copy()
# print(new_list)  # [1, 2, 3]






### ----------------------------------------------------------------------------------------------------------
### remove(): Removes the first occurrence of a specified value.
### ------------------------------------------------------------------------------------------------------------

# my_list = [1, 2, 3, 2]
# my_list.remove(2)
# print(my_list)  # [1, 3, 2]





### ----------------------------------------------------------------------------------------------------------
### pop(): Removes and returns an element at a specified index (or the last item if no index is given).
### ------------------------------------------------------------------------------------------------------------

# my_list = [1, 2, 3]
# popped_value = my_list.pop(1)
# print(my_list)  # [1, 3]
# print(popped_value)  # 2





### ----------------------------------------------------------------------------------------------------------
### sort(): Sorts the list in ascending or custom order.
### ------------------------------------------------------------------------------------------------------------
# my_list = [3, 1, 2]
# my_list.sort()
# print(my_list)  # [1, 2, 3]






### ----------------------------------------------------------------------------------------------------------
### reverse(): Reverses the elements of the list.
### ------------------------------------------------------------------------------------------------------------
# my_list = [1, 2, 3]
# my_list.reverse()
# print(my_list)  # [3, 2, 1]









### ========================================================================================
###
### ========================================================================================






### ========================================================================================
### 
### ========================================================================================






### ========================================================================================
### 
### ========================================================================================





### ========================================================================================
### 
### ======================================================================================== 




### ========================================================================================
### 
### ======================================================================================== 














































































































print()
print("----------------------------------------------------------------------------------------")
print()