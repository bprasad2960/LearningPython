#Author: Littl
#CreatedDate: 10th July 2021
# Read and write files using the built-in Python file methods
#

def main():  
  # Open a file for writing and create it if it doesn't exist
    f = open("sample_txt_file.txt", "w+")   # create a new file with 'x' -- write a disk file 'w+'
    for i in range(1,10):
        f.write("This is line number %d \n" %i)
    f.close()
  # Open the file for appending text to the end
    f = open("sample_txt_file.txt",'a')
    f.write("This is a new line appended\n")
  # write some lines of data to the file

  
  # close the file when done
    f.close()
  
  # Open the file back up and read the contents
    f = open("sample_txt_file.txt",'r')
    contents = f.read()
    f.close()
    f = open("sample_txt_file.txt",'r')
    contents1 = f.readlines()
    f.close()
    f = open("sample_txt_file.txt",'r')
    contents2 = f.readline()
    print(contents)
    print(type(contents))
    print(contents1)
    print(type(contents1))
    print(contents2)
    print(type(contents2))
    f.close()
    
if __name__ == "__main__":
  main()
