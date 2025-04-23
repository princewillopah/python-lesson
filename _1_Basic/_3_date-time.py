
import os
os.system('cls')
print("----------------------------------------------------------------------------------------")
print(" RESULTS")
print("----------------------------------------------------------------------------------------")
print()
print()





# -----------------------------------------------------------
#
# ------------------------------------------------------------

import datetime
# x = datetime.datetime.now()
# print(x) # OUTPUT => 2023-04-15 11:54:06.425863 WHERE date contains year, month, day, hour, minute, second, and microsecond.
# # # ----------------------------------------
# x = datetime.datetime.now()
# print(x.year) # 2023
# print(x.strftime("%A")) # Saturday

# # # -----------------------------------------------------------
# # # datetime() - class (constructor) of the datetime module requires three parameters to create a date: year, month, day
# # # ------------------------------------------------------------
# x = datetime.datetime(2020, 5, 17)
# print(x)
# # The datetime() class also takes parameters for time and timezone (hour, minute, second, microsecond, tzone), but they are optional, and has a default value of 0, (None for timezone).
# # # -----------------------------------------------------------
# # # strftime() Method formatS date objects into readable strings  - takes one parameter, format, to specify the format of the returned string:
# # # ------------------------------------------------------------
# x = datetime.datetime(2018, 6, 1)
# print(x.strftime("%B"))

# ---------------------------------------------------------
#  FORMATS
# ------------------------------------------------------------

# %d	=>  Day of month 01-31	 EXAMPLE =>  31
# %a	=>  Weekday, short version	 EXAMPLE =>  Wed
# %A	=>  Weekday, full version	 EXAMPLE =>  Wednesday
# %b	=>  Month name, short version	 EXAMPLE =>  Dec
# %B	=>  Month name, full version	 EXAMPLE =>  December
# %y	=>  Year, short version, without century	 EXAMPLE =>  18
# %Y	=>  Year, full version	 EXAMPLE =>  2018

# %w	=>  Weekday as a number 0-6, 0 is Sunday	 EXAMPLE =>  3
# %m	=>  Month as a number 01-12	 EXAMPLE =>  12


# %H	=>  Hour 00-23	 EXAMPLE =>  17
# %I	=>  Hour 00-12	 EXAMPLE =>  05
# %p	=>  AM/PM	 EXAMPLE =>   EXAMPLE =>  PM
# %M	=>  Minute 00-59	 EXAMPLE =>  41
# %S	=>  Second 00-59	 EXAMPLE =>  08


# %f	=>  Microsecond 000000-999999	 EXAMPLE =>  548513
# %z	=>  UTC offset	 EXAMPLE =>  +0100
# %Z	=>  Timezone	 EXAMPLE =>  CST
# %j	=>  Day number of year 001-366	 EXAMPLE =>  365
# %U	=>  Week number of year, Sunday as the first day of week, 00-53	 EXAMPLE =>  52
# %W	=>  Week number of year, Monday as the first day of week, 00-53	 EXAMPLE =>  52
# %c	=>  Local version of date and time	Mon Dec 31 17:41:00  EXAMPLE =>  2018
# %C	=>  Century	 EXAMPLE =>  20
# %x	=>  Local version of date	 EXAMPLE =>  12/31/18
# %X	=>  Local version of time	 EXAMPLE =>  17:41:00
# %%	=>  A % character	 EXAMPLE =>  %
# %G	=>  ISO 8601 year	 EXAMPLE =>  2018
# %u	=>  ISO 8601 weekday (1-7)	 EXAMPLE =>  1
# %V	=>  ISO 8601 weeknumber (01-53)	 EXAMPLE =>  01

# # # ---------------------------------------------------------
# # #  Key Functions
# # # ------------------------------------------------------------

# # # datetime.datetime.now() – Get current date and time.
# # # datetime.date.today() – Get current date.
# # # datetime.date(year, month, day) – Create a specific date.
# # # datetime.timedelta(days=n) – Add/subtract days.
# # # relativedelta(months=n) – Add/subtract months (requires dateutil).
# # # strftime() – Format date.
# # # strptime() – Parse a date from a string.


# # # ---------------------------------------------------------
# # #  Getting the Current Date and Time
# # # ------------------------------------------------------------

# # Current date and time
# current_datetime = datetime.datetime.now()
# print("Current Date and Time:", current_datetime)

# # Only current date
# current_date = datetime.date.today()
# print("Current Date:", current_date)

# # Creating a specific date (Year, Month, Day)
# specific_date = datetime.date(2024, 9, 27)
# print("Specific Date:", specific_date)

# # Add 10 days to the current date
# future_date = current_date + datetime.timedelta(days=10)
# print("Date after 10 days:", future_date)

# # Subtract 5 days from the current date
# past_date = current_date - datetime.timedelta(days=5)
# print("Date 5 days ago:", past_date) 

# # # ---------------------------------------------------------
# # # ### Adding/Subtracting Months
# # # ------------------------------------------------------------

"""
There isn’t a direct method in datetime to add months, but you can use the dateutil.relativedelta module from the dateutil package.
pip install python-dateutil
"""
# from dateutil.relativedelta import relativedelta

# # Add 2 months to the current date
# future_date_months = current_date + relativedelta(months=2)
# print("Date after 2 months:", future_date_months)

# # Subtract 3 months from the current date
# past_date_months = current_date - relativedelta(months=3)
# print("Date 3 months ago:", past_date_months)
"""
Example: Adding Days and Months
Here's a complete example demonstrating how to add both days and months to a given date:
"""

# import datetime
# from dateutil.relativedelta import relativedelta

# # Current date
# current_date = datetime.date.today()
# print("Current Date:", current_date)

# # Add 15 days
# new_date = current_date + datetime.timedelta(days=15)
# print("Date after 15 days:", new_date)

# # Add 2 months
# new_date_months = current_date + relativedelta(months=2)
# print("Date after 2 months:", new_date_months)




# # # # ---------------------------------------------------------
# # # # ### Formatting Dates
# # # # ------------------------------------------------------------

# current_date = datetime.datetime.now()

# # Formatting date as Day-Month-Year
# formatted_date = current_date.strftime("%d-%m-%Y")

# print("Formatted Date:", formatted_date)

# More format options:
# %Y - Year (4 digits)
# %m - Month (2 digits)
# %d - Day (2 digits)
# %H - Hour (24-hour format)
# %M - Minute
# %S - Second


# # # ---------------------------------------------------------
# # # ### Parsing Dates from Strings
# # # ------------------------------------------------------------
### To convert a string representation of a date into a datetime object, you use strptime():

# Parsing a date string
# date_string = "15-09-2024"
# parsed_date = datetime.datetime.strptime(date_string, "%d-%m-%Y").date()
# print("Parsed Date:", parsed_date)


# # # ---------------------------------------------------------
# # # ### Difference Between Two Dates
# # # ------------------------------------------------------------
### To convert a string representation of a date into a datetime object, you use strptime():

# date1 = datetime.date(2024, 9, 1)
# date2 = datetime.date(2024, 9, 15)

# difference = date2 - date1
# print("Difference in days:", difference.days)



"""
A Python program that accepts user input and displays the user's current year, month, and day, you can combine the input() function to 
get the user’s input and use the datetime module to retrieve the current date details. 
Below is a simple example of how you can achieve this:
"""

# import datetime

# # Accept user input
# name = input("Please enter your name: ")

# # Get the current date
# current_date = datetime.datetime.now()

# # Extract year, month, and day
# current_year = current_date.year
# current_month = current_date.month
# current_day = current_date.day

# # Display the user's current year, month, and day
# print(f"Hello, {name}!")
# print(f"Today's date is: {current_year}-{current_month}-{current_day}")



"""
Python program that asks the user for their birthdate and calculates their age in terms of years, months, and days, you can 
use the datetime module to handle dates and perform the calculation. 
Here is how you can achieve that:
"""

# # # ---------------------------------------------------------
# # # Python Code to Calculate Age
# # # ------------------------------------------------------------


import datetime

def calculate_age(birthdate):
    # Get today's date
    today = datetime.date.today()
    
    # Calculate the difference in years, months, and days
    years = today.year - birthdate.year
    months = today.month - birthdate.month
    days = today.day - birthdate.day

    # Adjust if necessary for months or days
    if days < 0:
        months -= 1
        days += (today - datetime.timedelta(days=today.day)).day
    
    if months < 0:
        years -= 1
        months += 12

    return years, months, days

# Accept user input for birth year, month, and day
year = int(input("Enter your birth year (YYYY): "))
month = int(input("Enter your birth month (MM): "))
day = int(input("Enter your birth day (DD): "))

# Create a date object from the user's input
birthdate = datetime.date(year, month, day)

# Calculate the age
years, months, days = calculate_age(birthdate)


print(f"You are {years} years, {months} months, and {days} days old.") # Display the result

































































print()
print()
print()
print()
print("----------------------------------------------------------------------------------------")