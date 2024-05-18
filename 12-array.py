from array import *
arr = array('i',[10,20,30,40,50])
for i in arr:
    print(i,end=" ")
print(" ")
print(arr.buffer_info())
print(arr.typecode)
arr.reverse()
print(arr)