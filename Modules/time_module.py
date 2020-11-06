# to get the time in how much time program is executed
# using for loop
import time
initial=time.time()
for i in range(4):
    print("this is mesup")
print(f"for loop ran time{time.time()-initial}")
# using while loop 
initial2=time.time()
k=0
while k<4:
    print("mesup")
    k+=1
print(f"while loop ran time {time.time()-initial2}")
# it helps to stop for second
time.sleep(5)
# to get local time
localtime = time.asctime(time.localtime(time.time()))
print(localtime)