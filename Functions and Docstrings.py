#Functions
''''
Types of functions
1)built-in functions
2)user defined functions(using def keyboard)
'''
#built-in functions
a=4
b=5
c=sum((a,b))#here the sum() is functions and they are built-in function
print(c)
#user-defined functions 
def functions1():
    print("Hello!you are in functions1")
functions1()#it it will only print Hello!you are in functions1 
'''
print(functions1())#it helps to print the Hello!you are in functions1 and none
'''
#if we want to print statement multiple times then we can write
functions1()#this is called calling the functions
functions1()
functions1()
functions1()
functions1()
#fuctions can also take input

def Mesup(a,b):
    print("hello! Mesup",a+b)
Mesup(12,5)
#we can also write like this 
a=3
b=5
def mesup(a,b):
    print("hello",a+b)
mesup(a,b)
#we can also take input from the user
a=int(input("enter 1st number"))
b=int(input("enter 2nd number"))
def hi(a,b):
    print("sum is ", a+b)
hi(a,b)
#we can also put variables to store data
def abhiskar(a,b):
    average=(a+b)/2#we have store (a+b)/2 in variable and print them
    print("this is your average no",average)
abhiskar(2,4)
# if we want to store any functions in variables then we have to write return and variable name 
def hero(a,b):
    average=(a+b)/2
    return average
v=hero(5,6)
print(v)
#Docstring is the line which is written for our own understanding that is written inside the functions
#Python docstrings are the string literals that appear right after the definition of a function, method, class, or module. Let's take an example.
def hero(a,b):
    """this is a fuction which will calculate average of the two numbers"""
    average=(a+b)/2
    return average
v=hero(5,6)
print(v)
''''
They are used to document our code.
We can access these docstrings using the .__doc__ attribute.
'''
#._doc_helps to see our docstrings code.we can print docstrings so that we can understand what the coder is writing about.
def square(n):
    '''Takes in a number n, returns the square of n'''
    return n**2
print(square.__doc__)



