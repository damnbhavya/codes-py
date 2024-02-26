# WAP to check whether a given number is armstrong or not
n=int(input("Enter a number: "))
t=n
c=r=s=0
while(n>0):
    c+=1
    n=int(n/10)
n=t
while(n>0):
    r=n%10
    s=s+pow(r,c)
    n=int(n/10)
if(s==t):
    print("Armstrong Number")
else:
    print("Not an Armstrong Number")