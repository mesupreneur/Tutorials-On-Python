f = open("file_read.txt","rb")#here "r" is default
content=f.read()
print(content)
f.close()#if we have opened anything then we have to close it.(as expected behave)
'''
how much user want to read he/she can read
'''
f = open("file_read.txt","r")#here "r" is default
content=f.read(3)
print(content)
f.close()#if we have opened anything then we have to close it.(as expected behave)
'''
here it read first mes and up and space in reading second
'''
#if we write in same to read file 
f = open("file_read.txt","rb")#here "r" is default
content=f.read(3)
print(content)
content=f.read(3)
print(content)
f.close()#if we have opened anything then we have to close it.(as expected behave)
#if we write big no then it print all 
f = open("file_read.txt","rb")#here "r" is default
content=f.read(3423478365)
print(content)
content=f.read(3039759)#here it write nothing because all the content is written by first one read
print(content)
f.close()

#we want to print character by characters then we write
f = open("file_read.txt","rt")
content=f.read()
for line in content:
    print(line)
f.close()
#if we want to print line by line we simply write 
f = open("file_read.txt","rt")#here "r" is default
for line in f:
    print(line,end="")
f.close()
#if we want to print one or limited line
#readline
f = open("file_read.txt","rt")#here "r" is default
print(f.readline())
print(f.readline())
print(f.readline())
print(f.readline())
f.close()
#readlines helps to store it in the list. 
f= open("file_read.txt","rt")#here "r" is default
print(f.readlines())
f.close()

