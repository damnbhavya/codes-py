# WAP to print the grade of a student
import math
a=float(input("Enter 1st number:"))
b=float(input("Enter 2nd number:"))
c=float(input("Enter 3rd number:"))
marks=int(input("Enter the marks: "))
if(marks>=91):
    print("Grade A")
elif(marks>=81):
    print("Grade B")
elif(marks>=71):
    print("Grade C")
elif(marks>=61):
    print("Grade D")
elif(marks>=51):
    print("Grade E")
else:
    print("Pass")