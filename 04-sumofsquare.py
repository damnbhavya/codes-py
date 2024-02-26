# WAP to print sum of squares
a=int(input("Enter a number: "))
sum=i=0
# for i in range(0,a+1):
#     sum=i**2+sum
while(i<a+1):
    sum=i**2+sum
    i+=1
print("Sum of square: ",sum)