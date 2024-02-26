# WAP to find hcf of two numbers 
a=int(input("Enter the number: "))
b=int(input("Enter the number: "))
m=min(a,b)
for i in range(1,m+1):
    if(a%i==0 and b%i==0):
        hcf=i
print("HCF: ",hcf)