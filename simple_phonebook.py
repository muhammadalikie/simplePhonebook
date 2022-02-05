import os


PATH = "C:/Users/markazi/Desktop/python-faradars/python/database.txt"


# validation :


def validation():
    if not os.path.exists(PATH):
        f = open(PATH, 'w+')
        f.write("")


# start function:


def add(name, number):
    validation()

    f = open(PATH, 'a')
    new_phone = name + ":" + number + "\n"
    f.write(new_phone)
    f.close()


def search(name):
    validation()

    f = open(PATH, 'r')
    for line in f.readlines():
        if name ==  line.split(":")[0]:
            print(name + ":" + line.split(":")[1])

    f.close()


def delete(name):
    validation()

    f = open(PATH, 'r')
    new_database = ""
    for line in f.readlines():
        if not name == line.split(":")[0]:
            new_database += line
    f.close()

    f = open(PATH, 'w')
    f.write(new_database)
    f.close()

def show_all():
    validation()

    f = open(PATH, 'r')
    database = ""
    database = f.read()
    f.close()
    print(database)



### start


ch = 1


while ch != 0 :


    print("1 - Add User\n2 - search phone\n3 - delete phone\n4 - show all\n0 - exit")
    ch = int(input("Enter your choice: "))
    os.system("cls")
    

    if ch == 1:
        name = input("enter name: ")
        number = input("enter number: ")
        add(name, number)


    elif ch == 2:
        name = input("enter name: ")
        search(name)
        

    elif ch == 3:
        name = input("enter name: ")
        delete(name)


    elif ch == 4:
        show_all()