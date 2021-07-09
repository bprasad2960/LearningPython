#Author: Littl
#CreatedDate: 10th July 2021
# Example file for working with filesystem shell methods
#
import os
from os import path, rename
import shutil
from shutil import make_archive
from zipfile import ZipFile


def main():
  # make a duplicate of an existing file
  if path.exists("sample_txt.txt"):
    # get the path to the file in the current directory
    #str = os.path.realpath("sample_txt_file.txt")
    #dst = str+'bkp'
    # let's make a backup copy by appending "bak" to the name
   # shutil.copyfile(str,dst)

    # copy over the permissions, modification times, and other info
    #shutil.copystat(str,dst)
    
    # rename the original file
    #rename("sample_txt_file.txt","sample_txt.txt")
    
    # now put things into a ZIP archive
    #fld, fil = os.path.split(os.path.realpath("sample_txt.txt"))
    #print(fld, "\n" ,fil)
    #shutil.make_archive("archive","zip", fld)

    # more fine-grained control over ZIP files
    with ZipFile("zipped_file.zip","w") as zipper:
        zipper.write("sample_txt.txt")
        zipper.write("sample_txt_file.txtbkp") 

         
if __name__ == "__main__":
  main()
