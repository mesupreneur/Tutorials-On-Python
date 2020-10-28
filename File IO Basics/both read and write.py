#if we want to open the file for both read and write we simply write r+
f=open("file_read_and_write.txt","r+")
print(f.read())#we can read like this
f.write("yes it is write ")#we can write like this
f.write("hi bro")