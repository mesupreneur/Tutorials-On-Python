

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
    @classmethod
    def change_leaves(cls,newleaves):
        cls.no_of_leaves=newleaves
mesup_adhikari=Employee("Mesup",10000,"Instructor")
abhiskar_poudel=Employee("Abhiskar",20000,"Vice-Chairman")
divyan_thapa=Employee("Divyan",30000,"Chairman")
print(Employee.no_of_leaves)
# before changing value 
# print(mesup_adhikari.no_of_leaves)
# # if we change the templete by writing class name 
# Employee.no_of_leaves=89
# after changing the main class value
mesup_adhikari.change_leaves(89)
print(mesup_adhikari.no_of_leaves)
# we can also change the value of class 
Employee.change_leaves(89)
