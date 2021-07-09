# Author: Littl
# CreatedDate: 8th July 2021
# Example file for working with loops
#

def main():
  x = 0

  # define a while loop
  while (x<5):
      print (x)
      x = x+1

  # define a for loop
  for i in range(5,10,2):
      print(i)
    
  # use a for loop over a collection
  days =  ['Mon',"Tues","Wed"]
  for d in days:
      print(d)  
  # use the break and continue statements
  for i in range(1,10):
      print(i)
      if(i>7):
          break
      else:
        if(i%2==0):
              continue
      print(str(i), " is an odd number")

  #using the enumerate() function to get index 
  for d,i in enumerate(days):
      print(d,i)
if __name__ == "__main__":
  main()
