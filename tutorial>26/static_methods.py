'''
Static method. It is one of the important concepts to use while you are learning OOPs programming with Python. A static method is very much easy to understand if we are familiar with class methods. 
It is also easier to implement than a class method because it can be accessed without any object. 
However, we can also access it using a class or any instance.
'''
'''
Static Method in Python:
We know that a static method in Python is treated differently than in other languages. Static methods in Python are extremely similar to python class methods, but the difference is that 
a static method is bound to a class rather than the objects for that class.
To define a static method, we use @staticmethod decorator, 
which is a built-in decorator. Also, there is no need to import any module to use decorators. Using a static method in a class, we permit it to be accessed only by the class objects or inside the class.
'''
'''
There are few limitations related to static methods, such as:

Unlike, class method a static method cannot alter or change any variable value or state of the class.
Static methods do not have any knowledge related to class

Static methods do not require any knowledge related to the class that they are built-in. 
They are only formed in a class so that only the class instances can access them. We can use a static method for simple functionality that is mostly not related to the class. 
For example, we want to add two numbers together, but we do not want our method to be used elsewhere, other than the class, or through its instances, so we will create a static method. 
It will not require any information related to class as it only requires the numbers it has to add, but it will still fulfill its purpose as it is like a personal method that only the class has access to.
Most of the functionalities of the static methods can be performed using a class method. However, we prefer the static method, at places where it could work to make our program more efficient and faster as we do not have to pass self as a parameter, so the efficiency of the program increases.
In Python static methods can be created using @staticmethod.   
Using @staticmethod annotation is actually a better way to create a static method in Python as the intention of keeping the method static is clear.

Advantages of Python static method
Static methods have a very clear use-case. When we need some functionality not for an Object but with the complete class, we make a method static. This is advantageous when we need to create utility methods.
Finally, note that in a static method, we do not need the self or cls to be passed as the first argument
'''
'''
In this tutorial, we will learn how we can convert a class method into an alternating constructor. 
This tutorial is not about "what," as we have seen in previous tutorials, where we learn about new concepts or functionality. 
But this one is about" how." 
We will focus more on implementation as we are already familiar with all the concepts we are going to use. In this tutorial, we are going to learn some new skills or techniques other than a new concept.
We learned about constructor and its functionality, where we had to set all the values as parameters to a constructor. Now we will learn how to use a method as a constructor. It has its own advantages. By using a method as a constructor, we would be able to pass the values to it using a string.
Note that we are talking about a class method, not a static method.
The parameters that we have to pass to our constructor would be the class i.e., cls and the string containing the parameters. Moving on towards the working, we have to use a function "split()," that will divide the string into parts. And the parts as results will be stored in a list. 
We can now pass the parameters to the constructor using the index numbers of the list or by the concept of *args (discussed in tutorial#43 ).
'''
'''
split():
Let us have a brief overview of the split() function. 
What split() does is, it takes a separator as a parameter. 
If we do not provide any, then the default separator is any whitespace it encounters. 
Else we can provide any separator to it such as full stop, hash, dash, colon, etc. 
After separating the string into parts, the split() function, 
stores it into a list in a sequence. For example:
'''
class Employee():
    no_of_leaves=5#this is used for everyone
    # constructor using _init_
    def __init__(self,aname,asalary,arole):#making argument
       self.name=aname
       self.salary=asalary
       self.role=arole
    # method (we have to write self otherwise it shows an error)
    def printdetails(self):#here the self mean that object in which function works
        return f" His name is {self.name} and his salary is {self.salary}"
    @classmethod
    def change_leaves(cls,newleaves):
        cls.no_of_leaves=newleaves
    @classmethod
    def fromstr(cls,string):#here cls means employee
        # seperate=string.split("-")
        # # print(seperate)output-----['Divyan', '30000', 'Chairman']
        # return cls(seperate[0],seperate[1],seperate[2])
        return cls(*string.split("-"))
    # this function neither take self  or cls as an argument but works for it only then we use static method(inside class)
    @staticmethod
    def printgood(string):
        print(f"this is good {string}")
mesup_adhikari=Employee("Mesup",10000,"Instructor")
abhiskar_poudel=Employee("Abhiskar",20000,"Vice-Chairman")
divyan_thapa=Employee.fromstr("Divyan-30000-Chairman")
print(Employee.no_of_leaves)
print(divyan_thapa.name)
abhiskar_poudel.printgood("abhiskar")
# we can also access it by writing class name 
Employee.printgood("abhiskar")



