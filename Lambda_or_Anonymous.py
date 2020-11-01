# lambda/Anonymous 
'''
A lambda function is a small anonymous function.
A lambda function can take any number of arguments, but can only have one expression.
'''
# simple method(not using lambda)
def mesup(a,b):
    return a+b
print(mesup(14,5))
# lambda function
'''
Syntax
lambda arguments : expression 
'''
using_lambda=lambda x,y:x+y
print(using_lambda(14,5)) 
# making list of list
# y component
def a_first(a):
    return a[1]#here a[1] looks the y value in the list
a=[[7,15],[2,8],[9,4]]
a.sort(key=a_first)
print(a)
# x component
def a_first(a):
    return a[0]#here a[1] looks x value in the list
a=[[7,15],[2,8],[9,4]]
a.sort(key=a_first)
print(a)
# making same thing using lambda function
a=[[7,15],[2,8],[9,4]]
a.sort(key=lambda a:a[0])#argument:expression
print(a)