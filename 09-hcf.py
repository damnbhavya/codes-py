# WAP to find hcf of two numbers
def hcf(a,b):
    while b:
        a,b = b, a%b
    return a
a=int(input("Enter number 1: "))
b=int(input("Enter number 2: "))
print("HCF: ",hcf(a,b))