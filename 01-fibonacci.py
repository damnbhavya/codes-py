# WAP to print fibonacci series
f=0
s=1
n=int(input("Enter the number of terms: "))
print("Fibonacci Series: ",f,s,end=" ")
for i in range(2,n):
    nx=f+s
    print(nx,end=" ");
    f=s
    s=nx

# # WAP TO PRINT FIBONACCI USING RECURSION
# def fibo(n):
#     if n<=1:
#         return n
#     else:
#         return fibo(n-1)+fibo(n-2)

# n=int(input("Enter the number of terms: "))
# if n<=0:
#     print("Enter a positive integer!")
# else:
#     print("Fibonacci Series:",end=" ")
#     for i in range(n):
#         print(fibo(i) ,end=" ")