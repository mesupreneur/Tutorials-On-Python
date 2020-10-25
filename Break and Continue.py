#The break keyword is used to break out a for loop, or a while loop.
#The continue keyword is used to end the current iteration in a for loop (or a while loop), and continues to the next iteration.
i=0
while(i<45):
    print(i+1,end=" ")#end=""helps to print the line in same statement and i+1 helps to start from 1 to 45
    i=i+1
"""
if we write while(True): then it never stops print........
so to stop we use break
"""
i=0
while(True):
    print(i ,end=" ")#end=" "keeping space so that while printing it makes gaps
    if(i==44):
        break  #stop the loop
    i=i+1
    """(there was while(true)condition so that it never stops
    so, to make stop by putting again the condition write break so that if the condition get satisfied it stop the program,)"""
"""
i+1=1 means i+=1
"""
for item in range(1,6):
    print(item)
#break
for items in range(1,6):
    print(items)
    break
"""
output is
1
"""
for item in range(1,6):
    if item==3: #when loop comes to 3 then it become true(3=3) then it stop the loop and goes down 
        break
    print(item)
print("the end")#we have to print 
"""
output is 
1
2
the end
"""
i=0
while(True):
    if i+1<5:
        continue#continue means donot go down and it goes up to while loop(if we write continue and it is true then it donot go down)
    print(i+1,end="")
    if(i==44):
        break
    i=i+1
"here the output is notthing because the condition is true"   
i=0
while(True):
    if i+1<5:
        i=i+1
        continue
    print(i+1,end="")
    if(i==44):
        break
    i=i+1