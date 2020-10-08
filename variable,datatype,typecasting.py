#VARIABLES,DATATYPING,TYPECASTING
#TO PRINT ONLY ONE WORD
print("Hello")
#BUT TO PRINT LONG WORD
#VARIABLE IS USED TO STORE SOMETHING(CONTAINER)
Var1="HELLO WORD"
print(Var1)
#TYPES OF VARIABLES(Three types of variables)
#STRING VARIABLE--
Var1="HELLO WORLD"
print(type(Var1))
#INTEGER VARIABLE
Var2= 4
print(type(Var2))
#FLOAT VARIABLE
Var3= 36.7
print(type(Var3))
#now when we add strings with number variables like integer or float ,it will be wrong
#like (var1+var3) or (var1+var2) but if we add strings with strings then it will show
Var1="HELLO WORD "#ALWAYS REMEMBER THAT IF WE PUT SPACE IN INSIDE STRING VARIABLE THEN RESULT WILL SPACE
Var5="MESUP"
print(Var1+Var5)
#WE CAN EASILY ADD INTEGER WITH FLOAT
Var6=4
Var7=37.99
print(Var6+Var7)
#WE HAVE TO PRINT WHEN WE WRITE type
print(type(Var7))#ALWAYS REMEMBER THAT type is in small letter
#SEE IF WE ALSO WRITE NUMBER BUT IT IS ENCLOSED WITHIN SEMICOLON("")THEN IT BECOMES STRING
Var8="42 "
Var9="50"
print(Var8+Var9)
#if you want to print word multiple times then
print(10 * "helloword")
#if you want to print in different line then use escape character that is \n
print(10*"helloword\n")#remember that \n is use inside("")
"""------------------------TYPE CASTING --------------------------------
str()
int()
float()
"""
#if we do any operation with integer with integer then it will be like this
Var10="50"#remeber that this is string print(type(Var1))
Var11="32"
#REMEMBER THAT WE ARE CHANGING STRING TO INTEGER
print(100* int(Var10)+int(Var11))#AND OPERATIN OF INTEGER AND INTEGER WILL NOT PRINT MULTIPLE TIMES BUT DO OPERATION AND FIND ANS
#AND WE WE WANT TO REPEAT MULTIPLE TIME WE WE MAKE INTEGER INTO STRING USING TYPECASTING
print(100* str(int(Var10)+int(Var11)))#str(int(Var10)+ int(Var11))this will do then 82*100 ,it comes
#if we wnt to make user to input
print("enter your nunber")
no=input()#input use to input from user.(remember that inputs always goes in string )
print("you entered",no)
#but if want to add the number
print("enter your nunber")
mesup=input()
print("you entered", int(mesup)+10)#we have to make srting to integer because input always take string
#type casting #remember that int(mesup)+10)
#making calculator that add two number
print("enter your first number")
n1=input()
print("enter your number number")
n2=input()
print("sum of these numbers is",int(n1)+int(n2))
