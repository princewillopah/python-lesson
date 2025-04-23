import os
os.system('cls')
print("----------------------------------------------------------------------------------------")
print(" RESULTS")
print("----------------------------------------------------------------------------------------")
print()
print()



























### ========================================================================================
### Whileloop examples
### ========================================================================================




### --------------------------------------
### Iterating Through a List with a While Loop
### --------------------------------------
"""

Explanation:
    i is the index that starts at 0 and increases with each loop iteration.
    The loop runs while i is less than the length of the list, allowing it to print each element.
"""

fruits = ["Apple", "Banana", "Cherry", "Paw Paw", "Pineapple"]   #
 #          i = 0    i = 1     i = 2     i = 3      i = 4


# for i in fruits:
#     print(i)


# i = 0

# while i < len(fruits):
#     print(fruits[i])
#     i += 1

n=0
while 5 > n:
    print(" i am good")
    n = n + 1



### --------------------------------------
### Example 2: Summing All Numbers in a List
### --------------------------------------
"""
Explanation:

Each number in the list is added to total.
i increments each time to move to the next item in the list.
"""
# numbers = [10, 20, 30, 40]
# i = 0
# total = 0

# while i < len(numbers):
#     total += numbers[i]
#     i += 1

# print("Total sum:", total)








### --------------------------------------
### Removing Items from a List
### --------------------------------------
"""
This example removes items one by one from the list until it is empty.

Explanation:
tasks.pop(0) removes the first item each time the loop runs.
The loop continues until tasks is empty.


"""
# tasks = ["clean", "cook", "study"]
# while tasks:
#     task = tasks.pop(0)  # Removes the first item in the list
#     print(f"Task '{task}' completed!")
# print("All tasks are done!")







### --------------------------------------
### Filtering Even Numbers from a List
### --------------------------------------
"""
This example creates a new list with only the even numbers

Explanation:
If the number at numbers[i] is even (i.e., divisible by 2), it is added to even_numbers.
This continues until all items are checked.
"""
# numbers = [1, 2, 3, 4, 5, 6]
# i = 0
# even_numbers = []

# while i < len(numbers):
#     if numbers[i] % 2 == 0:
#         even_numbers.append(numbers[i])
#     i += 1

# print("Even numbers:", even_numbers)












### --------------------------------------
### Example 5: Counting Specific Items in a List
### --------------------------------------
"""
This example counts how many times a specific item (e.g., "apple") appears in a list.
Explanation:

Each time the item "apple" is found, apple_count is incremented by 1.
The loop finishes after checking all items.

"""
# fruits = ["apple", "banana", "apple", "cherry", "apple"]
# i = 0
# apple_count = 0

# while i < len(fruits):
#     if fruits[i] == "apple":
#         apple_count += 1
#     i += 1

# print("Number of apples:", apple_count)







### --------------------------------------
### Reversing a List
### --------------------------------------
"""
This example uses a while loop to reverse the elements of a list.
Explanation:

i starts at the last index and decreases by 1 each time.
Each element is added to reversed_numbers in reverse order
"""

# numbers = [1, 2, 3, 4, 5]
# reversed_numbers = []
# i = len(numbers) - 1  # Start from the last index

# while i >= 0:
#     reversed_numbers.append(numbers[i])
#     i -= 1

# print("Reversed list:", reversed_numbers)





### --------------------------------------
### Finding the Maximum Value in a List
### --------------------------------------
"""
This example finds the largest number in a list.
Explanation:

max_value keeps track of the largest number found.
Each number in the list is compared to max_value, updating it if a larger number is found

"""

# numbers = [7, 10, 4, 15, 3]
# i = 0
# max_value = numbers[0]  # Start with the first item

# while i < len(numbers):
#     if numbers[i] > max_value:
#         max_value = numbers[i]
#     i += 1

# print("Maximum value:", max_value)






### --------------------------------------
### Removing Specific Items Until None Remain
### --------------------------------------
"""
This example removes a specific item (e.g., "apple") from a list until it’s no longer present.
Explanation:

The loop continues removing "apple" from fruits as long as it exists in the list.
"""

# fruits = ["apple", "banana", "apple", "cherry", "apple"]
# while "apple" in fruits:
#     fruits.remove("apple")

# print("List after removing apples:", fruits)








### --------------------------------------
### Moving Items from One List to Another
### --------------------------------------
"""

This example moves items from one list to another until the first list is empty.
Explanation:

Each item is removed from pending_tasks and added to completed_tasks until pending_tasks is empty.
"""
# pending_tasks = ["task1", "task2", "task3"]
# completed_tasks = []

# while pending_tasks:
#     task = pending_tasks.pop(0)  # Take the first task
#     completed_tasks.append(task)  # Move it to completed
#     print(f"Completed: {task}")

# print("All tasks completed:", completed_tasks)









### --------------------------------------
### 
### --------------------------------------
"""

"""








### --------------------------------------
### 
### --------------------------------------
"""

"""









### --------------------------------------
### Basic Counter with a While Loop
### --------------------------------------
"""
This loop will print numbers from 1 to 5.

Explanation: The loop runs as long as count is less than or equal to 5. Each time, it adds 1 to count until count is greater than 5.
"""

# name = "Jane"
# age = 1 #Jane's age
# while age <= 18:
#     print(f"{name} is still a teen at {age} years old")
#     age = age + 2  # Increments age by 1 each time







### --------------------------------------
### Asking for a Password Until Correct
### --------------------------------------
"""

This loop keeps asking the user for the correct password.
Explanation: The loop keeps running until the user enters "open123". When they do, the loop stops, and it prints “Access granted!”
"""


# password = ""
# username = ""
# while password != "open123" and username != "moriah":
#     username = input("Enter the Username: ")
#     password = input("Enter the password: ")
# print("Access granted!")





### --------------------------------------
### Simple Guessing Game
### --------------------------------------
"""

This loop asks the user to guess a number until they guess correctly.

Explanation: The loop continues as long as the guess is not equal to secret_number. It will keep prompting the user until they guess the correct number.
"""


# secret_number = 7
# guess = 0

# while guess != secret_number:
#     guess = int(input("Guess the number (between 1 and 10): "))
#     if guess == secret_number:
#         print("Correct! You guessed it.")
#     elif guess < 1:
#         print(f"""You entered {guess}. I said the number is between 1 and 10 inlusive.
#               Try again!""")
#     elif guess > 10:
#         print(f"""You entered {guess}. I said the number is between 1 and 10 inlusive.
#               Try again!""")
#     else:
#         print("Try again!")





### --------------------------------------
###  Countdown Timer
### --------------------------------------
"""
This loop counts down from a starting number, for example, 10, to 1.
Explanation: The loop will continue until timer reaches 0. Each time it loops, it subtracts 1 from timer and stops when timer is no longer greater than 0.
"""

# timer = 10
# while timer > 0:
#     print(timer)
#     timer -= 1  # Decreases timer by 1 each time
# print("Time's up!")






### --------------------------------------
### Keep Adding Numbers Until Total is Over 100
### --------------------------------------
"""
This loop keeps adding numbers entered by the user until the total is over 100.
Explanation: The loop continues as long as total is less than or equal to 100. 
Each time the user enters a number, it adds it to total until it exceeds 100.
"""
# total = 0

# while total <= 100:
#     number = int(input("Enter a number to add: "))
#     total += number
#     print(f"Total so far: {total}")

# print("You've reached over 100!")







### --------------------------------------
### Summing a List of Numbers
### --------------------------------------
"""
This loop goes through a list of numbers and keeps adding them to get a sum.
Explanation: The loop runs while i is less than the length of the list, adding each number in numbers to total one by one.
"""
# numbers = [5, 10, 15, 20]
# i = 0
# total = 0

# while i < len(numbers): # while i < 4
#     total += numbers[i] # total = total +  numbers[i]
#     i += 1 # i = i + 1

# print("The total sum is:", total)





### --------------------------------------
### Collecting User Input Until They Type "stop"
### --------------------------------------
"""

This loop keeps collecting user input and adds it to a list until they type "stop".
Explanation: The loop breaks if the user types "stop". Otherwise, it keeps adding each response to user_responses.
"""
# user_responses = []

# while True:
#     response = input("Enter something (or type 'stop' to finish): ")
#     if response.lower() == "stop":
#         break
#     user_responses.append(response)

# print("Responses collected:", user_responses)







### --------------------------------------
### 
### --------------------------------------
"""

"""







### --------------------------------------
### 
### --------------------------------------
"""

"""




# 5. Keep Adding Numbers Until Total is Over 100
# This loop keeps adding numbers entered by the user until the total is over 100.

# python
# Copy code
# total = 0

# while total <= 100:
#     number = int(input("Enter a number to add: "))
#     total += number
#     print(f"Total so far: {total}")

# print("You've reached over 100!")
# Explanation: The loop continues as long as total is less than or equal to 100. Each time the user enters a number, it adds it to total until it exceeds 100.

# 6. Infinite Loop (Be Careful!)
# A loop that runs forever (or until you stop it).

# python
# Copy code
# while True:
#     print("This will go on forever unless you stop it!")
# Explanation: Since the condition is True, this loop has no end and will keep running forever. Infinite loops can be useful in some cases, but you’ll usually want a way to break out of them!

# 7. Summing a List of Numbers
# This loop goes through a list of numbers and keeps adding them to get a sum.

# python
# Copy code
# numbers = [5, 10, 15, 20]
# i = 0
# total = 0

# while i < len(numbers):
#     total += numbers[i]
#     i += 1

# print("The total sum is:", total)
# Explanation: The loop runs while i is less than the length of the list, adding each number in numbers to total one by one.

# 8. Collecting User Input Until They Type "stop"
# This loop keeps collecting user input and adds it to a list until they type "stop".

# python
# Copy code
# user_responses = []

# while True:
#     response = input("Enter something (or type 'stop' to finish): ")
#     if response.lower() == "stop":
#         break
#     user_responses.append(response)

# print("Responses collected:", user_responses)
# Explanation: The loop breaks if the user types "stop". Otherwise, it keeps adding each response to user_responses.
































































print()
print()
print()
print()
print("----------------------------------------------------------------------------------------")
