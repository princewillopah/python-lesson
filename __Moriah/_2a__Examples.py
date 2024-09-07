print("----------------------------------------------------------------------")
print()

###--------------------------------------------------
###   examples
###--------------------------------------------------


# print("I AM GOING TO THE MARKET TODAY")
# print(str(4))
# length_of_string = len("we are going to the market")
# print(length_of_string)


###--------------------------------------------------
### upper() | Lower() | capitalize()
###--------------------------------------------------
# name = input("Enter your name: ")
# print()
# name = name.upper()
# print(f"Hello {name}, you are welcome to the club")
# name = name.lower()
# print(f"Hope you will be comfortable, {name}")
# name = name.capitalize()
# print(f"Hi {name}, I think i am pronouncing your name correctly")

### Example
# name = input('Please enter your name : ')
 
# name = name.capitalize()
 
# yob =int(input('What year where you born? : '))
# age = 2024 - yob
 
# ## print(f'According to what you have entered your name is {name}')
# ## print(f'and you are {age} years old')
 
 
# print(f'''
# Hello {name},
# According to what you have entered the year of birth is {yob}
# and you are {age} years old.
# ''')
###--------------------------------------------------
### center()
###--------------------------------------------------
# text = "hello"
# centered_text = text.center(30, '-')
# print(centered_text)  # Output: -------hello--------


###--------------------------------------------------
### format()
###--------------------------------------------------

# num1 = 55
# num2 = 20
# print(f"{num1} + {num2} = {num1+num2}")
# answer = num1+num2
# print("{} + {} = {}".format(num1,num2,answer))

# name="moriah"
# yob=2012
# age = 2024 - yob

# print(f"""
# Hello {name},
# According to what you entered, you year of birth is {yob}
# your age is now {age}
# """)

# print("""
# Hello {},
# According to what you entered, you year of birth is {}
# your age is now {}
# """.format(name,yob,age))

###----------------------------------------------------------------
### find()  -- this will return the index of what you are looking for. if it did not find what you are looking for, it will return "-1"
###--------------------------------------------------
# story = """Once upon a time in a bustling town called Techville, there was a young coder named Alex. Alex was known far and wide for his love of technology and his incredible ability to solve complex problems with ease. However, there was one thing Alex had always dreamed of doing but had never attempted: building a robot.

# One sunny afternoon, while wandering through the town's market, Alex stumbled upon an old, dusty bookstore. Drawn to the store's mysterious aura, he decided to venture inside. The shelves were lined with ancient books and manuals, each one a treasure trove of forgotten knowledge. In the back corner, he found a book titled "The Art of Robotics."

# Excited, Alex bought the book and hurried home. He spent the next several weeks poring over the book, learning about circuits, sensors, and programming. He began collecting spare parts from various places around town: old electronics from the recycling center, gears from the local clockmaker, and wires from the hardware store. With each new piece, his vision of the robot became clearer.

# As Alex worked day and night, his friends in Techville grew curious. They would often stop by his workshop to see his progress and offer encouragement. Despite the challenges and occasional setbacks, Alex's determination never wavered. He meticulously assembled each component, soldered every connection, and wrote lines of code until he finally completed his creation.

# On a crisp autumn morning, Alex was ready to bring his robot to life. He gathered his friends and family in his workshop, their faces filled with anticipation. With a deep breath, he flipped the switch. The robot's eyes flickered to life, and it began to move. It wasn't just a robot; it was a marvel of engineering, capable of performing tasks, learning from its environment, and even holding simple conversations.

# The townspeople were amazed. Alex's robot quickly became a beloved member of the community, helping with daily chores, teaching children about technology, and even assisting the elderly with tasks they found difficult. Alex's dream had come true, and in the process, he had inspired a new generation of young tech enthusiasts in Techville.

# The story of Alex and his robot spread far and wide, becoming a legend in its own right. And so, in the town of Techville, where technology and creativity thrived, the spirit of innovation continued to grow, thanks to a young coder's dream and his unwavering perseverance."""


# name = "Moriah"
# #         012345
# what_am_i_looking_for = "t"
# result = name.find(what_am_i_looking_for)  # -1 or index


# if  result == -1:
#     print(f"We did not find  '{what_am_i_looking_for}' in {name} ")
# else:
#     print(f"We Found '{what_am_i_looking_for}' in {name} and it is in the {result} position")


# search = input("Enter what you want to search: ")
# result = story.find(search)  # return index of the searched word or return -1 if the searched word is not found

# # if result == -1:
# #     print(f"sorry, I can not find {search}")
# # else:
# #     print(f"Yeah, we located {search} at the {result}th position")

# if result > -1: #0,1,2,3,4,5,5,6,77,8,,899,,900,,0
#      print(f"Yeah, we located {search} at the {result}th position")
# else:
#      print(f"sorry, I can not find {search}") 

###--------------------------------------------------
### count()
###--------------------------------------------------

# story = """Once upon a time in a bustling town called Techville, there was a young coder named Alex. Alex was known far and wide for his love of technology and his incredible ability to solve complex problems with ease. However, there was one thing Alex had always dreamed of doing but had never attempted: building a robot.

# One sunny afternoon, while wandering through the town's market, Alex stumbled upon an old, dusty bookstore. Drawn to the store's mysterious aura, he decided to venture inside. The shelves were lined with ancient books and manuals, each one a treasure trove of forgotten knowledge. In the back corner, he found a book titled "The Art of Robotics."

# Excited, Alex bought the book and hurried home. He spent the next several weeks poring over the book, learning about circuits, sensors, and programming. He began collecting spare parts from various places around town: old electronics from the recycling center, gears from the local clockmaker, and wires from the hardware store. With each new piece, his vision of the robot became clearer.

# As Alex worked day and night, his friends in Techville grew curious. They would often stop by his workshop to see his progress and offer encouragement. Despite the challenges and occasional setbacks, Alex's determination never wavered. He meticulously assembled each component, soldered every connection, and wrote lines of code until he finally completed his creation.

# On a crisp autumn morning, Alex was ready to bring his robot to life. He gathered his friends and family in his workshop, their faces filled with anticipation. With a deep breath, he flipped the switch. The robot's eyes flickered to life, and it began to move. It wasn't just a robot; it was a marvel of engineering, capable of performing tasks, learning from its environment, and even holding simple conversations.

# The townspeople were amazed. Alex's robot quickly became a beloved member of the community, helping with daily chores, teaching children about technology, and even assisting the elderly with tasks they found difficult. Alex's dream had come true, and in the process, he had inspired a new generation of young tech enthusiasts in Techville.

# The story of Alex and his robot spread far and wide, becoming a legend in its own right. And so, in the town of Techville, where technology and creativity thrived, the spirit of innovation continued to grow, thanks to a young coder's dream and his unwavering perseverance."""

# what_i_want_to_count = "Alex"
# result = story.count(what_i_want_to_count)

# print(f"{what_i_want_to_count} appears {result} times")
# -----------------------
# print("Enter a story you know")
# story = input()
# main_character = input("Enter Main Character: ")


# result = story.count(main_character)


# print()
# print(f" {main_character} is mentioned {result} times in your story")

# -----------------------





















###--------------------------------------------------
### replace()  
###--------------------------------------------------

# my_name = "Joshuah"
# print(my_name)
# my_name  = my_name.replace("oshuah","osh")
# print(my_name)


# story = """Once upon a time in a bustling town called Techville, there was a young coder named Alex. Alex was known far and wide for his love of technology and his incredible ability to solve complex problems with ease. However, there was one thing Alex had always dreamed of doing but had never attempted: building a robot.

# One sunny afternoon, while wandering through the town's market, Alex stumbled upon an old, dusty bookstore. Drawn to the store's mysterious aura, he decided to venture inside. The shelves were lined with ancient books and manuals, each one a treasure trove of forgotten knowledge. In the back corner, he found a book titled "The Art of Robotics."

# Excited, Alex bought the book and hurried home. He spent the next several weeks poring over the book, learning about circuits, sensors, and programming. He began collecting spare parts from various places around town: old electronics from the recycling center, gears from the local clockmaker, and wires from the hardware store. With each new piece, his vision of the robot became clearer.

# As Alex worked day and night, his friends in Techville grew curious. They would often stop by his workshop to see his progress and offer encouragement. Despite the challenges and occasional setbacks, Alex's determination never wavered. He meticulously assembled each component, soldered every connection, and wrote lines of code until he finally completed his creation.

# On a crisp autumn morning, Alex was ready to bring his robot to life. He gathered his friends and family in his workshop, their faces filled with anticipation. With a deep breath, he flipped the switch. The robot's eyes flickered to life, and it began to move. It wasn't just a robot; it was a marvel of engineering, capable of performing tasks, learning from its environment, and even holding simple conversations.

# The townspeople were amazed. Alex's robot quickly became a beloved member of the community, helping with daily chores, teaching children about technology, and even assisting the elderly with tasks they found difficult. Alex's dream had come true, and in the process, he had inspired a new generation of young tech enthusiasts in Techville.

# The story of Alex and his robot spread far and wide, becoming a legend in its own right. And so, in the town of Techville, where technology and creativity thrived, the spirit of innovation continued to grow, thanks to a young coder's dream and his unwavering perseverance."""

# story = story.replace("Alex","Josh")
# story = story.replace("Techville","London")

# print(story)

# ------------------------


# script = """
# "Goldilocks and the Three Bears"

# Once upon a time, a curious girl named Goldilocks wandered into a forest and came across a cozy little house belonging to a family of bears: Great Big Papa Bear, Middle-Sized Mama Bear, and Little Baby Bear.

# While the bears were away, Goldilocks knocked on the door, and when no one answered, she took it upon herself to enter the house. She saw three bowls of porridge on the table and tasted each one.

# "Too hot!" Goldilocks exclaimed, tasting Papa Bear's porridge.
# "Too cold!" she said, tasting Mama Bear's porridge.
# "Just right!" she said, tasting Baby Bear's porridge, and she ate it all up.

# Next, Goldilocks sat in the living room and saw three chairs. She sat in Papa Bear's chair, but it was too hard. She sat in Mama Bear's chair, but it was too soft. Then she sat in Baby Bear's chair, and it was just right.

# Feeling tired, Goldilocks went upstairs and saw three beds. She lay down in Papa Bear's bed, but it was too big. She lay down in Mama Bear's bed, but it was too small. Then she lay down in Baby Bear's bed, and it was just right. Goldilocks fell fast asleep.

# Meanwhile, the three bears returned home and found their porridge had been tasted, their chairs had been sat in, and someone was sleeping in Baby Bear's bed! They soon discovered Goldilocks and woke her up.

# Goldilocks quickly ran out of the house, and from then on, she never forgot her encounter with the three bears: Great Big Papa Bear, Middle-Sized Mama Bear, and Little Baby Bear.

# The repeated name in this story is "Bear", which appears several times to refer to the three members of the bear family.
# """


# script = script.replace("Goldilocks","Panda")
# print(script)


###------------------------------------------------------------------------------------------------------------------------------------------------------
### index()     	    Searches the string for a specified value and returns the position of where it was found
###------------------------------------------------------------------------------------------------------------------------------------------------------


# text = "Hello, World!"
# print(text.index("World"))  # Output: 7
# print(text.index(","))  # Output: 5
# print(text.index("H"))  # Output: 0

###------------------------------------------------------------------------------------------------------------------------------------------------------
### split()     	    Splits the string at the specified separator, and returns a list
###------------------------------------------------------------------------------------------------------------------------------------------------------

# text = "apple,banana,cherry"
# print(text.split(","))  # Output: ["apple", "banana", "cherry"]
# print(text.split(",", 1))  # Output: ["apple", "banana,cherry"]

# text = "Hello World"
# print(text.split())  # Output: ["Hello", "World"]

# # Splitting with a specified separator:
# text = "123-456-789"
# print(text.split("-"))  # Output: ["123", "456", "789"]

###------------------------------------------------------------------------------------------------------------------------------------------------------
###  zfill()       	Fills the string with a specified number of 0 values at the beginning
###------------------------------------------------------------------------------------------------------------------------------------------------------
import random


print("Welcome to the Dice Game!")
print("Think of two numbers between 1 and 6.")

guess1 = int(input("Guess the first number: "))  # 5
guess2 = int(input("Guess the second number: "))  # 6

dice1 = random.randint(1, 6)   # 5
dice2 = random.randint(1, 6)   # 4



print(f"\nYou guessed: {guess1}, {guess2}")   # 5 and 6
print(f"The numbers were: {dice1}, {dice2}\n")  # 5 and 4

if guess1 == dice1 and guess2 == dice2:
        print(" Congratulations! You got it right!")
else:
        print("Sorry, try again next time!")

# -----------------------

# number = int(input("guess a number between 9 and 11: "))

# answer = random.randint(9, 11)

# if number == answer:
#     print("you got it right")
# else:
#     print("you failed")
#     print(f"the correct anwer is {answer}")






# text = "23"
# print(text.zfill(9))  # Output: "00123"
# print(text.zfill(3))  # Output: "123"

# text = "-123"
# print(text.zfill(5))  # Output: "-0123"




###------------------------------------------------------------------------------------------------------------------------------------------------------
### expandtabs()	    Sets the tab size of the string
###------------------------------------------------------------------------------------------------------------------------------------------------------

###------------------------------------------------------------------------------------------------------------------------------------------------------
### join()      	    Joins the elements of an iterable to the end of the string
###------------------------------------------------------------------------------------------------------------------------------------------------------



###----------------------------------------------------------------------------------------------------
###  casefold()	    Converts string into lower case  
###----------------------------------------------------------------------------------------------------
# text = "HI, My name is ADAm and i am NOT Great at playING FootBall!"
# print(text.casefold())  # Output: "hello, world!"
# print(text.lower())

###----------------------------------------------------------------------------------------------------
###   splitlines()      Splits the string at line breaks and returns a list 
###----------------------------------------------------------------------------------------------------

# text = "Hello\nWorld!\nThis is a test."
# # print(text)
# print(text.splitlines())  # Output: ["Hello", "World!", "This is a test."]

###----------------------------------------------------------------------------------------------------
###   startswith()      Returns true if the string starts with the specified value 
###----------------------------------------------------------------------------------------------------
# text = "Hello, World!"
# print(text.startswith("Hello"))  # Output: True
# print(text.startswith("World"))  # Output: False

# print("You are allowed to enter this clud if and only if your name starts with 'P'")
# name = input("ENter your name: ")

# if name.startswith('P') or name.startswith('p'):
#     print(f" Heyy, {name}  you are qualified to be part of this club")
# else:
#     print(f" Sorry, {name}  you are NOT qualified to be part of this club")




###----------------------------------------------------------------------------------------------------
###   strip()     	    Returns a trimmed version of the string 
###----------------------------------------------------------------------------------------------------

# text = "   Hello, World!   "
# print(text)

# print(text.strip())  # Output: "Hello, World!"

###----------------------------------------------------------------------------------------------------
###    swapcase()  	    Swaps cases, lower case becomes upper case and vice versa
###----------------------------------------------------------------------------------------------------

# text = "Hello, World!"
# print(text.swapcase())  # Output: "hELLO, wORLD!"

###----------------------------------------------------------------------------------------------------
###    title()     	    Converts the first character of each word to upper case
###----------------------------------------------------------------------------------------------------

# text = "my name is john and i am going to be a programmer someday"
# print(text.title())  # Output: "Hello World"



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
print("----------------------------------------------------------------------")