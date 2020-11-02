# f-string
# string formatting
hello_world="mesup"
conversation="hi,what going on %s"%hello_world
print(conversation)
me="mesup"
a1=3
a="this is %s %s"%(me,a1)
print(a)
# format
# The format() method formats the specified value(s) and insert them inside the string's placeholder.
'''

The placeholder is defined using curly brackets: {}. 
Read more about the placeholders in the Placeholder section below.
'''
'''
The format() method returns the formatted string.
'''
#named indexes:
txt1 = "My name is {fname}, I'm {age}".format(fname = "mesup", age = 15)
print(txt1)
# or we can also write like this 
txt2="My name is {name},I'm {age}"
b= txt2.format(name="mesup",age= 15)
print(b) 
# if we want to put the value which is stored in the variable then we simply write like this:
#empty placeholders:
hello="abhiskar"
a2=5
mesup="this is {} {}"
conversation1=mesup.format(hello,a2)
print(conversation1)
#numbered indexes:
txt2 = "My name is {0}, I'm {1}"#it helps to place the John in first and 36 in the second 
hi=txt2.format("John",36)
print(hi)
# if we want to format in opposite we simply write like this 
txt2 = "My name is {1}, I'm {0}"#it helps to place the 36 in first and John in the second 
hi=txt2.format("John",36)
print(hi)

# Option #1: %-formatting
'''
This is the OG of Python formatting and has been in the language since the very beginning.
You can read more in the Python docs. Keep in mind that %-formatting is not recommended by the docs, which contain the following note:'''
# Option #2: str.format()
'''
This newer way of getting the job done was introduced in Python 2.6.
You can check out the Python docs for more info.
'''
# option #3:f-string
'''
f-Strings: A New and Improved Way to Format Strings in Python#
'''
me="mesup"
a1=3
a=f"this is {me} {a1}"
print(a)
# we can also write any expression in f-string like 
best_friend="abhiskar"
a=f"{best_friend} roll no is {3+5}"#here we have also written expression
print(a)
# we can also import module and can use in f-string
import math
best_friend="abhiskar"
a=f"{best_friend} roll no is {math.cos(65)}"
print(a)
# f-string=full form
# fast

