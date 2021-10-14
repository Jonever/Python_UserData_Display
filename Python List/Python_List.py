import os
import re
import random

def clear():
    os.system('cls' if os.name in ('nt', 'dos') else 'clear')

listInfo_ = []
dateRegex = '(jan|feb|mar|apr|may|jun|jul|aug|sep|oct|nov|dec). ([1-2][0-9]|[3][0-1]|[1-9]), ([1][0-9][0-9][0-9]|[2][0-5][0-9][0-9])'

def addItem_():
    item = {} #dictionary
    item['id'] = generateID_() #add ID Value to dictionary
    print("Add Item Selected")
    print()
    found = True #boolean variable if name and lastname found
    while found == True: #while loop if name and last name found end loop if name and last name not found
        item['name'] = inputCheck("Name: ").title().replace(" ","")#add name
        lastname = inputCheck("Last Name: ").title().replace(" ","")#add lastname
        itemFound = False
        for info in listInfo_:#check from List if name and last name is already exsist
            if info['lastname'].lower() == lastname.lower() and info['name'].lower() == item['name'].lower():# if name and last name found
                itemFound = True
        if itemFound == True:#if name and last name is found
            print("Name and last name already exist")
        else:
            found = False# if not found end while loop

    item['lastname'] = lastname #add last name to dictionary
    item['middlename'] = inputCheck("Middle Name: ").title()#add middle name to dictionary
    bday = None
    while bday == None:#While Loop check if date format is valid
        input_ = inputCheck("Birth Day(mmm. dd, yyyy): ")#input for date
        res = re.match(dateRegex,input_)#check regex if match format
        if res is not None:
            bday = input_
    item['birthday'] = bday.title()#add birth date to dictionary
    age = None
    while age == None:#while loop check if input is valid number
        try:
            age = int(inputCheck("Age: "))#conver string to integer catch exception if input is not valid number
        except:
            pass
    item['age'] = age#add Age value to dictionary
    item['job'] = inputCheck("Job: ").title()#add Job value to dictionary
    salary = None
    while salary == None:#while loop check if input is valid value
        try:
            salary = int(inputCheck("Salary: "))#convert string to integer catch exception if input is not valid number
        except:
            pass
    item['salary'] = salary#Add salary value to dictionary
    listInfo_.append(item)#Add dictionary item to List
    print("Item ID: " + str(item['id']))
    print("Item Added Succesfully")

def insertItem_():
    item = {}
    item['id'] = generateID_()
    print("Insert Item Selected")
    print()
    index = None
    while index == None:
        try:
            i = int(inputCheck("Index: "))
            if i <= len(listInfo_):
                index = i
            else:
                print("Index must be less than or equal: " + str(len(listInfo_)))
        except:
            print("Ivalid Index")

    found = True
    while found == True:
        item['name'] = inputCheck("Name: ").title().replace(" ","")
        lastname = inputCheck("Last Name: ").title().replace(" ","")
        itemFound = False
        for info in listInfo_:
            if info['lastname'].lower() == lastname.lower() and info['name'].lower() == item['name'].lower():
                itemFound = True
        if itemFound == True:
            print("Name and last name already exist")
        else:
            found = False
    item['lastname'] = lastname
    item['middlename'] = inputCheck("Middle Name: ").title()
    bday = None
    while bday == None:
        input_ = inputCheck("Birth Day(mmm. dd, yyyy): ")
        res = re.match(dateRegex,input_)
        if res is not None:
            bday = input_
    item['birthday'] = bday.title()
    age = None
    while age == None:
        try:
            age = int(inputCheck("Age: "))
        except:
            pass
    item['age'] = age
    item['job'] = inputCheck("Job: ").title()
    salary = None
    while salary == None:
        try:
            salary = int(inputCheck("Salary: "))
        except:
            pass
    item['salary'] = salary
    listInfo_.insert(index,item)
    print("Item ID: " + str(item['id']))
    print("Item Insert Succesfully")

def updatetItem_():
    item = {}
    print("Update Item Selected")
    print()
    done = False
    while done == False:
        item['name'] = inputCheck("Name to be update: ").title().replace(" ","")#Add name to find
        lastname = inputCheck("Last name to be update: ").title().replace(" ","")#Add last name to find
        found = False
        for info in listInfo_:#for loop check if name and last name found
            if info['lastname'].lower() == lastname.lower() and info['name'].lower() == item['name'].lower():#if item is found. then update item next
                bday = None
                while bday == None:
                    input_ = inputCheck("Set birth Day(mmm. dd, yyyy): ")
                    res = re.match(dateRegex,input_)
                    if res is not None:
                        bday = input_
                    info['birthday'] = bday.title()#update birth day if date format is valid
                age = None
                while age == None:
                    try:
                        age = int(inputCheck("Set age: "))#check if input is valid age number
                    except:
                        pass
                info['age'] = age
                info['job'] = inputCheck("Set job: ").title()#update job value from list
                salary = None
                while salary == None:
                    try:
                        salary = int(inputCheck("Set salary: "))#check if valid number
                    except:
                        pass
                info['salary'] = salary
                print("Item Update Succesfully")
                found = True
                done = True
                break
        if found == False:
            print("Item Not Found")


def findItem_():
    print("Find Item Selected")
    print()
    item = {}
    item['name'] = inputCheck("Name: ").title().replace(" ","")#add name to dictionary
    item['lastname'] = inputCheck("Last Name: ").title().replace(" ","")#add last name to dictionary
    itemFound = False
    for info in listInfo_:#for loop check all item from list
        if info['lastname'].lower() == item['lastname'].lower() and info['name'].lower() == item['name'].lower():#check if item is found
            item = info
            itemFound = True
    if itemFound == True:#if item found print all info from the item
        print()
        print("Item Info:")
        print("\tID: " + str(info['id']))
        print("\tName " + info['name'])
        print("\tLast Name: " + info['lastname'])
        print("\tMiddle Name: " + info['middlename'])
        print("\tBirth Day: " + info['birthday'])
        print("\tAge: " + str(info['age']))
        print("\tJob: " + info['job'])
        print("\tSalary: " + str(info['salary']))
    else:
        print()
        print("Item Not Found")

def itemDelete_():
    print("Delete Item Selected")
    print()
    done = False
    while done == False:
        name = inputCheck("Name to be delete: ").title().replace(" ","")#input name to find
        lastname = inputCheck("Last name to be delete: ").title().replace(" ","")#input lastname to find
        found = False
        for i in range(len(listInfo_)):#while loop check if item is exist
            info = listInfo_[i]
            if info['lastname'].lower() == lastname.lower() and info['name'].lower() == name.lower():#if item found
                listInfo_.pop(i)#delete item from index i
                print()
                print("Item Deleted Successfully")
                found = True
                done = True
                break
        if found == False:
            print("Item Not Found")

def itemShowAll_():
    print("Show All Item Selected")
    print()
    print("Item Info:")
    for info in listInfo_:#for loop print one by one item from list
        print("\tID: " + str(info['id']))
        print("\tName " + info['name'])
        print("\tLast Name: " + info['lastname'])
        print("\tMiddle Name: " + info['middlename'])
        print("\tBirth Day: " + info['birthday'])
        print("\tAge: " + str(info['age']))
        print("\tJob: " + info['job'])
        print("\tSalary: " + str(info['salary']))
        print()

def itemClearAll_():
    print("Clear All Item Selected")
    print()
    listInfo_.clear()#Clear all items
    print("All item has been removed successfully")

def showAllSalary_():
    print("Show All Salary Selected")
    print()
    print("Salary Info:")
    total_salary = 0
    count = len(listInfo_)#check list item count
    for info in listInfo_:#loop to read all item salary
        total_salary += info['salary']#salary from item add to total_salary
        print("\t" + info['name'] + " " + info['middlename'] + " " + info['lastname'] + ": Salary " + str(info['salary']) + ".00")
    print("\t-Total Salary: " + str(total_salary) + ".00")#print total salary
    print("\t-Average Salary: " + str(total_salary/count))#print average salary

def inputCheck(message):#Chech if input is not blank
    input_ = ""
    while True:
        print(message ,end = "")
        input_ = input()
        if input_ != "":
            break
    return input_

def generateID_():#Generate Random Number
    id_ = False
    while id_ == False:
        i = random.randrange(10000, 999999, 1)
        found = False
        for info in listInfo_:
            if info['id'] == i:
                found = True
        if found == False:
            id_ = i
    return id_

def Start():
    print("Course/Year: BSIT-A1")
    print()
    print("Item Count: " + str(len(listInfo_)))
    print("\r\nOptions:")
    print("\t1:Add Item")
    print("\t2:Find Item")
    print("\t3:Update Item")
    print("\t4:Insert Item")
    print("\t5:Delete Item")
    print("\t6:Show All Item")
    print("\t7:Clear All Items")
    print("\t8:Show All Salary")
    print("\t9:Exit")
    print()
    option = 0
    while option == 0:
        try:
            print("Select Number: " ,end = "")
            option = int(input())
        except:
            pass

    if option == 1:
        addItem_()
    elif option == 2:
        findItem_()
    elif option == 3:
        updatetItem_()
    elif option == 4:
        insertItem_()
    elif option == 5:
        itemDelete_()
    elif option == 6:
        itemShowAll_()
    elif option == 7:
        itemClearAll_()
    elif option == 8:
        showAllSalary_()
    elif option == 9:
        exit()

while True:
        Start()
        print()
        input("Press enter to clear")
        clear()