'''
Using if __name__ == “__main__” statement is one such concept that may be difficult to grasp for beginners, but once learned, it is very helpful and used quite often afterward. However, it may seem confusing at times. This article aims to provide an understanding of the behavior of the statement and further discusses how to use it. As discussed earlier, a module is just a file containing a python code with a .py extension and can be imported to other files. That's where the keyword __name__ comes
Let’s understand __name__ first before moving onto if __name__ == “__main__.
What is __name__?
“A __name__ is a built-in variable that returns us the name of the module being used.”

In simple words, by using __name__, we can check whether our module is being imported or run directly.

'''
# if we return then we should print while calling function
def mesup(string):
    return f"ye string mesup ko de de thakur{string}"
def add(num1,num2):
    return num1+num2+5
    # if we want to write if __name__ == "__main__": we simply write main and enter
print("__name in tutmain2.py is set to"+__name__)#name value comes name if we are using the same file but name value comes file name then it was imported.
if __name__ == "__main__":
    print(mesup("mesup1"))#here after if __name__ == "__main__": it will not be executed in other file if we import.
    hello=add(4,5)
    print(hello)
'''
What are the Advantages of using if __name__ == “__main__” statement?
Following are the advantages of using if __name__ == “__main__” statement:

Using the main in our file, we can restrict some data from exporting to other files when imported.
We can restrict the unnecessary data, thus making the output cleaner and more readable.
We can choose what others may import or what they may not while using our module.
 To summarise the concepts discussed in this tutorial, Modules in Python has a special attribute called __name__. The value of the __name__ attribute is set to __main__ when the module is run as the main program. Otherwise, the value of __name__ is set to the name of the module. The if __name__ == “__main__” block prevents the certain code from being run when the module is imported.
'''



'''