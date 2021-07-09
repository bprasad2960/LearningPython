# Author: Littl
# CreatedDate: 8th July 2021
# Example file for working with date information
#

from datetime import date
from datetime import time
from datetime import datetime

def main():
  ## DATE OBJECTS
  # Get today's date from the simple today() method from the date class
  today = date.today()
  print(today)

  # print out the date's individual components
  print(today.day)
  print(today.month)
  print(today.year)
  
  # retrieve today's weekday (0=Monday, 6=Sunday)
  print(today.weekday())
  
  ## DATETIME OBJECTS
  # Get today's date from the datetime class
  now = datetime.now()
  print(now)
  print(now.date())
  
  # Get the current time
  print(now.hour,now.minute,now.second)
  print(now.strftime("Current date is  %a, %d, %m, %y"))

if __name__ == "__main__":
  main();
  