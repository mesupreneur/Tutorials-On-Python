var2=56
#i have taken input as string and typecasting it to integer
var3=int(input())
if var3>var2:#colon means we want to go inside it
    print("greater")
if var3==var2:
    print("equal")#always remember that in python equal to is written as (==) 
else:
    print("smaller")    
#in print we have given spaces that is called indentation
"""
Indentation refers to the spaces at the beginning of a code line. Where in other programming languages the indentation in code is for readability only, the indentation in Python is very important. Python uses indentation to indicate a block of code.
""" 
#IF WE USE if THEN PYTHON IT CHECKS ALL THE LINE LINE BY LINE ALSO AFTER THE CONDITION GET SATISFIED
"""BUT IF WE USE elif THAN IT CHECKS THE LINE AND 
IF THE CONDITION GETS SATISFIED THEN DIRECTLY 
PRINT THE OUTPUT RATHER THAN CHECKING OTHER LINES (ITS HEPLS TO MAKE THE PROGRAM FAST)"""
#FOR EXAMPLE:
var2=56
var3=int(input())
if var3>var2:#colon means we want to go inside it
    print("greater")
elif var3==var2:#HERE WE USE elif
    print("equal")#always remember that in python equal to is written as (==) 
else:
    print("smaller") 
#if (anything) in (list variable)
list1=[1,2,3,4,5]
if 5 in list1:#if 5 is in the list or not
     print("yes,it is in the list")
#if we want to see true or false
#either it is in list or not
list2=[2,4,6,7]
print(2 in list2)#it says true because 2 is in the list
print(5 in list2)#it says false because 5 is not in list
#not in list
list5=[1,2,3,4,5]
if 5 not in list1:#it says false beacuse 5 is in the list if there was no 5 then it print no,it is in the list
     print("no,it is in the list")
#not in list either true or false
list7=[2,4,6,7]
print(4 not in list7)#it says false because 4 is in the list



