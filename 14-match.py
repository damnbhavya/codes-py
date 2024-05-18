while True:
    t1=eval(input("Enter a point(x,y): "))
    t1=tuple(t1)
    match t1:
        case (0,0):
            print("Origin")
        case (x,0):
            print("X=",x)
        case (0,y):
            print("Y=",y)
        case (x,y):
            print("X=",x,"Y=",y)
        case _:
            raise ValueError("Not a point")
    x=input("Do you want to stop? True/False: ")
    if not(x):
        break
    else:
        continue