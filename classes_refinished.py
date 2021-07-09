# Author: Littl
# CreatedDate: 8th July 2021
# Example file for working with classes
#

#Define a class1

class myClass():

#Define methods inside class
    def method1(self):
        print("This is method 1 in myclass")
    def method2(self,stringname):
        print("This is method2 in myclass",stringname)

#Define another class inheriting from myClass
class anotherClass(myClass):

#Define method2 overriding super class method2
    def method1(self):
        myClass.method1(self)
        print("This is method1 in anotherClass")
    
    def method2(self,stringname):
        myClass.method2(self,"Calling from anotherClass method2")
        print("This is method2 in anotherClass",stringname)

def main():
    c1 = myClass()
    c1.method1()
    c1.method2("My Dear Littl!")
    c2 = anotherClass()
    c2.method1()
    c2.method2("My Dear Littl!")

if __name__ == "__main__":
    main()
