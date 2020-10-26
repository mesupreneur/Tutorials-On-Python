''''
 try block lets you test a block of code for errors.
The except block lets you handle the error.
The finally block lets you execute code, regardless of the result of the try- and except blocks.
'''
'''
Exception Handling
When an error occurs, or exception as we call it, Python will normally stop and generate an error message.
These exceptions can be handled using the try statement:'''
#if we write string then it shows error in the program because the input is integer 
#but sometime it is very important to show something after program
#here we want to print something in the last of the program then we use try except exception handling in python.
try:
   num1=(input("enter 1st number"))
   num2=(input("enter 2nd number"))
   print("the sum of these numbers is ",int(num1)+int(num2))
except Exception as e:
    print(e)
print("this line is very important")
