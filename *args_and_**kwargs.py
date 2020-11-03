# *args and **kwargs
# this function takes the argument(marks of the students) and print the argument
'''
Special Symbols Used for passing arguments:-

1.)*args (Non-Keyword Arguments)

2.)**kwargs (Keyword Arguments)
'''
'''
1.) *args

The special syntax *args in function definitions in python is used to pass a variable number of arguments to a function. 
It is used to pass a non-key worded, variable-length argument list. 

'''
def function_name_print(a,b,c,d):
    print(a,b,c,d)
function_name_print("mesup","rohan","bhisworaj","abhiskar")
# if we want to add any name then we write e but it is not the proper way
def function_name_print(a,b,c,d,e):
    print(a,b,c,d,e)#if we add e but this is not the proper way to add (in big projects)
function_name_print("mesup","rohan","bhisworaj","abhiskar","happy")
# method using args
# always remember that whether the value is in the list or tuple it pass the value as the tuple
def mesup(*hi):
    print(type(hi))
    print(hi)
list1=["mesup","harry","rohan","bhiswas"]
mesup(*list1)
# using for loop it helps to print one by one
def mesup(*hi):
    for item in hi:
       print(item)
list1=["mesup","harry","rohan","bhiswas"]
mesup(*list1)
# without args if we use normal argument then it print in the list[""]
def mesup(hi):
    print(hi)
list1=["mesup","harry","rohan","bhiswas"]
mesup(list1)
# we an also use normal argument with args but normal must be in the first and *args and then *kwargs
def mesup(normal,*hi):
    print(normal)
    print(hi)
list1=["mesup","harry","rohan","bhiswas"]
normal="hi bro"#here we can also write integer
mesup(normal,*list1)
# args and kwargs are optional
'''
The special syntax **kwargs in function definitions in python is used to pass a keyworded, variable-length argument list. We use the name kwargs with the double star. ...
A keyword argument is where you provide a name to the variable as you pass it into the function.
'''
'''
difference between 
*args passes variable number of non-keyworded arguments list and on which operation of the list can be performed.
**kwargs passes variable number of keyword arguments dictionary to function on which operation of a dictionary can be performed. 
'''
#kwargs
def mesup(**hi):
    for key,value in hi.items():
       print(f"{key} is a {value}")
dict1={"mesup":"man","harry":"programmer","rohan":"student","bhiswas":"bike rider"}
mesup(**dict1)

