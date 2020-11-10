'''
Python is a powerful programming language that supports the object-oriented programming paradigm. In object-oriented programming, the program splits into self-contained objects. Each object is representing a different part of the application which can communicate among themselves. 
We will be discussing classes and objects in more detail in the next tutorial i.e, 
Creating Our First Class In Python. The primary focus of this tutorial is to give you the understanding of Object-Oriented Programming or in short form OOP. 
A programming technique that requires the use of objects and classes is known as OOP. Object-Oriented Programming is based on the principle of writing reusable code that can be accessed multiple times by the user.
'''
# class-template (already written something and adding somthing to it)
# for example of class like if you have anything that is written already and we have to add something (no need to write again and again)
# object-particular thing (instence of the class) or after writting detail in template the final thing is object.
# their main purpose is donot repeat again and again
class friends:
    pass #pass do nothing donot show an error
mesup=friends()
abhiskar=friends()
print(mesup,abhiskar)
# output
# <__main__.student object at 0x7fee6ac29e80> <__main__.student object at 0x7fee6aba56d0>
'''
because they are stored in diffent memory location in main page
they are two different objects 
'''
# if we want to get the something 
class student:
    pass #here we can also put the templete 
# this is the object
mesup_adhikari=student()
abhiskar_poudel=student()
divyan_thapa=student()
# putting the values in variables
mesup_adhikari.name="Mesup Adhikari"
mesup_adhikari.rollno=1
mesup_adhikari.address="Milanchowk"
abhiskar_poudel.name="Abhiskar Poudel"
abhiskar_poudel.rollno=2
abhiskar_poudel.address="Kalika nagar"
divyan_thapa.name="DivaynThapa"
divyan_thapa.rollno=3
divyan_thapa.address="Di butwal"
mesup_adhikari.subject=["maths","english","nepali"]
print(mesup_adhikari.name)
print(mesup_adhikari.rollno , divyan_thapa.rollno,abhiskar_poudel.rollno)
print(mesup_adhikari.name , divyan_thapa.name ,abhiskar_poudel.name)
print(mesup_adhikari.subject)#we can also print list




