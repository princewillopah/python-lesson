# -----------------------------------------------------------
#
# ------------------------------------------------------------

import datetime
x = datetime.datetime.now()
print(x) # OUTPUT => 2023-04-15 11:54:06.425863 WHERE date contains year, month, day, hour, minute, second, and microsecond.
# ----------------------------------------
x = datetime.datetime.now()
print(x.year) # 2023
print(x.strftime("%A")) # Saturday

# -----------------------------------------------------------
# datetime() - class (constructor) of the datetime module requires three parameters to create a date: year, month, day
# ------------------------------------------------------------
x = datetime.datetime(2020, 5, 17)
print(x)
# The datetime() class also takes parameters for time and timezone (hour, minute, second, microsecond, tzone), but they are optional, and has a default value of 0, (None for timezone).
# -----------------------------------------------------------
# strftime() Method formatS date objects into readable strings  - takes one parameter, format, to specify the format of the returned string:
# ------------------------------------------------------------
x = datetime.datetime(2018, 6, 1)
print(x.strftime("%B"))

# ---------------------------------------------------------
#  FORMATS
# ------------------------------------------------------------
#
# %a	=>  Weekday, short version	 EXAMPLE =>  Wed
# %A	=>  Weekday, full version	 EXAMPLE =>  Wednesday
# %w	=>  Weekday as a number 0-6, 0 is Sunday	 EXAMPLE =>  3
# %d	=>  Day of month 01-31	 EXAMPLE =>  31
# %b	=>  Month name, short version	 EXAMPLE =>  Dec
# %B	=>  Month name, full version	 EXAMPLE =>  December
# %m	=>  Month as a number 01-12	 EXAMPLE =>  12
# %y	=>  Year, short version, without century	 EXAMPLE =>  18
# %Y	=>  Year, full version	 EXAMPLE =>  2018
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



