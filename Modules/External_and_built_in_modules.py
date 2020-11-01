'''
What is a Module?
Consider a module to be the same as a code library.
A file containing a set of functions you want to include in your application.
'''
'''
Create a Module
To create a module just save the code you want in a file with the file extension .py:
'''
'''
Example
Save this code in a file named mymodule.py
def greeting(name):
  print("Hello, " + name)
'''
'''
Import the module named mymodule, and call the greeting function:
import mymodule
mymodule.greeting("Mesup")
'''
# built-in modules
import random#module
random_number=random.randint(1,5)#we can get any number between 1 to 5
print(random_number)
# random
mesup_number=random.random()#it print from 0 to 1
print(mesup_number)
# random upto 100
hi_number=random.random()*100#it helps to print from 0 to 100
print(hi_number)
# choice from list
list1=["python","node js","django","flask","facebook","instagram","java"]
mesup_love=random.choice(list1)
print("mesup love "+ mesup_love)
# some modules we have to install modules in terminal