# WAP to print factors of a number
a=int(input("Enter number: "))
print("Factors: ")
for i in range(1,a+1):
    if(int(a%i)==0):
        print(i,end=" ")