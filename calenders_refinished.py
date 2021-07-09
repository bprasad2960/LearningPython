# Author: Littl
# CreatedDate: 8th July 2021
# Example file for working with Calendars
#

# import the calendar module
import calendar

# create a plain text calendar
c = calendar.TextCalendar(firstweekday=1)
str = c.formatmonth(2017,1,0,0)
print(str)

# create an HTML formatted calendar
h = calendar.HTMLCalendar(1)
str = h.formatmonth(2017,1,True)
print(str)
# loop over the days of a month

for i in c.itermonthdays(2020,4):
    print(i)

# zeroes mean that the day of the week is in an overlapping month

  
# The Calendar module provides useful utilities for the given locale,
# such as the names of days and months in both full and abbreviated forms
for name in calendar.month_name:
    print(name)

for name in calendar.day_name:
    print(name)

# Calculate days based on a rule: For example, consider
# a team meeting on the first Friday of every month.
# To figure out what days that would be for each month,
# we can use this script:

for i in range(1,13):
    c = calendar.monthcalendar(2020,i)
    weekone = c[0]
    weektwo = c[1]

    if (weekone[calendar.FRIDAY] != 0):
        meetday = weekone[calendar.FRIDAY]
    else:
        meetday = weektwo[calendar.FRIDAY]
    print(calendar.month_name[i], meetday)