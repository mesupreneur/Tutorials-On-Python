#A Set is an unordered collection data type that is iterable, mutable and has no duplicate elements
#sets can be written as 
s=set({})
print(type(s))
#or we can write set as
a={"apple","banana","juice"}#but if we write {}braket with empty value then it is dictionary{}
print(type(a))
#we can also make list as set and print 
list=[1,2,3,4,5,6]
a1=set(list)
print(a1)
#set always print in {} brakets
"""
we can add anything in set but it do not print same type of element(only one),(unique value)
"""
a2=set({3,4})
a2.add(1)
print(a2)
#we can also write 
a3=set()
a3.add(34)
b=a3.union({1,2,3,4})
print(a3,b)
#intersection
a3=set()
a3.add(1)
b=a3.intersection({1,2,3,4})
print(a3,b)
#maximum,minumum
print(max(b))
#disjoint
"""
Disjoint--------------
Two sets are said to be disjoint if they do not have any common elements. For example Set {1, 2, 3} and Set {4, 5, 6} are disjoint sets because they do not have any common elements.

"""
s4=set({7,8,9})#they are not common so they are disjoint(true)
s5=set({1,2,3})
print(s4.isdisjoint(s5))
#to remove element
s9=set({2,3,5,7})
s9.remove(2)
print(s9)
[Chapter 1 - Practice set.pdf](https://github.com/iammesup/TUTORIALS-ON-PYTHON/files/5557819/Chapter.1.-.Practice.set.pdf)
