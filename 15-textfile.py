def read(filename):
    with open(filename,"r") as file:
        print(file.read())

def write(filename):
    with open(filename,"w+",) as file:
        data=input("Enter the data: ")
        file.write(data)
        file.close()
        read(filename)

def append(filename):
    with open(filename,"a+") as file:
        data=input("Enter the data: ")
        file.write(data)
        file.close()
        read(filename)

def search(filename, find):
    try:
        with open(filename,"r") as file:
            for i, data in enumerate(file, 1):
                index=data.find(find)
                if index != -1:
                    print(f"Found {find} at index {index}.")
                    break
            else:
                print(f"{find} not found.")
    except FileNotFoundError:
        print(f"File {filename} Not Found!")
    except Exception as e:
        print(f"Error: {e}")

filename=input("Enter the file name: ")
find=input("Enter the string to be searched: ")
read(filename)
write(filename)
append(filename)
search(filename, find)