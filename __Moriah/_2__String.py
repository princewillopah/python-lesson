print()
###  =================================================================================================================
###  Escape sequences(character with backslash) and raw string
###  =================================================================================================================
# print("the lady in a blue gown has a pen. you can ask her for assistance")
# print(f"The lady in a blue gown has a pen. you can ask her for assistance")
# print('welcome to Geek\'s course')  ## Escape sequences(character with backslash)
# print("Hi \nwelcome to the course")  ## Escape backslash with n(\n)
# print("A simple \ example")  ## Escaping the backslash itself
# print("Backslash at the end\\")  ## Escaping the backslash itself
# print("\\n")  ## Escaping the backslash itself
# print("\\t")  ## Escaping the backslash itself
# print("c:\project\name.py")  ## Raw string
# print(r"c:\project\name.py")  ## Raw string


# print("welcome to \"geek\" course")
# print("welcome to 'geek' course")
# print("welcome to \"geek\" course")
# print('welcome to "geek" course')

# print('welcome to \'geek\' course')
# print("welcome to 'geek' course")

# print("the lady in a blue gown has a pen. \\nyou can ask her for assistance")

# print("the lady in a blue gown has a pen. you can ask her for assistance \\")


# name = "Tony"
# school = "Prominent High School"
# teacher = "Mrs Ann"
# DOB = 2010
# age = 2024 - DOB

# print("My name is {0} and i attend {1}. my teacher's name is {2}. {0} was born in {3}, therefor i am {4} years old. therefor this is {0} talking".format(name,school,teacher,DOB,age))
# print(f"My name is {name} and i attend {school}. my teacher's name is {teacher}. i was born in {DOB}, therefor i am {age} years old")


# name = "Tony"
# friend = "Amanda"

# print("i am {0}. i have a friend called {1} whose father is also called {0}".format(name,friend)) 



# print("Home economics, also called domestic science or family and consumer sciences (often shortened to FCS or FACS), is a subject concerning human development, personal and family finances, consumer issues, housing and interior design, nutrition and food preparation, as well as textiles and apparel.")

# print("""Home economics, also called domestic science or family and consumer 
# sciences (often shortened to FCS or FACS), is a subject concerning human development, 
# personal and family finances, consumer issues, housing and interior design, nutrition and
# food preparation, as well as textiles and apparel.
# """)

# print("""Dear Mr. Andrews,

# I’m writing to resign from my position as customer service representative, effective September 16, 2023.
# I’ve recently decided to go back to school, and my program starts in late September. I’m tendering my resignation now so that I can be as helpful as possible to you during the transition.
# I’ve truly enjoyed my time working with you and everyone else on our team at LMK. It’s rare to find a customer service role that offers as much opportunity to grow and learn, and perhaps more rare to find such a positive, inspiring team of people to grow and learn with.
# I’m particularly grateful for your guidance while I was considering furthering my education. Your support has meant so much to me. 

# Please let me know if there’s anything I can do to help you find and train my replacement.

# Thanks and best wishes,

# Signature (hard copy letter)

# Nicole Thomas
# """)

# workers = ['Mary', 'Jennifer', 'Linda', 'Patricia', 'Elizabeth','Mary' 'Barbara', 'Susan','Jessica', 'Sarah', 'Karen', "Alice",'Karen','Adam', 'Joseph', 'Leo', 'Peter', 'Evans','Mathew', 'Banabas', 'Smart','Joe', 'Smith', 'Ken', "Apolo",'Paul']




# for name in workers:
#        print(f"""Dear {name},

# I’m writing to inform you of my position as the Boss of customer service representative, effective September 16, 2023.
# I’ve recently decided to go back to school, and my program starts in late September. I’m tendering my resignation now so that I can be as helpful as possible to you during the transition.
# I’ve truly enjoyed my time working with you and everyone else on our team at LMK. It’s rare to find a customer service role that offers as much opportunity to grow and learn, and perhaps more rare to find such a positive, inspiring team of people to grow and learn with.
# I’m particularly grateful for your guidance while I was considering furthering my education. Your support has meant so much to me. 

# Please let me know if there’s anything I can do to help you find and train my replacement.

# Thanks and best wishes,
 
# Nicole Thomas
# The Manager
# Alincco Limited

# """)
# print()


###--------------------------------------------------
###   String Methods
###--------------------------------------------------
# print("Enter your Name")
# name = input()

# print(f"You said you name is {name}")
# print(f"You said you name is {name.capitalize()}")

# print("When where you born")
# answer = input()

# print(f"You mentioned that: {answer.upper()}")





# upper()	        Converts a string into upper case
# lower()     	    Converts a string into lower case
# capitalize()	    Converts the first character to upper case
# center()	        Returns a centered string
# format()	        Formats specified values in a string
# find()	        Searches the string for a specified value and returns the position of where it was found
# replace()   	    Returns a string where a specified value is replaced with a specified value
# count()	        Returns the number of times a specified value occurs in a string

# index()     	    Searches the string for a specified value and returns the position of where it was found
# split()     	    Splits the string at the specified separator, and returns a list
# zfill()       	Fills the string with a specified number of 0 values at the beginning
# expandtabs()	    Sets the tab size of the string
# join()      	    Joins the elements of an iterable to the end of the string

# casefold()	    Converts string into lower case
# splitlines()      Splits the string at line breaks and returns a list
# startswith()      Returns true if the string starts with the specified value
# strip()     	    Returns a trimmed version of the string
# swapcase()  	    Swaps cases, lower case becomes upper case and vice versa
# title()     	    Converts the first character of each word to upper case


# encode()	       Returns an encoded version of the string
# endswith()	       Returns true if the string ends with the specified value
# format_map()       Formats specified values in a string
# isalnum()   	Returns True if all characters in the string are alphanumeric
# isalpha()   	Returns True if all characters in the string are in the alphabet
# isascii()   	Returns True if all characters in the string are ascii characters
# isdecimal() 	Returns True if all characters in the string are decimals
# isdigit()   	Returns True if all characters in the string are digits
# isidentifier()     Returns True if the string is an identifier
# islower()   	Returns True if all characters in the string are lower case
# isnumeric() 	Returns True if all characters in the string are numeric
# isprintable()      Returns True if all characters in the string are printable
# isspace()   	Returns True if all characters in the string are whitespaces
# istitle()   	Returns True if the string follows the rules of a title
# isupper()   	Returns True if all characters in the string are upper case
# ljust()     	Returns a left justified version of the string
# lstrip()    	Returns a left trim version of the string
# maketrans() 	Returns a translation table to be used in translations
# partition() 	Returns a tuple where the string is parted into three parts
# rfind()     	Searches the string for a specified value and returns the last position of where it was found
# rindex()    	Searches the string for a specified value and returns the last position of where it was found
# rjust()     	Returns a right justified version of the string
# rpartition()       Returns a tuple where the string is parted into three parts
# rsplit()    	Splits the string at the specified separator, and returns a list
# rstrip()    	Returns a right trim version of the string
# translate() 	Returns a translated string






###--------------------------------------------------
###    
###--------------------------------------------------


###--------------------------------------------------
###    
###--------------------------------------------------



###--------------------------------------------------
###    
###--------------------------------------------------



###--------------------------------------------------
###    
###--------------------------------------------------


###--------------------------------------------------
###    
###--------------------------------------------------


###--------------------------------------------------
###    
###--------------------------------------------------


###--------------------------------------------------
###    
###--------------------------------------------------


###--------------------------------------------------
###    
###--------------------------------------------------


###--------------------------------------------------
###    
###--------------------------------------------------

###--------------------------------------------------
###    
###--------------------------------------------------


###--------------------------------------------------
###    
###--------------------------------------------------



###--------------------------------------------------
###    
###--------------------------------------------------


###--------------------------------------------------
###    
###--------------------------------------------------



###--------------------------------------------------
###    
###--------------------------------------------------



###--------------------------------------------------
###    
###--------------------------------------------------


###--------------------------------------------------
###    
###--------------------------------------------------


###--------------------------------------------------
###    
###--------------------------------------------------


###--------------------------------------------------
###    
###--------------------------------------------------


###--------------------------------------------------
###    
###--------------------------------------------------


###--------------------------------------------------
###    
###--------------------------------------------------

###--------------------------------------------------
###    
###--------------------------------------------------


###--------------------------------------------------
###    
###--------------------------------------------------



###--------------------------------------------------
###    
###--------------------------------------------------


###--------------------------------------------------
###    
###--------------------------------------------------



###--------------------------------------------------
###    
###--------------------------------------------------



###--------------------------------------------------
###    
###--------------------------------------------------


###--------------------------------------------------
###    
###--------------------------------------------------


###--------------------------------------------------
###    
###--------------------------------------------------


###--------------------------------------------------
###    
###--------------------------------------------------


###--------------------------------------------------
###    
###--------------------------------------------------


###--------------------------------------------------
###    
###--------------------------------------------------

###--------------------------------------------------
###    
###--------------------------------------------------


###--------------------------------------------------
###    
###--------------------------------------------------

















































print()