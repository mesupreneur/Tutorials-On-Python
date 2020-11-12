'''
If you are familiar with any other object-oriented programming language, then the concept will be easy for you to grasp. 
So, let us begin with the Method.
'''
'''
A method is just like a function, with a def keyword and a single parameter in which the name of the object has to be passed. 
The purpose of the method is to show all the details related to the object in a single go. We choose variables that we want the method to take but do not have to pass all of them as parameters. Instead, we have to set the parameters we want to include in the method during its creation. Using methods make the process simpler and a lot faster. 

Self keyword:
The self keyword is used in the method to refer to the instance of the current class we are using. The self keyword is passed as a parameter explicitly every time we define a method.
__init__ method:-
"__init__" is also called as a constructor in object-oriented terminology. Whereas a constructor is defined as:

"Constructor in Python is used to assign values to the variables or data members of a class when an object is created."
Python treats the constructor differently as compared to C++ and Java. The constructor is a method with a def keyword and parameters, but the purpose of a constructor is to assign values to the instance variables of different objects. We can give the values by accessing each of the variables one by one, but in the case of the constructor, we pass all the values directly as parameters. Self keyword is used to assign value to a constructor too.  
As there can be only one constructor for a specific class, so the name of the constructor is a constant, i.e., __init__.
We declare a constructor in Python using def keyword,

'''
'''
The def keyword is used to define the function.
The first argument refers to the current object which binds the instance to the init() method.
In init() method ,arguments are optional. Constructors can be defined with any number of arguments or with no arguments.
'''
'''
Types of constructors in Python
We have two types of constructors in Python.

The default constructor is the one that does not take any arguments.
Constructor with parameters is known as parameterized constructor.
Method vs. Function:
Methods and functions are very similar, yet there are some differences:

Methods are explicitly for Object-Oriented programming.
The method can only be used by the object that it is called for. In simple terms, for a method, the parameter must be an object.
The method can only access the data that is initialized in the class the method is formed in. 
'''
class Employee():
    no_of_leaves=5#this is used for everyone
    # constructor using _init_
    def __init__(self,asalary,aname,arole):#making argument
       self.name=aname
       self.salary=asalary
       self.role=arole
    # method (we have to write self otherwise it shows an error)
    def printdetails(self):#here the self mean that object in which function works
        return f" His name is {self.name} and his salary is {self.salary}"
mesup_adhikari=Employee("Mesup",10000,"Instructor")
abhiskar_poudel=Employee("Abhiskar",20000,"Vice-Chairman")
divyan_thapa=Employee("Divyan",30000,"Chairman")
# instant variables
# mesup_adhikari=Employee()
# abhiskar_poudel=Employee()
# divyan_thapa=Employee()
# # putting the values in variables
# mesup_adhikari.name="Mesup"
# mesup_adhikari.salary=10000
# mesup_adhikari.role="Instructor"
# abhiskar_poudel.name="Abhiskar"
# abhiskar_poudel.salary=20000
# abhiskar_poudel.role="Vice Chairman"
# divyan_thapa.name="Divyan"
# divyan_thapa.salary=30000
# divyan_thapa.role="Chairman"
print(mesup_adhikari.salary)
print(mesup_adhikari.no_of_leaves)
print(divyan_thapa.no_of_leaves)#no of leaves is same for everyone
# to access no of leaves, we can also write class name 
print(Employee.no_of_leaves)
print(mesup_adhikari.printdetails())
print(abhiskar_poudel.printdetails())
print(divyan_thapa.printdetails())
# output
# His name is Mesup and his salary is 10000
# His name is Abhiskar and his salary is 20000
# His name is Divyan and his salary is 30000



