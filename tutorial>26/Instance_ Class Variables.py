'''we learned about the object and their working with variables in detail.
Where we created a class Student. We also created its two objects (harry and larry) and also 
a few of their instance variables as well.'''
'''
When working with objects in Python, there are two types of variables we have to work with i.e. 
instance variables and class variables. But what do these types of variables mean, and how do they work? 
OOP allows the variables to be used at the class level or the instance level. 
In this tutorial, we are going to learn about the two different kinds of variables associated with a class and the difference between them. 
The variables are:

1)Instance variable
2)Class variable
'''
'''
Instance variable:
"Instance variable are the variables for which the value of the variable is different for every instance."
We can also say that the value is different for every object that we create.
Let us dive into some in-depth explanation. 
When we create a class, we define a few variables along with it. 
For example, we have created a class of Students, and we have defined a variable age. 
All the students cannot have the same age in a class, so we have assigned the variable an average age of 16. 
Now, whenever we use an object to print the value of age, it will show 16. 
We can try to change the value of age, but it will create a new instance variable for the specific object that we are updating it for, hence defining the value to it.
'''
'''
Class variable:
"Class attributes are owned by the class directly, which means that they are not tied to any object or instance."
Same as in the above example, if we want to change the age for every instance from 16 to 17, 
then we can do it by using the class variable, which in this case is Student. 

'''
'''
if we want that templete that can be used for everyone than we can write inside class
if we want diffent for all then we make different variable for each.(means his/her data is his/her property and it cannot be used for others)
'''
class Employee():
    no_of_leaves=5#this is used for everyone
    pass #here we can also put the templete 
# instant variables
mesup_adhikari=Employee()
abhiskar_poudel=Employee()
divyan_thapa=Employee()
# putting the values in variables
mesup_adhikari.name="Mesup"
mesup_adhikari.salary=10000
mesup_adhikari.role="Instructor"
abhiskar_poudel.name="Abhiskar"
abhiskar_poudel.salary=20000
abhiskar_poudel.role="Vice Chairman"
divyan_thapa.name="Divyan"
divyan_thapa.salary=30000
divyan_thapa.role="Chairman"
print(mesup_adhikari.salary)
print(mesup_adhikari.no_of_leaves)
print(divyan_thapa.no_of_leaves)#no of leaves is same for everyone
# to access no of leaves, we can also write class name 
print(Employee.no_of_leaves)
# we can change the value of all the data ithen we can do by writting class name
Employee.no_of_leaves=9#for all data that uses this class templete value changes to 9
print(mesup_adhikari.no_of_leaves)
print(divyan_thapa.no_of_leaves)
print(abhiskar_poudel.no_of_leaves)
print(abhiskar_poudel.__dict__)
# but we want to change the value of only one data not all data then we simply write(changing the templete for only abhiskar)
# it does not change the value all over the program but after changing it works for lower part.
# it makes new variable
abhiskar_poudel.no_of_leaves=2#it make instance variable
print(abhiskar_poudel.no_of_leaves)
print(abhiskar_poudel.__dict__)#it shows the list in that dictionary
# Every object in Python has an attribute which is denoted by __dict__, it maps the attribute name to its value. This dictionary is used to stores all the attributes defined for the object itself. Following is the syntax of using __dict__:
print(Employee.__dict__)#attributes

