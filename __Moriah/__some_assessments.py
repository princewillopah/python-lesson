import os
os.system('cls')
print("----------------------------------------------------------------------------------------")
print(" RESULTS")
print("----------------------------------------------------------------------------------------")
print()
print()


 
# 
# 1. add the maximum of 2 numbers wito 27 - this means it will find the maximum of 2 numbers, and them add it to 27
# 2. when a user provide 2 numbers, i want your code to find the sum, product, difference, and division, and max and minimum of those 2 number


# Zodiac Sign Date Ranges
# Aries: March 21 - April 19                  21 22 23 24 25 26 27 28 29 30 31   1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19         
# Taurus: April 20 - May 20
# Gemini: May 21 - June 20
# Cancer: June 21 - July 22
# Leo: July 23 - August 22
# Virgo: August 23 - September 22
# Libra: September 23 - October 22
# Scorpio: October 23 - November 21
# Sagittarius: November 22 - December 21
# Capricorn: December 22 - January 19
# Aquarius: January 20 - February 18
# Pisces: February 19 - March 20


# month = int(input("Enter your month(1 - 12) of birth: "))
# day = int(input("Enter your Day of birth: "))


# if (month == 1 and (day >= 1 and day <= 19)) or (month == 12 and (day >= 22 and day <= 31)):
#     print(f"This means you are Capricorn")
# elif month == 2:
#     print(f"You were born in February. This means you are either Pisces or Aquarius")   
# elif month == 3:
#     print(f"You were born in March. This means you are either Aries or Pisces")  
# elif month == 4:
#     print(f"You were born in April. This means you are either Aries or Taurus")  



# (day >= 19 and day <= 31) = 19 20 21 22 23 24 25 26 27 28 29 30 31 

# Capricorn: December 22 - January 19
# Aquarius: January 20 - February 18

# january from 19 - 31 
# Capricorn

# dec 22 23 24 25 26 27 28 29 30 31   (day >= 22 and day <= 31)
# jan 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19    (day >= 1 and day <= 19)



# age = int(input("enter age: "))

# if age > 40:     # 41 42 43 44 45 46............   10000000000000000000
#       print("You are an elder")
# elif age >= 18  and age <= 40:    #from 18 19 20 ........... 38 39 40     
#     print("You are an Youth")
# elif age >= 1 and age <= 17:      #  1 2 3 4 5 ...... 15 16 17
#      print("You are still a teen")
# elif age < 0:                           # -2 -3 -100 -99 -20000000 
#      print("You cannot have a negative age")
# else:
#      print("you have entered an invalid number")      

   

# i 2 3 4      .......   16 17 18 19 ....39 40






























# def get_zodiac_sign(day, month):
#     if (month == 3 and day >= 21) or (month == 4 and day <= 19):
#         return "Aries"
#     elif (month == 4 and day >= 20) or (month == 5 and day <= 20):
#         return "Taurus"
#     elif (month == 5 and day >= 21) or (month == 6 and day <= 20):
#         return "Gemini"
#     elif (month == 6 and day >= 21) or (month == 7 and day <= 22):
#         return "Cancer"
#     elif (month == 7 and day >= 23) or (month == 8 and day <= 22):
#         return "Leo"
#     elif (month == 8 and day >= 23) or (month == 9 and day <= 22):
#         return "Virgo"
#     elif (month == 9 and day >= 23) or (month == 10 and day <= 22):
#         return "Libra"
#     elif (month == 10 and day >= 23) or (month == 11 and day <= 21):
#         return "Scorpio"
#     elif (month == 11 and day >= 22) or (month == 12 and day <= 21):
#         return "Sagittarius"
#     elif (month == 12 and day >= 22) or (month == 1 and day <= 19):
#         return "Capricorn"
#     elif (month == 1 and day >= 20) or (month == 2 and day <= 18):
#         return "Aquarius"
#     elif (month == 2 and day >= 19) or (month == 3 and day <= 20):
#         return "Pisces"
#     else:
#         return "Invalid date"

# # Example usage
# day = int(input("Enter your birth day: "))
# month = int(input("Enter your birth month (1-12): "))

# zodiac_sign = get_zodiac_sign(day, month)
# print("Your Zodiac Sign is:", zodiac_sign)

# user_input = input("Continue?") #NO #no

# if user_input.lower().startswith("n"): 
#     print("Bye!")
# else:
#     print("Ok! Lets go again")

# "NO".lower()

# name = input("Pls enter your name: ")

# print(f"you are welcome to the club {name}")
# print(f"you are welcome to the club {name.lower()}")
# print(f"you are welcome to the club {name.lower().capitalize()}")

# print("Fruits: | Orange | Grape | Pineapple | Pawpaw | ")
# name = input("Mention one of the fruits i got from the market : ")


# if name.lower().startswith("pi"):
#     print("You got it right: I got Pineapple")
# elif name.startswith("or"):
#     print("You got it right: I got Orange")
# elif name.startswith("gr"):
#     print("You got it right: I got Grape")
# elif name.startswith("pa"):
#     print("You got it right: I got Pawpaw")
# else:
#     print(f"""You failed 
# The fruits i got are  | Orange | Grape | Pineapple | Pawpaw |
#           """)
    

# if False:
#     print("Bye!")
# elif True:
#     print("Ok! its me")
# else:
#     print("Ok! Lets go again")

# 5 > 2 True
# 2 > 5 False





# my_list1  = [1, "James", [-52.8,"Bond"]] 
# my_list2  = [["Captain",13],["America",14]]
# # my_list   = [my_list1, my_list2] # = [[1, "James", [-52.8,"Bond"]],[["Captain",13],["America",14]]]
my_list   = [
    [1, "James", [-52.8,"Bond"]],[["Captain",13],["America",14]]
    ]


# print(my_list)
# n = ["Tom","Jane"]
# n[1]

# name = ["Amanda","Grace","john","Hope",["Tom","Jane"],["Anna","PAUL","Bukky","Sandra"]]
# name 


mylist = [5,45,56,10,"sandra",True,"Bolhjdhd","i AM GOINT TO SCHOOL",["XXlarge","Paul","laugh",["jane","tom","Paul"],"cry","smile"]]

# 5
# 45
# 56
# 10
# sandra
# True
# Bolhjdhd
# i AM GOINT TO SCHOOL
# ["XXlarge","Paul","laugh",["jane","tom","Paul"],"cry","smile"]

# print(mylist[8])
# print(mylist[8][1])
# print(mylist[8][3][1])

# greatGranny = ["Jane","Tom",["jane","tom","Paul",["Jude","Joseph","Lakeside"],"Bukky","Sandra"],"Paul","Sandra"]  # 5 elements
# # print(len(greatGranny))
# # print()
# # for i in greatGranny:
# #     print(i)

# print(greatGranny[2])
# print(greatGranny[2][3][1])

# a list can contain several dat and the data can be of different datatype
# integer or float 1 2 3 4 5 6 7 7.8 0.987
# string: "A", "I am going" "djhdfjh34" "true or false" "23"
# boolean: True, False
# list  inside a list



# list1 = [4,6,2,"bread",[2,3,4],"Amanda",True,"7.8","d",["Lola","Afred","Tony","Hector"],2.34,-7,"-21.34"]
# list2 = []
# list3 = [1,2,5,7,9,2,6,2,8]
# list4 = [2,3,5,7,11,13,17,19,23,29,31] # list of prine numbers
# list5 = [2,4,6,8,10,12,14,16,18,20]   # list of even numbers from 2 - 20
# list6 = [1,3,5,7,9,11,13,15,17,19]  # list of odd numbers from 1 - 19
# list7 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]  # list of natural numbers from 1 - 20
# list8 = [-20,-19,-18,-17,-16,-15,-14,-13,-12,-11,-10,-9,-8,-7,-6,-5,-4,-3,-2,-1,0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]  # list of integers from -20 to 20
# list9 = [3,6,9,12,15,18,21] # list of multiple of 3
# list10 = ["Anna","Amanda","Adams","Bridget","Bukky","Zara"]



# print(f"i have a list of names. this is the list: {list10}")
# print(f"they are {len(list10)} in numbers")
# print("The names are: ")
# for name in list10:
#      print(name)

# print()
# print()

# list10[2] = "Belinda"

# # print(f"i have a list of names. this is the list: {list10}")
# print(f"they are {len(list1)} elements in the list")
# # print("The names are: ")
# for i in list1:
#      print(i)
 
# print(greatGranny[2][3][1])
# print(mylist[8][3][1])

# print(name[4])  #['Tom', 'Jane']
# print(name[4][0])
# print(name[5][2])

# ========================================

# i = 15
# while i > 0:
#     if i % 5 == 0:
#         print(i)
#     i = i - 1

# i = 15

# while 1 > 2:
#     print("yes")

# i = 15
# while i > 0:
#     print("yes")
#     i = i - 1

# while True:
#     print("Yes")

# for i in range(1,16): # [1,2,3,4,5,6,7,8,9,10,11,12,13,14]
#     print(i)


# print(1)
# print(2)
# print(3)
# print(4)
# print(5)
# print(6)
# print(7)
# print(8)
# print(9)
# print(10)
# print(11)
# print(12)
# print(13)
# print(14)
# print(15)

# even = []

# for i in range(1,21):  # [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20] 
#     if i % 2 == 0:
#         even.append(i)

# print(even)


# number = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20] 

# for i in number:
#     if i % 2 == 0:
#         print(f"{i} is an even number")

# list5 = [2,4,6,8,10,12,14,16,18,20]

# 
# customer_response = True

# while customer_response:
#     print("""Do you want to get another Item: y for "yes" and n for "NO" """)

# else:
#     print("""Thank you for patronizing us""")

















# girl_names = ["Sophia", "Olivia", "Ava", "Charlotte", "Amelia", "Harper", "Evelyn", "Abigail", "Emily", "Lily", "Madison", "Victoria", "Jessica", "Samantha", "Avery", "Riley", "Zoe", "Nina", "Gabriella","Julianne"]

# chosen_person = "olivia"

# for i in range(10):
#     answer = input("Enter the name that was chosen: ")
#     answer = answer.lower()

#     if answer == chosen_person:
#         print(f"Yeah!!! you got it right. {chosen_person.capitalize()} was the chosen one")
#         break
#     else:
#         print(f"You Failed. {answer.capitalize()} was NOT the chosen one")

# print("The End")

   

# True:
# False:

# 5 > 2 true
# 5 >= 2 True
# 2 = 5  false
# 2 > 5 False



# if 1 < 4 - 0:
#     print("I am John. I am Strong!")

# if 4 <= 3+1:
#      print("I am Tom. I am Better")

# if 6 / 3 == 2 - 0:
#     print("I am Jude. I am stronger!")

# if 7 >= 4+2 :
#     print("I am  Paul. I am Powerful!")

# if 3 > 1+1:
#     print("Thare are all weak. I am Toney .i am the strongest")





# if 1 > 4 - 0:
#     print("I am John. I am Strong!")

# elif 0 <= 3+1:
#      print("I am Tom. I am Better")

# elif 6 / 3 == 2 - 0:
#     print("I am Jude. I am stronger!")

# elif 7 >= 4+2 :
#     print("I am  Paul. I am Powerful!")

# elif 3 > 1+1:
#     print("Thare are all weak. I am Toney .i am the strongest")




# if True:
#     print("I am John. I am Strong!")

# if False:
#      print("I am Tom. I am Better")

# if True:
#     print("I am Jude. I am stronger!")

# if True:
#     print("I am  Paul. I am Powerful!")

# if False:
#     print("Thare are all weak. I am Toney .i am the strongest")







# if 1 > 4:
#     print("John")

# elif 2 < 0:
#      print("Tom")

# elif 6 == 2:
#     print("Jude")

# elif 7 >= 9 :
#     print(" Paul")

# elif 1 > 2:
#     print("Tony")
# else:
#     print("Me")



# if 1 > 4:
#     print("John")

# if 2 < 0:
#      print("Tom")

# if 6 == 2:
#     print("Jude")

# if 7 >= 9 :
#     print(" Paul")

# if 1 > 2:
#     print("Tony")


# name = input("Enter your name: ")

# for i in [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19]:
#     print(f"{i} Hello {name}")

# for i in range(1,21):
#      print(f"{i} Hello {name}")




# [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19]

# name = ["Anna", "Alice", "Agatha", "Amanda", "Anbolyn"]

# for i in name:
#     print(i)

# name_of_girls = []

# for i in name_of_girls:
#     print(i)

# for i in range(5):
#     name = input("Enter your name: ")
#     name_of_girls.append(name)

# for i in name_of_girls:
#     print(i)

# num = 5

# while 15 >= num:    # true
#     print(num)
#     num = num + 2


# 15 > 1 True print( 1)
# 15 > 2 True print( 2)
# 15 > 3 True print( 3)
# 15 > 4 True print( 4)
# 15 > 5 True print( 5)
# 15 > 6 True print( 6)
# 15 > 7 True print( 7)
# 15 > 8 True print( 8)
# 15 > 9 True print( 9)
# 15 > 10 True print( 10)
# 15 > 11 True print( 11)
# 15 > 12 True print( 12)
# 15 > 13 True print( 13)
# 15 > 14 True print( 14)
# 15 > 15 False 





# 15 > 5 True print( 5)
# 15 > 7 True print( 7)
# 15 > 9 True print( 9)
# 15 > 11 True print( 11)
# 15 > 13 True print( 13)
# 15 > 15 False




# answer = "y"

# while answer == "y":
#     answer = input("Do you want to buy something else? (y=Yes and n=NO): ")
#     if answer == "y":
#         item = input("Enter item: ")
#         num = int(input("Enter the numner of quantity: "))
#     else:
#         answer = "n"
#         print("Thank you for you patronage")


 
# names = ["Anna","Blessing","Cathrine","Doris","Emily","Faith","Gloriah","Helen","Iris","Jenet","Kate","Lian","Moriah","Nosa","Oprah","Patricial","Queenet","Ruth","Sandra","Tianna","Ucheriah","Vivian","Whitney","Xena","Yvonne ","Zara"]

# words = "I AM GOING TO SCHOOL"
# print(f" there are {len(word)} characters in '{word}'")
# print(f" there are {len(names)} names in {names}")


# for i in names:
#     if len(i) >= 5:
#         print(i)

# for i in names:
#         i = i.upper()
#         print(i)

    # print(i,end="")

# vowel = "AEIOU"
# for i in words:
#     if i != " " and i not in vowel:
#        print(i)


# user_words= input("Enter your words: " )



# total_nume_of_words = user_words.split(" ") 
# sentence = user_words.split(".")
# print()
# print(f"""Your message contains:
# {len(user_words)} characters
# {len(total_nume_of_words)} words
# {len(sentence)} sentences
# 1 paragragh
# """)

# write a program that will look for any item that cons 4 or less character, if found, your promgram will add "l" at the end of "a". howeer, if the 4 letter words end with any other characters, add "baby"



# name = input("Enter your name: ")


# if len(name) < 5:
#    if name.endswith("a"):
#      name  = name+"l"
#      print(f"i am going to call you {name}")
#    else:
#        name  = name+"baby"
#        print(f"i am going to call you {name}")  
# else:
#    print(f"i am going to call you {name}")



# For Loop: Used when you know in advance how many times you want to repeat a block of code.
# Think of a for loop as something that counts up to a certain number. It’s like saying, “Do this action 5 times.”
# Let's print numbers from 1 to 5 using a for loop

# for number in range(3, 20, 4): # [3, 7, 11, 15, 19]
#     print(number)
    

# While Loop: Used when you want to repeat a block of code until a specific condition is no longer true.
# Think of a while loop like a question: "Keep doing this as long as the answer is yes." It repeats until the condition becomes false.



# Let's print numbers from 5 to 1 using a while loop

names = [
    "Alice", "Bella", "Chloe", "Daisy", "Ella",
    "Fiona", "Grace", "Hannah", "Isla", "Jasmine",
    "Katie", "Lily", "Maya", "Nina", "Olivia",
    "Paige", "Quinn", "Rose", "Sophia", "Tessa",
    "Uma", "Violet", "Willow", "Moriah" "Xena", "Yara",
    "Zoe", "Amelia", "Brooke", "Claire", "Diana"
]

# for i in names:
#     if len(i) >= 5:
#        print(i) 


# for i in names:
#     print(i)

for i in names:
    i = i.lower()
    if "a" not in i:
        print(i)




# # for i in names:
# #     print(i)
# three_letters_list = []
# four_letters_list = []
# five_or_more_letters_list = []

# for i in names:
#    if len(i) == 3:
#       i = "Beautiful " + i
#       three_letters_list.append(i)
#    elif len(i) == 4:
#       i = "Good " + i
#       four_letters_list.append(i)
#    else:
#       five_or_more_letters_list.append(i)


# for i in three_letters_list:
#    print(i)

# print()

# for i in four_letters_list:
#    print(i)

# print()

# for i in five_or_more_letters_list:
#    print(i)









# while names != "Moriah"
#      print

# count = 5
# while count > 0:
#     print(count)
#     count -= 1  # Decrease count by 1 each time


# name = "Alice"
# for letter in name:
#     print(letter)





# write a program that will look for any item that contains 4 or less character, 
# if found, your promgram will add "l" at the end of "a". howeer, if the 4 letter words end with any other characters, add "baby"































print()
print()
print()
print()
print("----------------------------------------------------------------------------------------")
