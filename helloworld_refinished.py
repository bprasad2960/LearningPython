#Author : Littl
#CreateDate: 7th July
#
#Purpose: Practise how to create a main function in python
#

#Define a funcion named main()
def main():
    print("Hello")
#Take user input
    name = input("what is your name?")
    print(f'Nice to meet you {name}!')

#Set the __name__ parameter to __main__ as this is the primary module and it should \\
#be called on its own

if __name__ == '__main__':
    main()