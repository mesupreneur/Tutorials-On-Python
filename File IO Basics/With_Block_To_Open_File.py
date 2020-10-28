#to open file, we write f=open("file_read.txt")
# same as  f=open("file_read.txt") we can also use with open ("file_read.txt") as f:
'''
if we use with open method to open the file then we donot need to close the file but using previous method we have to close the file
'''
with open("file_read.txt") as f:
    print(f.readline())
    a=f.readline()
    print(a)
#they both are same 
f=open("file_read.txt")
print(f.readlines())