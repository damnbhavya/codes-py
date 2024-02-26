# WAP to find lcm of two numbers
a=int(input("Enter number 1: "))
b=int(input("Enter number 2: "))
m=max(a,b)
lcm=m
while True:
    if lcm%a==0 and lcm%b==0:
        break
    lcm+=m
print("LCM: ",lcm)