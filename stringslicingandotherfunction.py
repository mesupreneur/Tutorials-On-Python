#string is datatype.(combination of characters)
mystr ="mesup is a good boy"
print(mystr)
print(type(mystr))
#in python always character(index) starts from 0 to .....
#some word to print from character
mystr ="hi mesup"
print(mystr[0])#this print h
print(mystr[1])#remember that it will print i beacuse always in python letter starts from zero
print(mystr[2])#remember that this will print nothing because in index 2 there is space.
print(mystr[3])#this print m
print(mystr[4])#this print e
print(mystr[5])#this print s
print(mystr[6])#this print u
print(mystr[7])#this print p
"""
this is string slicing
"""
#if we want to print some words than [0:...]then
slicing ="hello,how are you"
#remember that for eg: [0:5]
print(slicing[0:5])#remember that it include 0 but exclude(donot take)5
#so it will print upto 4 that is hello
"""there are many functions"""
#len
slicing ="hello,how are you"
print(len(slicing))
"""
if we write print(slicing[78])then itn shows error because there are less than 78 but 
if we write print(slicing[0:78]) then it print full how much it is written it doesnot shows error
"""
print(slicing[0:78])
#if we want to print words putting gap gap then
print(slicing[0:5:2])#remember that it will print hlo only because we are using :2] that makes gap
"""if we print (slicing[0:]) or (slicing[:]) than it takes all character automatically"""
print(slicing[0:])
print(slicing[:])
"""if we print (slicing[:5])than in include it takes automatically 0"""
print(slicing[:5])
"""if we donot write anything print(slicing[::]) it takes gap 1 automatically but there is no gap 
beacuse there the character start from zero
"""
"""print(slicing[::])
print(slicing[0:no of character:1]) by default"""
slicing ="hello,how are you"
print(slicing[::])
print(slicing[0:17:1])
"""how much gap we want than we sould write one more than that no
for example we want to gap 2 step than we write 3 there
like print(slicing[0:17:3])
if we write many no than it will reslove how much it can
print(slicing[0:17:9249289474972])
"""
"""negative index"""
hello="mesup is a good boy"#its result space b
print(hello[-4:-2])
print(hello[15:17])
"""making string opposite"""
print(hello[::-1])#if there will be - than it makes opposite
"""functions
"""
#isalnum() or (there is no space)
print(hello.isnumeric())#boolen true or false
#if there spaces than it is also not alphanumeric
#isalpha() or (there is numerical and alphabet but no numerical
print(hello.isalpha())#false because there is space
#endswith("anything string")
print(hello.endswith("boy"))#it is true because sentence is ended by boy
#to count how many letters are there in sentence
"""for example hello.counts("b") than there are 1 b in  hello string
"""
print(hello.count("b"))
"""to capitalize first letter we write capitalize()"""
print(hello.capitalize())
"""to find any words than you can simply write find("words to find") it tell on which length it is"""
print(hello.find("is"))#ans 6.
"""if we want to capitalize all letters in sentences than we simply write upper()and
to lower all letters in sentences than we simply write lower()
"""
print(hello.lower())
print(hello.upper())
"""
if we want to replace anything to any word than we write replace("word to replace,word to put now") 
"""
"""
if we want to replace is with are than we simply write print(hello.replace("is","are"))
"""
print(hello.replace("is","are"))