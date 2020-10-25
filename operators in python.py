#operators in python
"""
Arithmetic Operators
Assignment Operators
Comparison Operators
Logical Operators
Identity Operators
Membership Operators
Bitwise Operators
"""
#Arithmetic Operators
print("5 + 6 is ",5+6)#addiction(11)
print("5 - 6 is ",5-6)#subtraction(-1)
print("5 * 6 is ",5*6)#multiplication(30)
print("5 / 6 is ",5/6)#division(0.8333333333333334)
print("5 % 6 is ",5%6)#modulus(5)remainder
print("5 ** 6 is ",5**6)#exponentiation(15625)5*5*5*5*5*5
print("5 // 6 is ",5//6)#floor division(0)

#Assignment Operators
x = 5#here = is assignment operator
print(x)
#here += is assignment operator
x=5
x-=5#here x-=5 is also written as x=x-5
print(x)
#using multication
x = 5
x *= 3
print(x)
#using subtaction
x = 5
x -= 3
print(x)
#using division
x = 5
x /= 3
print(x)
#using modulus
x= 5
x%=3
print(x)
#using exponentiation
x = 5
x**=3
print(x)
#using floor division
x = 5
x//=3
print(x)
#& uses
x = 5
x &= 3
print(x)
#| uses
x = 5
x |= 3
print(x)
#^ uses
x = 5
x ^= 3
print(x)
#>> uses
x = 5
x >>= 3
print(x)
#<< uses
x = 5
x <<= 3
print(x)
#Comparison Operators
i=5
print(i==5)#(True)
print(i!=5)#i is not equal to 5(False)
print(i<5)#(False)
print(i>5)#(False)
print(i<=5)#(True)
print(i>=5)#(True)
print(i and 5)#(5)

"""
Logical Operators
"""
"""
and operator
"""
a=True
b=False
print(a and b)#here it returns false bacause to return true all the condition must be true 
"""
or operator
"""
a=True
b=False
print(a or  b)#here it returns true beacuse any one of them is true then it returns true
"""
Identity Operators
"""
#(is) and (is not)
a=True
b=False
print(a is b)#it returns false because a is not b (true is not false)
a=True
b=False
print(a is not b)#it returns true beacuse a is not b
print(5 is not 7)#true 
"""
Membership Operators

"""
#(in) and (not in)
list1=[1,3,4,5,6]
print(2 in list1)#it returns true
print(344  not in list1)#it returns true
"""
Bitwise Operators
0 or 1
"""
"""
0-00
1-01
2-10
3-11
"""
#and 
print(0 and 1)#it print 0
print(0 & 1)
#or 
print(0 | 1)# for or we use |(it print 1)
print(0 | 3)#(it print 3)