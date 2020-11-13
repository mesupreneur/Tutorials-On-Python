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
mesup_adhikari=Employee("Mesup",10000,"Instructor")
abhiskar_poudel=Employee("Abhiskar",20000,"Vice-Chairman")
divyan_thapa=Employee.fromstr("Divyan-30000-Chairman")
print(Employee.no_of_leaves)
print(divyan_thapa.name)
# before changing value 
# print(mesup_adhikari.no_of_leaves)
# # if we change the templete by writing class name 
# Employee.no_of_leaves=89
# after changing the main class value
mesup_adhikari.change_leaves(89)
print(mesup_adhikari.no_of_leaves)
# we can also change the value of class 
Employee.change_leaves(89)





