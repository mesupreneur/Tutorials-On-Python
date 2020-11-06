stay_motivated="import module"
print(f"get ready to write a code {stay_motivated}")
'''
When we write a certain module name along with the import keyword, it will start searching for a file with that name having an extension .py. After finding the file, it will import it into our program, which means 
that it will permit our program to use the functions of the certain module we imported.
We can import a module named “sys” to see the path that our import statement takes while searching for a module.
'''
import sys
print( sys.path)#path where it brings
# sys.path prints out a list of directories. When we tell Python to import something, then it looks in each of the listed locations in order. 
'''
A common mistake that most of the beginners make and
is also the primary reason for making this tutorial is, 
why can’t we name our file, the same as the name of a module.
The reason is associated with the path. When we give our file a name same as the name of a module, then instead of importing the original module, the system will import our created file because it starts its search for the file from the directory where the file we are working on exists.
So, we will not be able to use the functions of the original file.
'''
'''
There are two methods to use functions or variables after importing:
1st method
The first one is to import using an object. For this, 
we usually import the whole module by using a simple import statement.
When we use only the import keyword,we will import the resource directly, like this:
'''
import sklearn 
'''
2nd method
When we use the second syntax, we will import the resource from another package or module. Here is an example:
'''
# from f import sklearn
'''
We can also choose to rename an imported resource, like this:
This renames the imported resource sklearn to sk. 

We can not access it using sklearn keyword; instead, 
we have to use pd or the compiler will show an error.
This case comes in handy when the module name is difficult or lengthy, 
and we have to use a module again and again to call its functions.
'''
import sklearn as sk
# Note: import module as module_name does not rename the module originally but only for a specific program where it is imported using this sort of keyword.
'''
Disadvantages:
One of the major disadvantages of the flexibility provided by a python in the  of modules is that they can be easily modified and overridden. 
Along with disrupting the functionality of the program, case
it also poses a major security risk.
'''
# to get version
# 1st method
import sklearn 
print(sklearn.__version__)#it takes time
#2nd method 
import sklearn as sk
print(sk.__version__) 
#donot make a file with the name of module 

# if make a file with the name of module then it simply uses that file
# we have made file2 and imported it and access it
# 1st method
import file2#mostly prefer method
print(file2.a)
# 2nd method
from file2 import a
print(a)
# we have stored the function (printjoke) in file2 and we can import 
file2.printjoke("hahhahaha")#this helps to print this is a function is a joke hahahahah
#variables which are stored in program are int,float
