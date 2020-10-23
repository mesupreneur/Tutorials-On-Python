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
