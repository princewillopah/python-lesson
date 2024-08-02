# They allow you to search for patterns in strings and manipulate the strings based on those patterns.
#  to user regular expression, you need to import its module "import re"
#  we use the "." and "*" to match certain parts of a string. for example  For example,
    #  the pattern cat will match the string "cat",
    #  while the pattern ca. will match "cat", "car", and "cab".



# "Metacharacters" are characters with a special meaning:
# []	=> A set of characters  :example	"[a-m]"
# \	    => Signals a special sequence (can also be used to escape special characters)  :example	"\d"
# .	    => 	Any character (except newline character)  :example	"he..o"
# ^	    => 	Starts with  :example	"^hello"
# $	    => 	Ends with  :example	"planet$"
# *	    => Zero or more occurrences  :example	"he.*o"
# +	    => 	One or more occurrences  :example	"he.+o"
# ?	    => 	Zero or one occurrences  :example	"he.?o"
# {}    => 	Exactly the specified number of occurrences  :example	"he.{2}o"
# |	    => 	Either or  :example	"falls|stays"
# ()    => 	Capture and group


# A special sequence is a \ followed by one of the characters in the list below, and has a special meaning:

# \A    => 		Returns a match if the specified characters are at the beginning of the string :example	"\AThe"
# \b    => 		Returns a match where the specified characters are at the beginning or at the end of a word (the "r" in the beginning is making sure that the string is being treated as a "raw string") :example		r"\bain"   or   r"ain\b"
# \B    => 		Returns a match where the specified characters are present, but NOT at the beginning (or at the end) of a word (the "r" in the beginning is making sure that the string is being treated as a "raw string") :example		r"\Bain" or r"ain\B"
# \d    => 		Returns a match where the string contains digits (numbers from 0-9) :example		"\d"
# \D    => 		Returns a match where the string DOES NOT contain digits :example		"\D"
# \s    => 		Returns a match where the string contains a white space character :example		"\s"
# \S    => 		Returns a match where the string DOES NOT contain a white space character :example		"\S"
# \w    => 		Returns a match where the string contains any word characters (characters from a to Z, digits from 0-9, and the underscore _ character) :example		"\w"
# \W    => 		Returns a match where the string DOES NOT contain any word characters :example		"\W"
# \Z    => 		Returns a match if the specified characters are at the end of the string :example		"Spain\Z"

# [arn]    => 	Returns a match where one of the specified characters (a, r, or n) is present
# [a-n]    => 	Returns a match for any lower case character, alphabetically between a and n
# [^arn]   => 	Returns a match for any character EXCEPT a, r, and n
# [0123]   => 	Returns a match where any of the specified digits (0, 1, 2, or 3) are present
# [0-9]    => 	Returns a match for any digit between 0 and 9
# [0-5][0-9]    => 	Returns a match for any two-digit numbers from 00 and 59
# [a-zA-Z]    => 	Returns a match for any character alphabetically between a and z, lower case OR upper case
# [+]    => 	In sets, +, *, ., |, (), $,{} has no special meaning, so [+] means: return a match for any + character in the string


# The re module offers a set of functions that allows us to search a string for a match:
#  findall	Returns a list containing all matches
# search	Returns a Match object if there is a match anywhere in the string
# split	Returns a list where the string has been split at each match
# sub	Replaces one or many matches with a string

#-----------------------------------------------------------------------------------------------------

#-----------------------------------------------------------------------------------------------------
# ^a...s$  =>  any five letter string starting with a and ending with s


#-----------------------------------------------------------------------------------------------------
#     EXAMPLES
#-----------------------------------------------------------------------------------------------------


import re
#-----------------------------------------------------------------
# The findall() function returns a list containing all matches.
#-----------------------------------------------------------------

# txt = "The rain in Spain"
# x = re.findall("ai", txt)
# print(x)
### ANOTHER EXAMPLE
# txt = "The rain in Spain"
# x = re.findall("Portugal", txt)
# print(x)
#-----------------------------------------------------------------
#-----------------------------------------------------------------

#-----------------------------------------------------------------
# The search() function searches the string for a match, and returns a Match object if there is a match.
# If there is more than one match, only the first occurrence of the match will be returned:
#-----------------------------------------------------------------
# Search the string to see if it starts with "The" and ends with "Spain":
# txt = "The rain in Spain"
# x = re.search("^The.*Spain$", txt)
# if x:
#   print("YES! We have a match!")
#   print(x)
# else:
#   print("No match")
# ---------------------------------------------
# txt = "The rain in Spain"
# x = re.search("\s", txt)
# print("The first white-space character is located in position:", x.start())
# #
#-----------------------------------------------------------------
# # # If no matches are found, the value None is returned:
# txt = "The rain in Spain"
# x = re.search("Portugal", txt)
# print(x)
# #
#-----------------------------------------------------------------
# # A Match Object is an object containing information about the search and the result
# Note: If there is no match, the value None will be returned, instead of the Match Object.
# txt = "The rain in Spain"
# x = re.search("ai", txt)
# print(x)

#-----------------------------------------------------------------
# # The sub() function replaces the matches with the text of your choice:
#-----------------------------------------------------------------

# txt = "The rain in Spain"
# x = re.sub("\s", "-", txt)
# print(x)
# # # You can control the number of replacements by specifying the count parameter:
# txt = "The rain in Spain"
# x = re.sub("\s", "-", txt, 2)
# print(x)
#
# ----------------------------------------------------------
# ----------------------------------------------------------
# ----------------------------------------------------------
# ----------------------------------------------------------
# ----------------------------------------------------------


# # The Match object has properties and methods used to retrieve information about the search, and the result:
# # .span() returns a tuple containing the start-, and end positions of the match.
# # .string returns the string passed into the function
# # .group() returns the part of the string where there was a match
#
# Print the position (start- and end-position) of the first match occurrence.
#
# The regular expression looks for any words that starts with an upper case "S":
txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.span())
#
# # Print the string passed into the function:
# txt = "The rain in Spain"
# x = re.search(r"\bS\w+", txt)
# print(x.string)
#
# Print the part of the string where there was a match.
#
# The regular expression looks for any words that starts with an upper case "S":
#     txt = "The rain in Spain"
#     x = re.search(r"\bS\w+", txt)
#     print(x.group())
#
#
#
#
# import re
# pattern = r"cat" # Define a regular expression pattern
# text = "The cat in the car jumped out of the cab"
# match = re.search(pattern, text) # Search for the pattern in a string
# print(match.group()) # Print the match # "cat"
# # The search() method is used to search for the pattern in the string, and the group() method is used to extract the matching substring from the string.
# # pattern = r"ca*" # Define a regular expression pattern
# # text =  "The cat in the car jumped out of the cab"
# # match = re.search(pattern, text) # Search for the pattern in a string
# # print(match.group()) # Print the match # "cat"
#-----------------------------------------------------------------
# march
#-----------------------------------------------------------------
# any five letter string starting with a and ending with s.
# pattern = '^a...s$'
# test_string = 'abyss'
# result = re.match(pattern, test_string)
#
# if result:
#   print("Search successful.")
# else:
#   print("Search unsuccessful.")
#-----------------------------------------------------------------
# [] - Square brackets specifies a set of characters you wish to match
#-----------------------------------------------------------------