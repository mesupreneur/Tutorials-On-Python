'''
Python has an interesting feature called decorators to add functionality to an existing code.
This is also called metaprogramming because a part of the program tries to modify another part of the program at compile time.
'''
'''
Prerequisites for learning decorators
In order to understand about decorators, we must first know a few basic things in Python.

We must be comfortable with the fact that everything in Python (Yes! Even classes), are objects. Names that we define are simply identifiers bound to these objects. Functions are no exceptions, they are objects too (with attributes).
Various different names can be bound to the same function object.

'''
'''
Last Updated: 10-11-2018
In Python, functions are the first class objects, which means that –
Functions are objects; they can be referenced to, passed to a variable and returned from other functions as well.
Functions can be defined inside another function and can also be passed as argument to another function.
'''
'''
Decorators are very powerful and useful tool in Python since it allows programmers to modify the behavior of function or class. Decorators allow us to wrap another function in order to extend the behavior of wrapped function, without permanently modifying it.
In Decorators, functions are taken as the argument into another function and then called inside the wrapper function.
'''
# syntax for decorators
# @gfg_decorator
# def hello_decorator(): 
# 	print("Gfg") 

'''Above code is equivalent to - 

def hello_decorator(): 
	print("Gfg") 
	
hello_decorator = gfg_decorator(hello_decorator)'''
# function
'''
Functions in Python can be defined as lines of codes that are built to create a specific task and can be used again and again in a program when called.
'''
# decorators
''''
What is Python Decorator?
Decorator as can be noticed by the name is like a designer that helps to modify a function. The decorator can be said as a modification to the external layer of function, as it does not make any change in its structure. What a decorator does is, it takes a function and insert some new functionality in it without changing the function itself. A reference to a function is passed to a decorator and the decorator returns a modified function. The modified functions usually contain calls to the original function. This is also known as metaprogramming because a part of the program tries to modify and add functionality into another part of the program at compile time. Understanding the definition could be difficult but we can grasp the concept easily through the example in the video section.
In terms of python, the other function is also called a wrapper.
'''
# wrapper
'''
A wrapper is a function that provides a wrap-around another function. 
While using decorator all the code that is executed before our function that we passed as a parameter and also the code after it is executed belongs to the wrapper function. The purpose of the wrapper function is to assist us. Like if we are dealing with a number of similar statements, the wrapper can provide us with some code that all the functions have in common and we can use a decorator to call our function along with wrapper. 
A function can be decorated many times. 
'''
# Note that a decorator is called before defining a function.
'''
Advantages:
• Decorator function can make our work compact because we can pass all the functions to a decorator that requires the same sort of code that the wrapper provides.
• We can get our work done, without any alteration in the original code of our function.
• We can apply multiple decorators to a single function.
• We can use decorators in authorization in Python frameworks such as Flask and Django, Logging and measuring execution time.
'''
def function1():
    print("hello my name is mesup")
func2=function1
func2()
#it adds the value but donot change or delect
# trying to delect but it donot delect
def function2():
    print("hello my name is mesup")
func3=function2
del function2
func3()
# using function we can also define function
def funcret(num):
    if num==0:
        return print #built-in function
    if num==1:
        return int #class int
a=funcret(0)
print(a)
a=funcret(1)
print(a)
# 
def mesup(func1):
    func1("hello")
mesup(print)
# first method
def hello(func1):
    def hi():
        print("before executing hello")
        func1()
        print("after executing hello")
    return hi
def who_is_mesup():
    print("mesup is a good boy")
who_is_mesup= hello(who_is_mesup)#first method to write decorators 
who_is_mesup()
# 
# second method using @
def done(kacha):
    def hellobye():
        print("before executing done")
        kacha()
        print("after executing done")
    return hellobye
@done
def who_is_hi():
    print("mesup is a good boy")
who_is_hi()







