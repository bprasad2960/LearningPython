# Author: Littl
# CreatedDate: 8th July 2021
# Example file for working with timedelta objects
#

from datetime import date, timedelta
from datetime import time
from datetime import datetime


# construct a basic timedelta and print it
print(timedelta(days = 365, hours = 5, minutes = 1))

# print today's date
now = datetime.now()
print("Today's date is:" + str(now))

# print today's date one year from now
print("Today's date one year from now is: ", str(now +timedelta(days=365)))

# create a timedelta that uses more than one argument
print("Today's date one year and one month from now is: ", str(now +timedelta(days=365, weeks =4)))


# calculate the date 1 week ago, formatted as a string
print("Date 1 week ago from today is : ", (now - timedelta( weeks =1)).strftime("%Y:%M:%d"))


### How many days until April Fools' Day?
today = date.today()
april_1st = date(month= 4,year=today.year, day=1)
print(today)
print(april_1st)

# use date comparison to see if April Fool's has already gone for this year
if (april_1st < today):
    april_1st = date(month= 4,year=today.year+1, day=1)
    print("This year's april fool's day went" + str(april_1st))
    
else:
    april_1st = date(month= 4,year=today.year, day=1)
    print("This year's april fool's day is still"+ str(april_1st))

# if it has, use the replace() function to get the date for next year


# Now calculate the amount of time until April Fool's Day  
time_remaining = april_1st - date.today()
print(time_remaining)
