import csv
def read():
      with open("codes-py//csvfile.csv") as file:
            reader = csv.reader(file)
            print("%10s"%"EMPNO","%20s"%"EMP NAME","%10s"%"SALARY")
            print("______________________________________________")
            for row in reader:
                  print("%10s"%row[0],"%20s"%row[1],"%10s"%row[2])

def count():
      with open("C:\\Users\\Bhavya\\OneDrive\\codes\\python\\twelve-py\\files\\05.csv") as file:
            reader = csv.reader(file)
            count = 0
            print("%10s"%"EMPNO","%20s"%"EMP NAME","%10s"%"SALARY")
            print("______________________________________________")
            for row in reader:
                  print("%10s"%row[0],"%20s"%row[1],"%10s"%row[2])
                  count +=1
            print("______________________________________________")
            print("%30s"%"TOTAL RECORDS : ",count)
            print("______________________________________________")

def sums():
      with open("C:\\Users\\Bhavya\\OneDrive\\codes\\python\\twelve-py\\files\\05.csv") as file:
            reader = csv.reader(file)
            count = 0
            sm = 0
            print("%10s"%"EMPNO","%20s"%"EMP NAME","%10s"%"SALARY")
            print("______________________________________________")
            for row in reader:
                  print("%10s"%row[0],"%20s"%row[1],"%10s"%row[2])
                  sm += int(row[2])
                  if int(row[2]) > 70000:
                        count +=1
            print("______________________________________________")
            print("%30s"%"TOTAL RECORDS : ",count)
            print("%40s"%"EMPLOYEE WITH 70000+ SALARY : ", count)
            print("______________________________________________")

def write():
      with open("C:\\Users\\Bhavya\\OneDrive\\codes\\python\\twelve-py\\files\\05.csv", mode = 'a', newline='') as file:
            writer = csv.writer(file,delimiter=',')
            ch = 'y'
            while ch.lower() == 'y':
                  eno = int(input("ENTER EMPLOYEE NUMBER : "))
                  name = input("ENTER EMPLOYEE NAME : ")
                  salary = int(input("ENTER EMPLOYEE SALARY : "))
                  data = [eno,name,salary]
                  writer.writerow(data)
                  print("______________________________________________")
                  print("DATA SUCCESSFULLY RECORDED!")
                  print("______________________________________________")
                  ch = input("DO YOU WANT TO ADD MORE RECORDS? Y/N : ")
def update():
      with open("C:\\Users\\Bhavya\\OneDrive\\codes\\python\\twelve-py\\files\\05.csv", mode = 'r') as file:
            read = csv.reader(file)
            ans = 'y'
            c=0
            while ans.lower() == 'y':
                  found = False
                  e = int(input("ENTER EMPLOYEE NUMBER TO SEARCH : "))
                  for row in read:
                        if len(row) !=0:
                              c+=1
                              if int(row[0]) == e:
                                    name = input("ENTER EMPLOYEE NAME : ")
                                    salary = int(input("ENTER EMPLOYEE SALARY : "))
                                    data = [e,name,salary]
                                    lines = list(read)
                                    lines[e-1] = data
                                    with open("C:\\Users\\Bhavya\\OneDrive\\codes\\python\\twelve-py\\files\\05.csv", mode = 'w') as wfile:
                                          writer=csv.writer(wfile)
                                          writer.writerows(lines)
                                    # row=row.replace(row,data)
                                          print("______________________________________________")
                                          print("UPDATE DETAILS: ")
                                          print("EMPLOYEE NO : ", row[0])
                                          print("EMPLOYEE NAME : ", row[1])
                                          print("EMPLOYEE SALARY : ", row[2])
                                          found = True
                                          break
                        elif not found:
                              print("______________________________________________")
                              print("EMPLOYEE RECORD NOT FOUND.")
                              print("______________________________________________")
                  ans = input("DO YOU WANT TO SEARCH AGAIN? Y/N : ")
def search():
      with open("C:\\Users\\Bhavya\\OneDrive\\codes\\python\\twelve-py\\files\\05.csv", mode = 'r') as file:
            read = csv.reader(file)
            ans = 'y'
            while ans.lower() == 'y':
                  found = False
                  e = int(input("ENTER EMPLOYEE NUMBER TO SEARCH : "))
                  for row in read:
                        if len(row) !=0:
                              if int(row[0]) == e:
                                    print("______________________________________________")
                                    print("EMPLOYEE NAME : ", row[1])
                                    print("EMPLOYEE SALARY : ", row[2])
                                    found = True
                                    break
                        elif not found:
                              print("______________________________________________")
                              print("EMPLOYEE RECORD NOT FOUND.")
                              print("______________________________________________")
                  ans = input("DO YOU WANT TO SEARCH AGAIN? Y/N : ")

def mainmenu():
    print("______________________________________________")
    print("1. READING FROM CSV FILE")
    print("2. COUNTING NUMBER OF RECORDS")
    print("3. SUM OF SALARY AND COUNTING EMPOLYEE GETTING MORE THAN 70000 ")
    print("4. WRITING DATA TO CSV FILE")
    print("5. UPDATE MEMBER DETAILS ")
    print("6. SEARCHING ANY EMPLOYEE NO")
    print("7. EXIT")
    print("______________________________________________")

while True:
    mainmenu()
    ch = int(input("ENTER ACTION : "))
    if ch == 1:
        read()
    elif ch == 2:
        count()
    elif ch == 3:
        sums()
    elif ch == 4:
        write()
    elif ch == 5:
        update()
    elif ch == 6:
        search()
    elif ch == 7:
        break