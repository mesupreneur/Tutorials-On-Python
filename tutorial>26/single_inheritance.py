'''
In today’s tutorial, we are going to learn about Single inheritance in Python. 
Before discussing the concept of inheritance in Python, we should have some knowledge about the word itself. 
Inheritance means to receive something as an heir from one's parents or ancestors. The concept of inheritance is very similar in cases of classes where a class inherits all the properties and methods of its previous class that it is inheriting from.

"Inheritance is the ability to define a new class(child class) that is a modified version of an existing class(parent class)"
'''
'''
# syntax
class Parent_class_Name:
#Parent_class code block
class Child_class_Name(Parent_class_name):
#Child_class code block
'''
# The above syntax consists of two classes declared. One is the parent class or by other means, the base class, 
# and the other one is the child class which acts as the derived class.
'''
Two common terms related to inheritance are as follows:
Parent: The parent class is the one that is giving access to its methods or properties to the child class or derived class.
Child: Child class is the one that is inheriting methods and properties from the parent class.
The class that is inheriting i.e. the child class not only can inherit all the functionality of the parent class but can also add its functionalities too. 
As we have already discussed that each class can have its constructors and methods, so in case of inheritance the child class can make and use its constructor and also can use the constructor of the parent class. 
We can simply construct it as we did for the parent class but OOP has provided us with a simple and more useful solution known as Super().

We will be discussing super() and overriding in our Super() and Overriding In Classes tutorial of the course.


 
Single inheritance exists when a class is only derived from a single base class. Or in other words when a child class is using the methods and properties of only a single parent class then single inheritance exists. 
Single inheritance and Multiple inheritance are very similar concepts, the only major difference is the number of classes. We will see Multiple Inheritance in our next tutorial.

Different forms of Inheritance:
Single inheritance: When a child class inherits from only one parent class then it is called single inheritance.
Multiple inheritance: When a child class inherits from multiple parent classes then it is called multiple inheritance
Below is an example of single inheritance in python.

class Parent():
    def first(self):
        print('Parent function')
        
class Child(Parent):
    def second(self):
        print('Child function')

object1 = Child()
object1.first()
object1.second()
Output: 

Parent function

Child function

Advantages of inheritance:
It promotes code’s reusability as we do not have to copy the same code again to our new class.
It makes the program more efficient.
We can add more features to our already built class without modifying it or changing its functionality.
It provides a representation of real-world relationships.
In this tutorial, we have discussed the Inheritance concept. 
Inheritance is among the most significant concepts in object-oriented programming technique which provides code reusability, readability and helps in building optimized and efficient code.
'''
# inheritance means same copy of the class and adding to the class
# single inheritance
# no need to repeat the code if we use inheritance method

# one class inherit with one class
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
class Programmer(Employee):#this is not the right way to add something in constructor(we have to use super() in next tutorial,we will learn)
    def __init__(self,aname,asalary,arole,languages):#making argument
       self.name=aname
       self.salary=asalary
       self.role=arole
       self.languages=languages
    def printprog(self):
        return f" name is {self.name} and salary is {self.salary} and he is {self.role} and languages that he know are {self.languages}"
mesup_adhikari=Employee("Mesup",10000,"Instructor")
abhiskar_poudel=Employee("Abhiskar",20000,"Vice-Chairman")
divyan_thapa=Employee.fromstr("Divyan-30000-Chairman")
# print(Employee.no_of_leaves)
# print(divyan_thapa.name)
# abhiskar_poudel.printgood("abhiskar")
# # we can also access it by writing class name 
# Employee.printgood("abhiskar")
subham=Programmer("Subham",50000,"Programmer",["python"])
karan=Programmer("Karan",40000,"Programmer",["python","Django","Flask"])
print(karan.printprog())
print(karan.printdetails())
