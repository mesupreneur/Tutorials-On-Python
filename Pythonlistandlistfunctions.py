#list is a container to hold huge number,names(versatile datatype)
#containers to hold strings,integers
grocery=["Harpic","vim bar","icecream ","bindhi","lollypop",56,80]
print(grocery[0])#this print harpic
numbers1=[2,3,4,5,6]
print(numbers1[4]) #here we are accessing numbers
#TO MAKE LIST OPPOSITE
#We write list functions like
numbers1.sort()#arranging order
numbers1.reverse()
print(numbers1)
#it write (none)
print(numbers1.sort())
"""
slicing
"""
print(numbers1[0:5])
print(numbers1[1:5])#1 is include and 5 is exclude
"""
IF WE DO SLICING IT DOESNOT CHANGE THE ORIGINAL LIST BUT IF WE USE LIST FUNCTIONS THEN IT CHANGES 
THE ORIGINAL LIST
HERE ARE TWO VALUE OF Num but but if we use list function like .sort(),reverse() etc than it changes
original value
"""
Num=[56,20,70,50]
print(Num)
Num=[46,343,434]
print(Num)
#gap
print(numbers1[::2])#one step gapping between all numbers
print(numbers1[::-2])#one step gapping between all numbers and reverse the numbers
#if possible write only -1 but donot write other numbers
print(max(numbers1))
print(min(numbers1))
mesup=[24,57,"abhiskar",75]
mesup.append(4)#it helps to join anything at last
print(mesup)
mesup1=["mesup","hello",33]
mesup1.append("hllo")
mesup1.append("hllo")
mesup1.append("hllo")
mesup1.append("hllo")
print(mesup1)
hello=[]
hello.append("mesup")
hello.append("mesup")
hello.append("mesup")
print(hello)
"""so if we want to print anything in middle then we simply write insert(where to write,what to write"""
#for example
#insert function
hi=[24,42,44,23]
hi.insert(0,1)
hi.insert(1,"mesup")
#remove function helps help to remove anything from list
hi.remove(24)
print(hi)
#pop fuction (remove last thing from list)
he=[24,42,44,23]#this braket is knows as square braket
he.pop()
print(he)
#it removes 1 and comes 98(value changes)
he[1]=98
print(he)
"""if we donot want to change value in the list than we make tuple"""
#Mutable=can change(list)
#Immutable=cannot change(tuple)
#tuple
tp=(1,2,3,"me")#this braket is knows as parentheses
print(tp)
"""in tuple if we write tp[1]=8 than it shows error because here we cannot change the value"""
#to exchange the value between a and b there is traditional and modern method
#traditional method
a=1
b=8
c=a
a=b
b=c
print(a,b)
#modern method using python
a=1
b=8
a,b=b,a
print(a,b)


