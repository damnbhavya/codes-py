# WAP to swap values of two variables without third variable
a=int(input("Enter a number: "))
b=int(input("Enter a number: "))
print("Before Swapping")
print("Value of a=", a,", b=", b)
a,b=b,a
print("After Swapping")
print("Value of a=", a,", b=", b)