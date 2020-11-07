'''
Python's map() is a built-in function that allows you to process and transform all the items in an iterable without using an explicit for loop, a technique commonly known as mapping.
map() is useful when you need to apply a transformation function to each item in an iterable and transform them into a new iterable.
'''
# The map() function executes a specified function for each item in an iterable. The item is sent to the function as a parameter.
# syntax
# map(function, iterables)
'''
Parameter	Description
function	Required. The function to execute for each item
iterable	Required. A sequence, collection or an iterator object. You can send as many iterables as you like, just make sure the function has one parameter for each iterable.

'''
'''
Python provides many built-in functions that are predefined and can be used by the programmers by just calling them. These functions not only ease our work but also create a standard coding environment. In this tutorial, 
we will learn about three important functions: map(), filter, and reduce() in Python. These functions are most commonly used with Lambda function. "Lambda functions are functions that do have any name".
These functions are used as parameters to other functions. If you do not know what lambda functions are, then I recommend you to check Anonymous/Lambda Functions In Python  tutorial first to avoid any confusion.
'''
'''
Why are lambdas relevant to map(), filter() and reduce()?
These three methods expect a function object as the first argument. 
This function object can be a normal or predefined function. Most of the time,
functions passed to map(), filter(), and reduce() are the ones we only use once,
so there's often no point in defining a named function(def function).To avoid defining a new function, we write an anonymous function/lambda function that we will only use once and never again.

'''
'''
map():
"A map function executes certain instructions or functionality provided to it on every item of an iterable."
The iterable could be a list, tuple, set, etc. It is worth noting that the output in the case of the map is also an iterable i.e., a list.
It is a built-in function, so no import statement required.

'''
'''
A map function takes two parameters:
First one is the function through which we want to pass the items/values of the iterable
The second one is the iterable itself
'''
# method without using map
number=["34","44","56","90"]#this is a string 
# to make in integer
for i in range(len(number)):
    number[i]=int(number[i])
number[2]=number[2]+1
print(number[2])
# method using map makes easier in one line code.
# map and we write the function which apply to all the object in the list
# ---------------------------------map()------------------------------------------#
numbers=["44","32","78","12"]
numbers=list(map(int,numbers))
numbers[2]=numbers[2]+1
print(numbers[2])
# making it into tuple
numbers=["44","32","78","12"]
numbers=tuple(map(int,numbers))
print(numbers[2])
# map() function returns a map object(which is an iterator) of the results after applying the given function to each item of a given iterable (list, tuple etc.)
# map(fun, iter)
# fun : It is a function to which map passes each element of given iterable.
# iter : It is a iterable which is to be mapped.
def addition(n): 
    return n + n 
# We double all numbers using map() 
numbers = (1, 2, 3, 4) 
result = map(addition, numbers) 
print(set(result))
# print(list(result)) we can also transform it into the list,tuple,set
# inside map we have to use function and instead we can also use lambda function
# function without using lambda
def sq(a):
    return a*a
num=[23,4,5,6,7,8]
square=list(map(sq,num))
print(square)
# function using lambda
# def sq(a):
#     return a*a
num=[23,4,5,6,7,8]
square=list(map(lambda a:a*a,num))
print(square)
# function
def square(a):
    return a*a
def cube(a):
    return a*a*a
fun=[square,cube]
for i in range(5):#0,1,2,3,4
    # print(i)
    val=list(map(lambda a:a(i),fun))
    print(val)
# 0*0=0  0*0*0=0
# 1*1=1  1*1*1=1
# 2*2=4  2*2*2 =8
# 3*3=9  3*3*3=27
# 4*4=16 4*4*4=64
# -------------------------------filter()---------------------------------------------#
'''
"A filter function in Python tests a specific user-defined condition for a function and returns an iterable for the elements and values that satisfy the condition or, in other words, return true."
'''
'''
It is also a built-in function, so no need for an import statement.
All the actions we perform using the filter can also be performed by using a for loop for iteration and if-else statements to check the conditions. We can also use a Boolean that could take note of true or false, but that would make the process very lengthy and complex.
So, to simplify the code, we can use the filter function.
'''
'''
It also takes two parameters:

First one is the function for which the condition should satisfy
The second one is the iterable
'''
# syntax
# filter(function, iterable)
list1=[1,3,54,56,67]
def is_greater_5(num):
    return num>5
greaterno=list(filter(is_greater_5,list1))#it helps to filter the number according to the condition...
print(greaterno)
#----------------------------------------Reduce---------------------------------------#
'''
"Reduce functions apply a function to every item of an iterable and gives back a single value as a resultant".
'''
# Unlike the previous two functions (Filter and Map), we have to import the reduce function from functools module using the statement:
'''
from functools import reduce
We can also import the whole functools module by simply writing
Import functools
But in the case of bigger projects, it is not good practice to import a whole module because of time restraint.
'''
# syntax
# reduce(function, iterable)
# without using return
list3=[1,2,3,4]#if we want to join the value and return
# 1+2+3+4=10
num=0
for i in list3:
    num=num+ i
print(num)
# using return function
from functools import reduce#we have to import reduce
list2=[1,2,3,4]
num=reduce(lambda x,y:x+y,list2)
print(num)
# 

a=reduce( (lambda x, y: x * y), [1, 2, 3, 4] )
print(a) 
#Output: 24