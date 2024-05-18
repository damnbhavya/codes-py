# WAP to find lcm of two numbers
def gcd(a,b):
    while b:
        a,b = b, a%b
    return a
def lcm(a,b):
    return (a*b)//gcd(a,b)
a=int(input("Enter number 1: "))
b=int(input("Enter number 2: "))
print("LCM: ",lcm(a,b))