print()

###  =================================================================================================================
###  Escape sequences(character with backslash) and raw string
###  =================================================================================================================
# print('welcome tp Geek\'s course')  ## Escape sequences(character with backslash)
# print("Hi \nwelcome to the course")  ## Escape backslash with n(\n)
# print("A simple \ example")  ## Escaping the backslash itself
# print("Backslash at the end\\")  ## Escaping the backslash itself
# print("\\n")  ## Escaping the backslash itself
# print("\\t")  ## Escaping the backslash itself
# print("c:\project\name.py")  ## Raw string
# print(r"c:\project\name.py")  ## Raw string

#  ==================================================================================================================
#  String Comparison in Python
#  ==================================================================================================================
"""
the following below will produce the unicode representation of aphabeth(in integer )
"""
# Uppercase English Alphabet
# print("Uppercase English Alphabet (A-Z):")
# for char in range(ord('A'), ord('Z') + 1):
#     print(f"{chr(char)}: {char}")


#### Lowercase English Alphabet
# print("\nLowercase English Alphabet (a-z):")
# for char in range(ord('a'), ord('z') + 1):  
#     print(f"{chr(char)}: {char}")

### Uppercase English Alphabet (A-Z):
# A: 65
# B: 66
# C: 67
# D: 68
# E: 69
# F: 70
# G: 71
# H: 72
# I: 73
# J: 74
# K: 75
# L: 76
# M: 77
# N: 78
# O: 79
# P: 80
# Q: 81
# R: 82
# S: 83
# T: 84
# U: 85
# V: 86
# W: 87
# X: 88
# Y: 89
# Z: 90

### Lowercase English Alphabet (a-z):
# a: 97
# b: 98
# c: 99
# d: 100
# e: 101
# f: 102
# g: 103
# h: 104
# i: 105
# j: 106
# k: 107
# l: 108
# m: 109
# n: 110
# o: 111
# p: 112
# q: 113
# r: 114
# s: 115
# t: 116
# u: 117
# v: 118
# w: 119
# x: 120
# y: 121
# z: 122

### to get a since letter, use 
# print(f"a = {ord('a')}")
# print(f"A = {ord('A')}")


# s1 = "geeksforgeeks"
# s2 = "ide"

# print(s1<s2)                            # True    --  i in "ide" is greater than g  since i = 105 and g = 103
# print(s1<=s2)                           # True    --  i in "ide" is greater than g  since i = 105 and g = 103
# print(s1>s2)                            # False   --  i = 105 and g = 103
# print(s1>=s2)                           # False   --  i = 105 and g = 103
# print(s1==s2)                           # False   --  i = 105 and g = 103
# print(s1 != s2)                         # True    --  i = 105 and g = 103


# print("#############")                  
# print("abcd > abc ","abcd">"abc")       # True    --  abc on bothside match, but "b" in abcd made abcd greater than abc
# print("ZAB>ABC","ZAB">"ABC")            # True    --  
# print("abc>ABC","abc">"ABC")            # True    --  
# print("x>abcd","x">"abcd")              # True    --  
# ------------------------
# s = "geek"
# s[0] = "e"  # error: item assignment not supported
# print(s)

# s = """ Hi,
# This is python course.
# Hope you are enjoying it. """
# print(s)

#  ------------------------------------------------------------------------------------------------------------------
#    Formmatted String in Python
#  ------------------------------------------------------------------------------------------------------------------
# name = "ABC"
# course = "Python Course" 
# print("Welcome %s to the %s"%(name,course))
# print("welcome {0} to the {1}".format(name,course))  # using format function
# print(f"welcome {name} to the {course}")   # using f-string
# print()

# i am going to the protest today


# s1 = "geeks for geeks"
# s2 = "geeks"
# print(s1.find(s2))                 ##  ---->  0  # first place it found "geeks" which is index 
# print(s1.find("gfg"))              ##  ----> -1   # could not find it so it returned -1
# n = len(s1)
# print(s1.find(s2,1,n))             ##  ----> 10
# print()

# print(s1.index(s2))                 ##  ---->  0  # first place it found "geeks" which is index 
# # print(s1.index("gfg"))              ##  ----> error that the string does not exist  # could not index it so it returned -1
# n = len(s1)
# print(s1.index(s2,1,n))

"""
explaining print(s1.find(s2,1,n))
find('geeks'): searches for the substring 'geeks' within the original string.
1: This specifies the starting index for the search. The search will begin from the second character (index 1) of the string.
len("geeks for geeks"): This calculates the length of the original string, which is 15 characters. It specifies the ending index for the search, 
so the search will be performed up to the last character of the string.
--------
Overall: The code searches for the substring 'geeks' within the string "geeks for geeks", starting from the second character and continuing until the end of the string.
Output: The output of this code will be 5. This indicates that the substring 'geeks' is found at index 5 of the original string.
Explanation: The first occurrence of 'geeks' in the string "geeks for geeks" starts at index 5 (counting from 0). Since the search starts from index 1, the function returns the index of the first occurrence after the starting index
"""
#  ------------------------------------------------------------------------------------------------------------------
# Pattern Searching in Python 
#  ------------------------------------------------------------------------------------------------------------------

# txt = input("Enter Text:\n")
# pat = input("Enter Pattern:\n")
# pos = txt.find(pat)  # This will return the index of the first occurrence or -1 if not found
# found = False  # Flag to indicate if the pattern is found

# while pos >= 0:  # If the index returned is not -1, something is found, then print its position
#     found = True  # Set the flag to True when a pattern is found
#     print(f"{pat} is found on position {pos}")
#     pos = txt.find(pat, pos + 1)  # Redefine the find() to start from the next position

# if not found:  # If the pattern was never found, execute this block
#     print(f'"{pat.upper()}" was not found in the text you entered')

"""
- lets say the search term "I am goint to the Azure cloud to get my Azure certtificate. Azure104 is next. after that i will renew my Azure204" 
- pos = txt.find(pat) will seach for the first occurency of "Azure". 
    if found it will return 18 as the index it found it.  suppose it was not found, it will return -1
- while pos>=0: this while loop will only execute if the pos index found something, that it if pos is not -1
- when the while loop found something, it will print the position of the fisrt occurence, and the redefine the find function for pos variable
- pos = txt.find(pat,pos+1): this redefined find() will be like tex.find(pat.next-index-after-finding-the-last-occurrency )
   for example, it found the fisrt occurency of Azure in position 18, it will now start the next seach from position 19 and get Azure at position 40. it will now increase the starting search again from position 41 and so on 
-f nothin is found, that is, if any of the subsiquent seach return -1, then the wile loop will no longer execute. the "else" will now execute 
Result:
---------
Enter Text:
I am goint to the Azure cloud to get my Azure certtificate. Azure104 is next. after that i will renew my Azure204
Enter Pattern:
Azure
Azure is found on position 18
Azure is found on position 40
Azure is found on position 60
Azure is found on position 105
"""
#  ------------------------------------------------------------------------------------------------------------------
#  Reverse A String in Python
#  ------------------------------------------------------------------------------------------------------------------
"""
Slicing Syntax: sequence[start:stop:step]
    start: The index at which the slice starts. This value is inclusive.
    stop: The index at which the slice ends. This value is exclusive.
    step: The step size or stride. It determines how many elements to skip. 1 is default if step is not specified
"""
###  --------------------------------
###  Example-1
###  --------------------------------
    # s = "Hello, World!"
    # print(s[0:5])  # Output: Hello
"""
start = 0: Start at the first character.
stop = 5: Stop before the 6th character (index 5).
step: Not specified, so it defaults to 1 (every character).
"""

### ----------
### Example-2: Using Step - If you want every second character:
### ----------
    # print(s[::2])  # Output: Hlo ol!

"""
start: Not specified, so it defaults to the beginning of the string.
stop: Not specified, so it defaults to the end of the string.
step = 2: Take every second character.
"""

###----------
### Example-3: Reversing a String -- To reverse a string, you can use a negative step:
###----------

# print(s[::-1])  # Output: !dlroW ,olleH

"""
start: Not specified, so it defaults to the end of the string.
stop: Not specified, so it defaults to the beginning of the string.
step = -1: Move backwards one step at a time.

"""

###----------
### Example-4: Selecting a Substring with a Step
###----------

# s = "abcdefghijklmnopqrstuvwxyz"
# print(s[1:10:2])  # Output: bdfhj



"""
start = 1: Start at the second character (index 1, which is 'b').
stop = 10: Stop before the 11th character (index 10, which is 'k').
step = 2: Take every second character from the start index to the stop index.

"""


###----------
### Example-5:  Slicing with Negative Indices  -- Negative indices count from the end of the string:
###----------
# s = "abcdefghijklmnopqrstuvwxyz"
# print(s[-10:-1])  # Output: qrstuvwxy


"""
start = -10: Start at the 10th character from the end.
stop = -1: Stop before the last character.
step: Not specified, so it defaults to 1.

"""

###----------
### Example-6:  Reversing with Substring  --  If you want to reverse a substring:
###----------

# s = "abcdefghijklmnopqrstuvwxyz"
# print(s[5:15][::-1])  # Output: kjihegfedc

"""
s[5:15]: Extracts the substring from index 5 to 14 ('fghijklmno').
[::-1]: Reverses this substring.

"""




#  ------------------------------------------------------------------------------------------------------------------
# Check For Palindrome In Python
#  ------------------------------------------------------------------------------------------------------------------
"""
A palindrome is a word, phrase, number, or other sequence of characters that reads the same forward and backward (ignoring spaces, punctuation, and capitalization). Here are some examples of palindromic words:

Single-word Palindromes:
    Civic
    Level
    Rotor
    Kayak
    Racecar
    Madam
    Refer
    Noon
    Deified
    Repaper

Phrases (ignoring spaces and punctuation):
    A man, a plan, a canal, Panama!
    Was it a car or a cat I saw?
    No lemon, no melon
    Eva, can I see bees in a cave?
    Madam, in Eden, I'm Adam.

    

Numbers:
    121
    12321
    45654
    1001
    98989

"""
# -----------------------
### Method 1: Using String Slicing  --  String slicing is a concise way to reverse a string and compare it to the original string
# -----------------------

# s = input("Enter a String:\n")

# if s==s[::-1]:
#     print("Yes")
# else:
#     print("No")
# print()

### OR 

# def is_palindrome(s):
#     return s == s[::-1]

# # Example usage
# word = "racecar"
# print(is_palindrome(word))  # Output: True

# word = "hello"
# print(is_palindrome(word))  # Output: False

"""
Explanation
s[::-1] creates a reversed version of the string s.
s == s[::-1] checks if the original string is equal to its reversed version.

"""
# -----------------------
#### Method 2: Using a Loop --- You can use a loop to compare characters from the beginning and end of the string, moving towards the center
# -----------------------
# def is_palindrome(s):
#     for i in range(len(s) // 2):
#         if s[i] != s[-i - 1]:
#             return False
#     return True

# # Example usage
# word = "madam"
# print(is_palindrome(word))  # Output: True

# word = "world"
# print(is_palindrome(word))  # Output: False


"""
Explanation
len(s) // 2 determines the middle of the string.
The loop iterates from the start to the middle of the string.
s[i] != s[-i - 1] compares the characters at corresponding positions from the start and end.
If any pair of characters doesn't match, it returns False. If all pairs match, it returns True.

"""



# -----------------------
#### Method 3: Using Recursion --- A recursive function can be used to check if a string is a palindrome by comparing the first and last characters and then calling itself with the remaining substring.
# -----------------------
# def is_palindrome(s):
#     if len(s) <= 1:
#         return True
#     if s[0] != s[-1]:
#         return False
#     return is_palindrome(s[1:-1])

# # Example usage
# word = "refer"
# print(is_palindrome(word))  # Output: True

# word = "python"
# print(is_palindrome(word))  # Output: False


"""
Explanation
len(s) <= 1 checks if the string has zero or one character, in which case it's a palindrome.
s[0] != s[-1] compares the first and last characters.
is_palindrome(s[1:-1]) calls the function recursively with the substring excluding the first and last characters.
"""

# -----------------------
#### Method 4: Using Deque from collections  -- A deque (double-ended queue) can be used for efficient front and back character comparisons
# -----------------------
# from collections import deque

# def is_palindrome(s):
#     dq = deque(s)
#     while len(dq) > 1:
#         if dq.popleft() != dq.pop():
#             return False
#     return True

# # Example usage
# word = "level"
# print(is_palindrome(word))  # Output: True

# word = "python"
# print(is_palindrome(word))  # Output: False

"""
Explanation
deque(s) creates a deque with characters from the string s.
dq.popleft() removes and returns the leftmost character.
dq.pop() removes and returns the rightmost character.
The loop continues until the deque has zero or one character left, indicating a palindrome if all comparisons match.
"""

# -----------------------
#### Method 5: Ignoring Case and Non-Alphanumeric Characters   ---   To handle cases where the palindrome check should ignore case and non-alphanumeric characters, you can preprocess the string
# -----------------------

# import re

# def is_palindrome(s):
#     s = re.sub(r'[^A-Za-z0-9]', '', s).lower()
#     return s == s[::-1]

# # Example usage
# phrase = "A man, a plan, a canal, Panama!"
# print(is_palindrome(phrase))  # Output: True

# phrase = "Hello, World!"
# print(is_palindrome(phrase))  # Output: False


"""
Explanation
re.sub(r'[^A-Za-z0-9]', '', s) removes all non-alphanumeric characters using a regular expression.
.lower() converts the string to lowercase.
The processed string is then checked for being a palindrome using slicing (s == s[::-1]).
"""

# -----------------------
#### Method  6: Using String slicing
# -----------------------
############# This code checks whether the input string is a palindrome by comparing characters from the ends towards the center. 
########## If any pair of characters doesn't match, it prints "No" and exits. If all characters match, it prints "Yes" indicating the string is a palindrome.
## Step 1: Input the String
# s = input("Enter a String:\n")

# # Step 2: Initialize Pointers
# low = 0
# high = len(s) - 1

# # Step 3: While Loop for Comparison
# while low < high:
#     # Step 4: Check Characters at Pointers
#     if s[low] != s[high]:
#         print("No")  # Not a palindrome
#         break       # Exit the loop
#     # Step 5: Move Pointers Inward
#     low = low + 1
#     high = high - 1
# # Step 7: Else Block Execution
# else:
#     print("Yes")  # It's a palindrome


"""
Step-by-Step Breakdown
1 Input the String: The user is prompted to enter a string, which is stored in the variable s.
    s = input("Enter a String:\n")

2 Initialize Pointers:
    low = 0
    high = len(s) - 1
low is initialized to 0, pointing to the first character of the string.
high is initialized to len(s) - 1, pointing to the last character of the string.

3 While Loop for Comparison: The loop continues as long as low is less than high. This ensures that characters are compared from the outside towards the center.
    while low < high:

4. Check Characters at Pointers:  Within the loop, the characters at the low and high pointers are compared

    if s[low] != s[high]:
        print("No")
        break
If the characters at positions low and high are not equal (s[low] != s[high]), it means the string is not a palindrome.
    - print("No"): Prints "No" indicating the string is not a palindrome.
    - break: Exits the loop immediately since a mismatch has been found.

5. Move Pointers Inward: If the characters at the low and high pointers are equal, the pointers are moved inward to the next pair of characters

     low = low + 1
     high = high - 1

low = low + 1: Increments the low pointer by 1, moving it to the next character from the left.
high = high - 1: Decrements the high pointer by 1, moving it to the next character from the right.

6. Loop Continuation or Termination: The loop will continue to check and move pointers inward until low is no longer less than high.

7. Else Block Execution: If the loop completes without finding any mismatched characters, the else block is executed. This means the string is a palindrome.

    else:
        print("Yes")
print("Yes"): Prints "Yes" indicating the string is a palindrome.

-------------------

Example Walkthrough:
Let's walk through an example to see how the code works step-by-step:

Input: madam

Initialization:

s = "madam"
    low = 0
    high = 4 (since len(s) - 1 = 5 - 1 = 4)

First Iteration:
    Compare s[0] and s[4] (m and m)
    They are equal.
    Move low to 1 and high to 3.

Second Iteration:
    Compare s[1] and s[3] (a and a)
    They are equal.
    Move low to 2 and high to 2.

Loop Termination:
    Now low is not less than high (both are 2).
    The loop ends and the else block is executed.

Output:
    Prints "Yes" indicating the input string madam is a palindrome.







"""

#### 

#### 

#### 









#  ------------------------------------------------------------------------------------------------------------------
# Check for Anagram in Python
#  ------------------------------------------------------------------------------------------------------------------
"""
The next tasks is to check when given two string, if both are Anagram or not
lets say we have 2 string s1 = "silent" and s2 = "listen" of the same lengths. if every character in s1 is in s2, irrespective of their position, then they are both anagram
s1 = "listen" and s2 = "silent"                       ------>   Anagram
s1 = "rail safety" and s2 = "fairy tales"             ------>   Anagram
s1 = "elbow" and s2 = "below"                         ------>   Anagram
s1 = "heart" and s2 = "earth"                         ------>   Anagram
s1 = "state" and s2 = "taste"                         ------>   Anagram
s1 = "cinema" and s2 = "iceman"                       ------>   Anagram
s1 = "aab" and s2 = "abb"                             ------>   NOT Anagram
s1 = "silents" and s2 = "listen"                      ------>   NotAnagram

two string will be anagram only:
    - if they have the same length
    - if they are both sorted, they will be the same
"""

## method1 ##############
# def are_anagrams(str1, str2):
#     return sorted(str1) == sorted(str2)

# # Example usage
# str1 = "listen"
# str2 = "silent"
# print(are_anagrams(str1, str2))  # Output: True

# --------------------

### the time complextity is 0(nlogn)
# def check_for_anagram(s1,s2):
#     # Convert strings to lowercase for case-insensitive comparison
#     s1 = s1.lower()
#     s2 = s2.lower()
#     if len(s1) != len(s2):
#         return False
#     sorted_s1 = sorted(s1)
#     sorted_s2 = sorted(s2)
#     return (sorted_s1 == sorted_s2)

# s_1 = "listens"
# s_2 = "silent"
# if check_for_anagram(s_1,s_2):
#     print(f"'{s_1}' and '{s_2}' are Anagram")
# else:
#     print(f"'{s_1}' and '{s_2}' are NOT Anagram")  
# -----------------

### Using the Counter class from the collections module. This method counts the frequency of each character in both strings and compares the counts.
# from collections import Counter

# def are_anagrams(str1, str2):
#     return Counter(str1) == Counter(str2)

# # Example usage
# str1 = "listen"
# str2 = "silent"
# print(are_anagrams(str1, str2))  # Output: True

### -----------------

 ### Method 3: Using a Dictionary  -- You can also manually count the frequency of characters in both strings using dictionaries and compare them.
# def are_anagrams(str1, str2):
#     if len(str1) != len(str2):
#         return False
    
#     count1 = {}
#     count2 = {}
    
#     for char in str1:
#         count1[char] = count1.get(char, 0) + 1
    
#     for char in str2:
#         count2[char] = count2.get(char, 0) + 1
    
#     return count1 == count2

# # Example usage
# str1 = "listen"
# str2 = "silent"
# print(are_anagrams(str1, str2))  # Output: True
# ------------------------



"""
### Each character in the string str1 has been counted, and the dictionary count1 stores the frequency of each character.
# str1 = "listen"
# count1 = {}

# for char in str1:
#     count1[char] = count1.get(char, 0) + 1

# print(count1)  # {'l': 1, 'i': 1, 's': 1, 't': 1, 'e': 1, 'n': 1}
----------------------------
Execution:

First Iteration (char = 'l'):
    count1.get('l', 0) returns 0 (since 'l' is not in count1 yet).
    count1['l'] = 0 + 1 sets count1['l'] to 1.

Second Iteration (char = 'i'):
    count1.get('i', 0) returns 0.
    count1['i'] = 0 + 1 sets count1['i'] to 1.

Third Iteration (char = 's'):
    count1.get('s', 0) returns 0.
    count1['s'] = 0 + 1 sets count1['s'] to 1.

Fourth Iteration (char = 't'):
    count1.get('t', 0) returns 0.
    count1['t'] = 0 + 1 sets count1['t'] to 1.

Fifth Iteration (char = 'e'):
    count1.get('e', 0) returns 0.
    count1['e'] = 0 + 1 sets count1['e'] to 1.

Sixth Iteration (char = 'n'):
    count1.get('n', 0) returns 0.
    count1['n'] = 0 + 1 sets count1['n'] to 1.
----------------------------------------------------------


str1 = "bababa"
count1 = {}

for char in str1:
    count1[char] = count1.get(char, 0) + 1

print(count1)
------------------------

Execution Step-by-Step
Initial Setup:

str1 is "bababa".
count1 is an empty dictionary {}.



First Iteration (char = 'b'):
    count1.get('b', 0) returns 0 (since 'b' is not in count1 yet).
    count1['b'] = 0 + 1 sets count1['b'] to 1.

Second Iteration (char = 'a'):
    count1.get('a', 0) returns 0 (since 'a' is not in count1 yet).
    count1['a'] = 0 + 1 sets count1['a'] to 1.

Third Iteration (char = 'b'):
    count1.get('b', 0) returns 1 (since 'b' is already in count1 with value 1).
    count1['b'] = 1 + 1 sets count1['b'] to 2.

Fourth Iteration (char = 'a'):
    count1.get('a', 0) returns 1 (since 'a' is already in count1 with value 1).
    count1['a'] = 1 + 1 sets count1['a'] to 2.

Fifth Iteration (char = 'b'):
    count1.get('b', 0) returns 2 (since 'b' is already in count1 with value 2).
    count1['b'] = 2 + 1 sets count1['b'] to 3.

Sixth Iteration (char = 'a'):
    count1.get('a', 0) returns 2 (since 'a' is already in count1 with value 2).
    count1['a'] = 2 + 1 sets count1['a'] to 3.

 After all iterations, the dictionary count1 will look like this:    {'b': 3, 'a': 3}



"""




"""
Breakdown
for char in str1:
    count1[char] = count1.get(char, 0) + 1


This is a loop that iterates over each character (char) in the string str1.
count1[char] = count1.get(char, 0) + 1:
    count1[char]: This is accessing the dictionary count1 at the key char. If char is already a key in count1, this returns its associated value (the count of occurrences of that character so far). If char is not yet a key, it will create a new key-value pair in the dictionary.
    count1.get(char, 0): This is a method of dictionaries in Python. count1.get(char, 0) checks if char exists as a key in the dictionary count1. If it does, it returns the value associated with char. If char does not exist as a key, it returns the default value provided (in this case, 0).
    count1.get(char, 0) + 1: This expression adds 1 to the current count of char (which is retrieved by count1.get(char, 0)). If char is not already in the dictionary, count1.get(char, 0) will return 0, and adding 1 will set the count to 1.
    count1[char] = count1.get(char, 0) + 1: This updates the dictionary count1 by setting the value for the key char to the new count (current count + 1).

Example
Let's go through an example with a string str1 = "banana":

Initial state:
    str1 = "banana"
    count1 = {} (an empty dictionary)

Iteration 1 (char = 'b'):
    count1.get('b', 0) returns 0 (since 'b' is not in count1 yet)
    count1['b'] = 0 + 1 updates count1 to {'b': 1}

Iteration 2 (char = 'a'):
    count1.get('a', 0) returns 0 (since 'a' is not in count1 yet)
    count1['a'] = 0 + 1 updates count1 to {'b': 1, 'a': 1}

Iteration 3 (char = 'n'):
    count1.get('n', 0) returns 0 (since 'n' is not in count1 yet)
    count1['n'] = 0 + 1 updates count1 to {'b': 1, 'a': 1, 'n': 1}

Iteration 4 (char = 'a'):
    count1.get('a', 1) returns 1 (since 'a' is already in count1 with a count of 1)
    count1['a'] = 1 + 1 updates count1 to {'b': 1, 'a': 2, 'n': 1}

Iteration 5 (char = 'n'):
    count1.get('n', 1) returns 1 (since 'n' is already in count1 with a count of 1)
    count1['n'] = 1 + 1 updates count1 to {'b': 1, 'a': 2, 'n': 2}

Iteration 6 (char = 'a'):
    count1.get('a', 2) returns 2 (since 'a' is already in count1 with a count of 2)
    count1['a'] = 2 + 1 updates count1 to {'b': 1, 'a': 3, 'n': 2}


"""




"""
Explanation:

Sorting Method:
    sorted(str1) and sorted(str2) create sorted lists of characters from both strings.
    return sorted(str1) == sorted(str2) compares these lists. If they are equal, the strings are anagrams.

Counter Method:
    Counter(str1) and Counter(str2) create frequency dictionaries for characters in both strings.
    return Counter(str1) == Counter(str2) compares these dictionaries. If they are equal, the strings are anagrams.

Dictionary Method:
    if len(str1) != len(str2) checks if the strings are of equal length. If not, they can't be anagrams.
    count1 and count2 are dictionaries that store character frequencies.
    The loops for char in str1 and for char in str2 populate these dictionaries.
    return count1 == count2 compares these dictionaries. If they are equal, the strings are anagrams.

Performance Considerations:
    The sorting method has a time complexity of O(nlogn) due to the sorting operation.
    The Counter method and the dictionary method both have a time complexity of O(n), making them more efficient for larger strings.

"""

#  ------------------------------------------------------------------------------------------------------------------
#  Reverse A String in Python
#  ------------------------------------------------------------------------------------------------------------------

"""
In python, a string is immutable - once you create a string, you can not change it. 
thus to reverse it is not create a new string
"""

#### -------------
#### Method 0: 
#### -------------

# s = input("Enter a String:\n")

# rev = ""

# for i in s:
#     rev = i+rev

# print(rev)



#### --------------------------
#### Method 1: Using Slicing:
#### --------------------------

# def reverse_string(s):
#     return s[::-1]

# # Example usage
# original_string = "Hello, World!"
# reversed_string = reverse_string(original_string)
# print(reversed_string)  # Output: !dlroW ,olleH


#### ------------------------
#### Method 2: Using a Loop
#### ------------------------

# def reverse_string(s):
#     reversed_str = ""
#     for char in s:
#         reversed_str = char + reversed_str
#     return reversed_str

# # Example usage
# original_string = "Hello, World!"
# reversed_string = reverse_string(original_string)
# print(reversed_string)  # Output: !dlroW ,olleH


#### -------------
#### Method 3: Using the reversed() Function
#### -------------
# def reverse_string(s):
#     return ''.join(reversed(s))

# # Example usage
# original_string = "Hello, World!"
# reversed_string = reverse_string(original_string)
# print(reversed_string)  # Output: !dlroW ,olleH


#### -------------------------------
#### Method 4: Using Recursion
#### -------------------------------
# def reverse_string(s):
#     if len(s) == 0:
#         return s
#     else:
#         return reverse_string(s[1:]) + s[0]

# # Example usage
# original_string = "Hello, World!"
# reversed_string = reverse_string(original_string)
# print(reversed_string)  # Output: !dlroW ,olleH


#### -------------------------------
#### 
#### -------------------------------


#### -------------------------------
#### 
#### -------------------------------


#### -------------------------------
#### 
#### -------------------------------


#### -------------------------------
#### 
#### -------------------------------


#### -------------------------------
#### 
#### -------------------------------


#### -------------------------------
#### 
#### -------------------------------


#### -------------------------------
#### 
#### -------------------------------


#### -------------------------------
#### 
#### -------------------------------


#### -------------------------------
#### 
#### -------------------------------


#### -------------------------------
#### 
#### -------------------------------



#### -------------------------------
#### 
#### -------------------------------


#### -------------------------------
#### 
#### -------------------------------
































print()