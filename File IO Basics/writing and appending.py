# To write to an existing file, you must add a parameter to the open() function:
# "a" - Append - will append to the end of the file
# "w" - Write - will overwrite any existing content
'''
in writing
#if there is no such type of file then it makes a new file with the name of the which we have given.
#if there is already a content in the file it delect the previous content and write what the user have written.
'''
f = open("file_write.txt","w")#if the file has any content in it then it replace the file content with new what the uer have written. 
f.write("mesup is good boy.")
f.close()
#appending
'''
it helps to join the text at the end in the file '''
f= open("file_write.txt", "a")
f.write("hi bro")
f.close()
#to know how much character we have written.
f= open("file_write.txt", "a")
a=f.write("hi bro")
print(a)#to know how much character we have written.
f.close()


