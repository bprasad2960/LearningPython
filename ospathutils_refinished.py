#Author: Littl
#CreatedDate: 10th July 2021
# Example file for working with os.path module
#
import datetime
import os
import time
from datetime import date, time, timedelta
from os import path


def main():
  # Print the name of the OS
    print(os.name)  #nt
  
  # Check for item existence and type
    print("The file sample_txt_file.txt exists:", os.path.exists("sample_txt_file.txt") )
    print("The file path sample_txt_file.txt is a file?", os.path.isfile("sample_txt_file.txt") )
    print("The file path sample_txt_file.txt is a directory? ", os.path.isdir("sample_txt_file.txt") )
    print("The file path sample_txt_file.txt is a link?", os.path.islink("sample_txt_file.txt") )
  # Work with file paths
    print("Absolute path" , os.path.abspath("sample_txt_files.txt"))
    print("Directory name" , os.path.dirname(os.path.abspath("sample_txt_files.txt")))
    print("Split name" , os.path.split(os.path.abspath("sample_txt_files.txt")))
  
  # Get the modification time
    print("Last access time is:", datetime.datetime.fromtimestamp(os.path.getatime("sample_txt_file.txt")))
    print("Last modification time is:", datetime.datetime.fromtimestamp(os.path.getmtime("sample_txt_file.txt")))
    print("Created time is:", datetime.datetime.fromtimestamp(os.path.getctime("sample_txt_file.txt")))

  # Calculate how long ago the item was modified
    timediff = datetime.datetime.now() - datetime.datetime.fromtimestamp(os.path.getatime("sample_txt_file.txt"))
    print(type(timediff))  #timedelta
    print("This was last modified since %d days"%(timediff).days)
  
if __name__ == "__main__":
  main()
