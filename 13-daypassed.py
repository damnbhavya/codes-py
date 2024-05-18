def leapyear(year):
    if year%4==0:
        return True
    else:
        return False
def daypassed(day,month,year):
    monthdays=[31,28,31,30,31,30,31,31,30,31,30,31]
    if leapyear(year):
        monthdays[1]=29
    daycount=day
    month-=1
    while month>0:
        daycount+=monthdays[month-1]
        month-=1
    return daycount

while True:
    try:
        d=int(input("Enter the day:"))
        m=int(input("Enter the month: "))
        y=int(input("Enter the year: "))
        if d<1 or d>31 or m<1 or m>12:
            print("Invalid day or month. Please enter again.")
            continue
        if m==2 and d>29:
            print("Invalid day for February. Please enter again.")
            continue
        if m==4 or m==6 or m==9 or m==11:
            if d>30:
                print("Invalid day for this month. Please enter again.")
                continue
    except:
        print("Invalid Input!!")
    print("Number of days passed: ", daypassed(d,m,y))