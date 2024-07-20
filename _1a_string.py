a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua xxx."""




# capitalize(): Returns a copy of the string with the first character capitalized and the rest in lowercase.
# casefold(): Returns a copy of the string with all characters in lowercase, and it also handles some special cases for non-ASCII characters.
# center(): Returns a centered string of a specified width. The remaining space is filled with a specified character.
# count(): Returns the number of occurrences of a specified substring in the string.
# encode(): Returns an encoded version of the string.
# endswith(): Returns True if the string ends with the specified substring, otherwise False.
# expandtabs(): Replaces all tab characters in the string with a specified number of spaces.
# find(): Returns the index of the first occurrence of a specified substring in the string, or -1 if not found.
# format(): Formats the string according to a specified format string.
# format_map(): Formats the string according to a specified mapping.
# index(): Returns the index of the first occurrence of a specified substring in the string, or raises a ValueError if not found.
# isalnum(): Returns True if all characters in the string are alphanumeric, otherwise False.
# isalpha(): Returns True if all characters in the string are alphabetic, otherwise False.
# isdecimal(): Returns True if all characters in the string are decimal, otherwise False.
# isdigit(): Returns True if all characters in the string are digits, otherwise False.
# isidentifier(): Returns True if the string is a valid identifier, otherwise False.
# islower(): Returns True if all characters in the string are lowercase, otherwise False.
# isnumeric(): Returns True if all characters in the string are numeric, otherwise False.
# isprintable(): Returns True if all characters in the string are printable, otherwise False.
# isspace(): Returns True if all characters in the string are whitespace, otherwise False.
# istitle(): Returns True if the string is in title case, otherwise False.
# isupper(): Returns True if all characters in the string are uppercase, otherwise False.
# join(): Joins a sequence of strings with the specified separator string.

# ljust(): Returns a left-justified string of a specified width. The remaining space is filled with a specified character.
# lower(): Returns a copy of the string with all characters in lowercase.
# lstrip(): Returns a copy of the string with leading whitespace removed.
# maketrans(): Returns a translation table for use in string translation methods.
# partition(): Splits the string into three parts: the part before the specified separator, the separator itself, and the part after the separator.
# replace(): Replaces all occurrences of a specified substring with another substring.
# rfind(): Returns the highest index of the specified substring.
# rindex(): Returns the highest index of the specified substring, or raises a ValueError if not found.
# rjust(): Returns a right-justified string of a specified width. The remaining space is filled with a specified character.
# rpartition(): Splits the string into three parts: the part before the specified separator from the right, the separator itself, and the part after the separator.
# rsplit(): Splits the string into a list of substrings, starting from the right.
# rstrip(): Returns a copy of the string with trailing whitespace removed.
# split(): Splits the string into a list of substrings.
# splitlines(): Splits the string at line breaks and returns a list of lines.



# n="i am gonna crash python, \ndjango, nimble,pandas and more"
# print(n);
# name=input("enter name: ");
# print("mr. ",3*name+" ",name*2+"rism" " hmmmmm");
# l=len(name);
# a=name[2:3]# i
# b=name[:4] #prin
# c=name[4:]#cewill
# print(a+b+c)



# name=input("Enter any word: ")
name= "programmer"
name2= "I am a programmer"
name3 = "the\worild\with\love"

#-----------------------------------------------------------------------------------------------------
#     SUBSTRING
#-----------------------------------------------------------------------------------------------------
# str = 'Hello World!'
# print (str)          # Prints complete string // 'Hello World!'
# print (str[0])       # Prints first character of the string // H
# print (str[2:5])     # Prints characters starting from 3rd to 5th  //  llo
# print (str[2:])      # Prints string starting from 3rd character till the end // llo World!
# print (str * 2)      # Prints string two times  // Hello World!Hello World!
# print (str + "TEST") # Prints concatenated string // Hello World!TEST


#-----------------------------------------------------------------------------------------------------
#     CASE RELATED OR IMPORTANT ONES
#-----------------------------------------------------------------------------------------------------
print()
print("--------------Case Related----------------------")
print()
print(f"you entered {name}")
print(f"{name} has {len(name)} character(s)")
print(f"name.capitalize(): {name.capitalize()}")#capitalize only the 1st character
print(f"name.upper(): {name.upper()}")#capitalize only the 1st character
print(f"name.lower(): {name.lower()}")#capitalize only the 1st character
print(f"name.title():  {name.title()}")#capitalize only the 1st character
print(f"name.casefold():  {name.casefold()}") # return the case in smaller form (useful for case marching)
print(f"name.swapcase():  {name.swapcase()}")#capitalize only the 1st character
print(f"name.title(): {name.title()}")#capitalize only the 1st character
#-----------------------------------------------------
print(name2.title())#capitalize only the 1st character
#-----------------------------------------------------
#replace(): Returns a string where a specified substring is replaced with another specified substring.
str = "hello world"
print(str.replace("world", "python world")) # "hello python"
#-----------------------------------------------------
# rsplit(): Splits the string at the specified separator, starting from the right.
# it automatically converts string to list
str = "hello my beautiful python world"
print(str.rsplit(" ")) # ["hello", "world"]
#-----------------------------------------------------
# it automatically converts string to list
str = "hello my beautiful python world"
print(str.split()) # ["hello", "world"]
#-----------------------------------------------------
# join(): Joins a list of strings with the string as a separator.
list = ["hello", "world"]
str = " "
print(str.join(list)) # "hello world"

#-----------------------------------------------------
# strip(): Removes any leading and trailing characters (by default, whitespace characters) from the string.
# You can also pass a character or a substring as an argument to remove from the leading and trailing ends of the string.
str = "   hello world   "
print(str.strip()) # "hello world"
str = "***hello world***"
print(str.strip("*")) # "hello world"
#-----------------------------------------------------

#-----------------------------------------------------





#-----------------------------------------------------------------------------------------------------
#     RETURNED INDEXES
#-----------------------------------------------------------------------------------------------------

print()
print("-------------- Return Index----------------------")#capitalize only the 1st character
str = "hello world"
print(f"name.endswith('ism'):  {str.endswith('er')}")#
print(f"name.startswith('he'):  {str.startswith('he')}")#name.find(sub[, start[, end]])): ",name.find("a", 1, 3))# start or end are optional: find position of "a"
print(f"str.find('o'):  {str.find('o')}")# Returns the index of the first occurrence of a specified substring in the string, or -1 if not found.
print(f"str.rfind('o'):  {str.rfind('o')}")#  Returns the index of the last occurrence of a specified substring in the string
print(f"str.index('o'):  {str.index('o')}") # Returns the index of the first occurrence of a specified substring in the string, or raises a ValueError if not found.
print(f"str.rindex('o'):  {str.rindex('o')}")#rindex(): Returns the index of the last occurrence of a specified substring in the string.

#-----------------------------------------------------------------------------------------------------
#     RETURNED BOOLEANS
#-----------------------------------------------------------------------------------------------------

print()
print("-------------- Return Boolean----------------------")#capitalize only the 1st character

#-----------------------------------------------------
# isalnum(): Returns True if all characters in the string are alphanumeric.
str = "hello123"
print(str.isalnum()) # True
#-----------------------------------------------------
# isalpha(): Returns True if all characters in the string are alphabetic.
str = "hello"
print(str.isalpha()) # True
#-----------------------------------------------------
# isdecimal(): Returns True if all characters in the string are decimal digits.
str = "123"
print(str.isdecimal()) # True
#-----------------------------------------------------
# isdigit(): Returns True if all characters in the string are digits.
str = "123"
print(str.isdigit()) # True
#-----------------------------------------------------
# isidentifier(): Returns True if the string is a valid identifier.
str = "hello_world"
print(str.isidentifier()) # True

#-----------------------------------------------------
# islower(): Returns True if all characters in the string are lowercase.
str = "hello"
print(str.islower()) # True


#-----------------------------------------------------
# isspace(): Returns True if all characters in the string are whitespace.
str = "   "
print(str.isspace()) # True

#-----------------------------------------------------
# istitle(): Returns True if the string is in title case.
str = "Hello World"
print(str.istitle()) # True
#-----------------------------------------------------
# isupper(): Returns True if all characters in the string are uppercase.
str = "HELLO"
print(str.isupper()) # True

#-----------------------------------------------------

#-----------------------------------------------------
#-----------------------------------------------------------------------------------------------------
#     OTHERS
#-----------------------------------------------------------------------------------------------------
print()
print("--------------others----------------------")
print(f"name.center(13, '-'):  {name.center(16, '-')}")#

print(f"name.ljust(10, '-'): {name.ljust(15, '-')}") # "hello-----" / Returns a left-justified string of a specified width. The remaining space is filled with a specified character
print(f"name.rjust(10, '-'): {name.rjust(15, '-')}")#rjust(): Returns a right-justified version of the string, padded with a specified character.
print(f"name.count(' '):  {name.count(' ')}")#count(sub[, start[, end]] // name.count("a", 3, 9))# start or end are optional// #counts the number of substring in a string. in this case it return 0 since no space is in. if we have count('o') it will return 2 in a string "logo"
#-----------------------------------------------------
str = "    i am a man"
print(f"str.lstrip():  {str.lstrip()}")# Returns a copy of the string with leading whitespace removed // called left strip// reove space only from the left

#-----------------------------------------------------
# opposite of lstrip
# Returns a copy of the string with trailing whitespace removed.
str = "hello   "
print(str.rstrip()) # "hello"
#-----------------------------------------------------

#-----------------------------------------------------

#-----------------------------------------------------

#-----------------------------------------------------------------------------------------------------
#     THESE METHODS HAVE BETTER REPLACEMENTS
#-----------------------------------------------------------------------------------------------------

print()
print("--------------these string methods have better replacements----------------------")
#maketrans(): Returns a translation table to be used with the translate() method.
#the .upper() and lower() could do the job of makestrans easily
str1 = "abcdefghijklmnopqrstuvwxy"
str2 = "ABCDEFGHIJKLMNOPQRSTUVWXY"
table = str.maketrans(str1, str2)
print("hello zworld".translate(table)) # "HELLO zWORLD" note that i didnt add the Z on both side, so it could not translate z
#-----------------------------------------------------


#-----------------------------------------------------------------------------------------------------
#     NOT THAT USEFUL METHODS
#-----------------------------------------------------------------------------------------------------
print()
print("--------------not that useful----------------------")#capitalize only the 1st character

# print(f"name.encode():  {name.encode()}")
#-----------------------------------------------------
# print(f"name3.expandtabs(4):  {name3.expandtabs(4)}")
#-----------------------------------------------------
# str = "Hello, my name is {name} and i am {age} year old"
# dict = {"name":"John","age":19}
# print(str.format(name="John",age=19))
# print(str.format_map(dict))

# str = "My name is {0} and I am {1} years old."
# print(str.format("Alice", 30)) # "My name is Alice and I am 30 years old."
#-----------------------------------------------------
# #partition(): Returns a tuple containing the string before the specified separator, the separator itself, and the string after the separator.
# str = "hello my beautiful world"
# print(str.partition(" ")) # ("hello", " ", "world")
#-----------------------------------------------------
#rpartition(): Returns a tuple containing the string before the last occurrence of the specified separator, the separator itself, and the string after the separator.
# str = "hello world"
# print(str.rpartition(" ")) # ("hello", " ", "world")
#-----------------------------------------------------
# #zfill(): Returns a copy of the string padded with zeros to a specified width.
# str = "hello"
# print(str.zfill(10)) # "00000hello"
#-----------------------------------------------------

# print("name.): ",
# print("name.endswith(suffix[, start[, end]]): ",name.endswith("ism",2,3))# start or end are optional: search if string has "ism" at the end

# # print("name.count(sub[, start[, end]]): ",name.count("a", 3, 9))# start or end are optional
# print("name.center(width[, fillchar]): ",name.center(9,"="))#cthe fillchar must be just one character and width longer than string

#-----------------------------------------------------------------------------------------------------
#     IN
#-----------------------------------------------------------------------------------------------------
print()
print("--------------IN----------------------")#capitalize only the 1st character
# in operator: Returns True if the specified value is found in the sequence, and False otherwise.
# list
fruits = ["apple", "banana", "cherry"]
print("apple" in fruits) # True

# string
text = "hello world"
print("world" in text) # True

# tuple
t = (1, 2, 3)
print(4 in t) # False
#-----------------------------------------------------------------------------------------------------
#     NOT IN
#-----------------------------------------------------------------------------------------------------

print()
print("--------------NOT IN----------------------")#capitalize only the 1st character
# not in operator: Returns True if the specified value is not found in the sequence, and False otherwise.
# list
fruits = ["apple", "banana", "cherry"]
print("orange" not in fruits) # True

# string
text = "hello world"
print("goodbye" not in text) # True

# tuple
t = (1, 2, 3)
print(2 not in t) # False

#-----------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------

ch = input("Enter any letter u wanna find: ");
if(len(ch)>0):
    print("the first occurrency of  '",ch,"' is at position",(name.find(ch)+1))
else:
    print( ch, " does not occur in ", name)

print(ch,"occurs ",name.count(ch)," times in",name )
repl=input("Enter any letter u wanna replace it with: ");
print("after the replacement of",ch," by ",repl,", ",name," now becomes ",name.replace(ch,repl))
