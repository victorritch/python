import csv 
with open("names.csv",mode="w")as csvfile:
    fieldnames = ["first_name," "last_name"]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerow({"first_name":"Test", "last_name": "Person"})
#geeksforgeeks.org I got the dictwriter from their csvwrite-up which allows me to write rows of data
import csv
import os

FileLoc = "ContactMangerData.csv"
ContactData = []

def showCommandList ():
    #showing all commands for the user to verify
    print("1 - Create New Contact File")
    print("2 - Add New Contact")
    print("3 - View All Contacts")
    print("4 - Modify An Existing Contact")
    print("5 - Save and Exit")
    
def SaveData():
    #saving your rows you typed
    with open(FileLoc, "w") as File:
        WriteData = csv.writer(File)
        WriteData.writerows(ContactData)
        print("Saved Contact Data!")

def LoadData():
    #learnpython shows how to append and read files
    if not os.path.exists(FileLoc):
        SaveData()
        print("Creating New ContactData file")
    with open(FileLoc, "r") as File:
        ReadData = csv.reader(File)
        for row in ReadData:
            ContactData.append(row)
    print("Loaded Contact Data!")

def CreateNewContact():
    Name = input ("Enter The New Contact Name: ")
    PhoneNumber = input ("Enter New Contact Phone Number: ")
    Email = input (" Enter The New Email Address: ")
    ContactData.append([
        Name,
        PhoneNumber,
        Email
        ])      
    print("Created New Contact Successfully!") 

def ViewAllContacts():
    print("\n")
    print("Contact Info")
    print("-----------------------------------")
    print("Name \t \t Phone \t \t Email")
    for Contact in ContactData:
        print(f"{Contact[0]} \t \t {Contact [1]} \t \t {Contact [2]}")
def ModifyContact():
    #showing contacts modify is changing the contact name
    ViewAllContacts()
    print("Modify Contact")
    print("-----------------------------------")
    while True:
        ModifyName = input("Enter the Name of the Contact you want to modify: ")
        for Contact in ContactData:
            if Contact[0] == ModifyName:
                NewPhoneNumber = input ("Enter New Phone Number: ")
                NewEmail = input ("Enter New Email: ")
                Contact [1] = NewPhoneNumber
                Contact [2] = NewEmail
                SaveData()
                print("Updated Contact Data Successfully!")
                return
        print("Contact not found! (enter the exact name as shown)")

def RunCommands ():
    #Taking out old data from files
    while True:
        print("\nEnter the following commands to peform the corresponding action: ")
        showCommandList ()
        Command = input ("Enter a command Number: ")
        print("\n-----------------------")
        Command = Command[0]
        if Command.indigit():
            Command = int(Command)
            if Command <= 5 and Command > 0:
                if Command == 1:
                    os.remove(FileLoc)
                    ContactData.clear()
                    SaveData()
                    print("Created New Contact File Successfully!")
                if Command == 2:
                    CreateNewContact()
                if Command ==3:
                    ViewAllContacts
                if Command ==4:
                    ModifyContact() 
                if Command ==5:
                    SaveData()
                    print("Existing...")
                    break
            else:
                print("wrong Command")
        else:
            print("wrong Command")

def Main():
    print("Welcome to the Contact Manger App")
    print("-----------------------------------")

    LoadData()
    RunCommands()
    SaveData()

    print("Completed by Victor Ritcherson")

Main()

