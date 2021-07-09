# Author: Littl
# CreatedDate: 7th July 2021
# Example file for working with functions
#

# define a basic function
def func1 ():
    print("I am a basic function!")

# function that takes arguments
def func2(arg1, arg2):
    print(arg1, " ", arg2)

# function that returns a value
def func3(arg1, arg2):
    return arg1+arg2

func1()
print("Calling func1: ", func1())
func2(2,3)
print("Calling func1: ", func2(2,3))
func3(2,3)
print("Calling func1: ", func3(2,3))
# function with default value for an argument

def func4(arg1, arg2=4):
    return arg1+arg2

print("Calling func4 with less parameters" ,func4(2))

print("Calling func4 with all parameters" ,func4(2,3))

#print("Calling func4 with less parameters in different order" ,func4(,2))   #invalid syntax

#function with variable number of arguments

def func5(*args):
    result = 0
    for i in args:
        result = result + i
    return result

print("Calling multi parameter function: ", func5(2,3,4,5,6,7))
print("Calling multi parameter function: ", func5(2,3,4,5))


#define a function with default arguments and call it in different order using names
def func6( x = 2, y= 3):
    print ("x cube value is :", x*x*x)
    print ("y cube value is :", y*y*y)
    return x**y

print(func6(5,6))
#print(func6(y=5,6))   #SyntaxError: positional argument follows keyword argument
print(func6(6,y=5))
#print(func6(5,x=6))   #TypeError: func6() got multiple values for argument 'x'
print(func6(y=5,x=6))
print(func6(6))
#print(func6(,6))   #SyntaxError: invalid syntax