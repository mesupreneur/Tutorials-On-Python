#dictionary is a key(word) and (value)meaning
dict1={}
print(type(dict1))
#donot forget that {}braket is used as dictionary 
#In list we use [] braket and it is called mutable(can change the value in the list)
#In list we use ()bracket or tuple  and it is called immutable (cannot change the value in the list)
#In dictinary keys are immutable
d1={"Mesup":"name of person who live in Milanchowk","Abhiskar":"name of the person who live in Kalikanagar"}
print(d1)
#here the mesup is the key and name of the person who live in Milanchowk is the value
#we can also query the value by putting name(key)
print(d1["Mesup"])#remember that we cannot write small if the key is in capital(casesensative)
print(d1["Abhiskar"])
#we can also make dictionary inside keys
d2={"Mesup":"Roti","Rahul":"Meat","Abhiskar":{"Breakfast":"Bread,Jam","Lunch":"Rice,vegetable"}}
print(d2["Abhiskar"])
print(d2["Abhiskar"]["Breakfast"])
print(d2["Abhiskar"]["Lunch"])
#1st method to print the value from dictionary
print(d2["Mesup"])
#or
#2st method to print the value from dictionary
print(d2.get("Mesup"))#using functions to print the value of keys
#To add anythings In dictionary then there are two different methods to add
#1ST METHOD 
d3={"Mesup":"Roti","Rahul":"Meat"}
d3["Abhiskar"]="junk food"
d3[4039]="MESUP CAR NO"#Inside dictionary keys may be string or integer 
print(d3)
#2ST METHOD 
d3={"Mesup":"Roti","Rahul":"Meat"}
d3["Abhiskar"]="junk food"
d3.update({4039:"MESUP CAR NO"})
print(d3)
#to delect anything in the dictionary
d3={"Mesup":"Roti","Rahul":"Meat"}
d3["Abhiskar"]="junk food"
d3["Hari"]="lollypop"
print(d3)#here i have printed all before delecting
del d3["Abhiskar"] #to delect step (del variable name and ["key to delect"])
print(d3)
"""functions in dictionary"""
print(d3.copy())#it copies the dictionary
"""for example of copy"""
"""without using copy and if we only use d5=d4 then it donot make new copy(what we do it does for both)
if we use .copy then it makes new copy (what we do in one it donot does for both it makes these dictionary
seperate)
"""
#example of without using copy
d4={"hello":"word to say after metting people","laptop":"machine"}
d5=d4
del d5["hello"]
print(d4)#they both are same beacues it applies to both if we change any one of them
print(d5)
#example using copy function in dictionary
d4={"hello":"word to say after metting people","laptop":"machine"}
d5=d4.copy()
del d5["hello"]
print(d4)#they becomes different if we make it different
print(d5)
#to print keys of the dictionary
d6={12:"integer","mesup":"string"}
print(d6.keys())
#to print items of the dictionary
print(d6.items())
#dictionary functions libary











