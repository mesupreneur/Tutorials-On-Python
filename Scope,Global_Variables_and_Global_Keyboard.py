'''
There are two types of variables: global variables and local variables.
The scope of global variables is the entire program 
whereas the scope of local variable is limited to the function where it is defined.
'''

# Globalvariable 
'''Variables that are created outside of a function (as in all of the examples above) are known as global variables.
Global variables can be used by everyone, both inside of functions and outside.
'''
x = "awesome"
def myfunc():
  print("Python is " + x)
myfunc()
'''
If you create a variable with the same name inside a function,
this variable will be local, and can only be used inside the function. 
The global variable with the same name will remain as it was, global and with the original value.

'''
a = "awesome"
def myfunc():
  a = "fantastic"
  print("Python is " + a)
myfunc()
print("Python is " + a )


l=10#global variable
def function1(n):
    l=5#Local variable
    print(l)#it helps to print 5
    print(n,"I have printed")
function1("mesup")
print(l)#it helps to print 10
'''
if there is variable=(value) in global scope but inside the local scope,if there is no variable=(value)then it goes to global variables
for example 
'''
b=3
def mesup():
    l=5#local variable
    print(l,b)#there is no value of b in local scope so it takes the value of b from global scope
mesup()   
'''this shows an error beacuse l is in the local scope and it can only be applied inside the local scope'''
#print(l)
# we cannot change the global value in local scope but if we give access to local variable to use global variable
#if we want to give access then we simply write global and variable name 
# for example
#we write global keyboard before the variable which you want to give access
b=24
def mesup1():
    global b
    b=b+45
    print(l)
mesup1()

#nested function(function inside function)
x=55#if we also write this......
def hi():
    x=20
    def rohan():
        global x
        x=33
    print("before calling rohan()",x)
    rohan()
    print("after calling rohan()",x)
hi()
print(x)



