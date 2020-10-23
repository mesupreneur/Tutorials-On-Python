#A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).
#to print we write 
a=["mesup","abhiskar","divyan","hero"]
print(a)
#we can also print by using loop 
list1=["mesup","abhiskar","divyan"]
for item in list1:
    print(item)
#output
"""
mesup
abhikar
divyan
"""
#it also can be tuple
list1=("mesup","abhiskar","divyan")
for item in list1:
    print(item)
#list inside list
list3=[["mesup",1],["abhiskar",2],["divayan",2]]
for item in list3:
    print(item)
#but we can print like this 
for item,roll_no in list3:
    print(item,"roll no is",roll_no)
#dictionary
dict1=dict(list3)#typecasting list to dictionary
print(dict1)
#to use loop in dictionary we use dict.items()
list4=[["mesup",6],["abhsikar",8],["happy",9]]
dict3=dict(list4)
for items,lolly in dict3.items():
    print(items,"roll no is",lolly)
#if we want only the keys of dictionary then we can write 
for items in dict3:
    print(items)
#if we want to print the letters in words then we simply write
for x in "banana":
  print(x)
#to print the no upto (what you write)
for x in range(6):
  print(x)
"""
output is 
0
1
2
3
4
5
"""
#if we want to print the no inside(,)
for x in range(2, 6):
  print(x)
"""
output is 
3
4
5
"""
#if we want gap between no then we simply print(starting no,ending no,gap no)
for x in range(2, 30, 3):
  print(x)
"""
output is 
2
5
8
11
14
17
20
23
26
29
"""
#Print all numbers from 0 to 5, and print a message when the loop has ended:
for x in range(6):
  print(x)
else:
  print("Finally finished!") 
#Print each adjective for every fruit:
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]
for x in adj:
  for y in fruits:
    print(x, y) 
#for loops cannot be empty, but if you for some reason have a for loop with no content, put in the pass statement to avoid getting an error.
#having an empty for loop like this, would raise an error without the pass statement
for x in [0, 1, 2]:
  pass

