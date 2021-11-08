from os import name
from contact import *
from console import fg
from console.utils import cls
import csv


'''
!!!Run this program directly from the .py file or using the python interpreter due to error reading CSV file!!!
This is a simple command app used as a contact book to manage your contacts and store them on a CSV file for easy portability
'''
contact_list = []


def menu():
    cls()
    print("""\
        
        
       ______            __             __     ____              __  
      / ____/___  ____  / /_____ ______/ /_   / __ )____  ____  / /__
     / /   / __ \/ __ \/ __/ __ `/ ___/ __/  / __  / __ \/ __ \/ //_/
    / /___/ /_/ / / / / /_/ /_/ / /__/ /_   / /_/ / /_/ / /_/ / ,<   
    \____/\____/_/ /_/\__/\__,_/\___/\__/  /_____/\____/\____/_/|_|  
                                                                 
                                                                    \n""")
    # The different menu navigation numbers
    print(fg.green("0. ")+"Exit")
    print(fg.green("1. ")+"Add Contact")
    print(fg.green("2. ")+"Delete Contact")
    print(fg.green("3. ")+"Update Contact")
    print(fg.green("4. ")+"View Contacts")
    print(fg.green("5. ")+"Save Contacts to CSV")
    print(fg.green("6. ")+"Load Contacts from CSV\n")
    choice_number = int(input("Input a number to chose option: "))
    if choice_number == 0:
        quit()
    elif choice_number == 1:
        cls()
        add_contact()
    elif choice_number == 2:
        cls()
        delete_contact()
    elif choice_number == 4:
        cls()
        print_contacts()
    elif choice_number == 5:
        cls()
        save_to_csv()
    elif choice_number == 6:
        cls()
        load_contacts_from_csv()


def add_contact():
    # input name and number
    name = input("Enter Name: ")
    number = input("Enter Number: ")

    # check if number is an int
    while not number.isdigit():
        print("Wrong input")
        number = input("Enter Number again: ")
    # create Contact object using inputs
    new_contact = Contact(name, number)
    # add Contact to the list of contacts
    contact_list.append(new_contact)
    menu()


# print all contacts in array
def print_contacts():
    for i in contact_list:
        li = str(i).split(" ")
        print("Name: "+li[0], " | ", "Number: "+li[1])
    input_choice = int(input("Input 0 to exit: "))
    if input_choice == 0:
        menu()


def delete_contact():
    cls()
    counter = 0
    # display the contacts first
    for i in contact_list:
        counter += 1
        print(fg.red(str(counter)+". "), end="")
        li = str(i).split(" ")
        print("Name: "+li[0]+" | "+"Number: "+li[1])
    selected_contact = None
    # input which contact you would like to delete
    while selected_contact != 0:
        selected_contact = int(
            input("Input number of the contact you wish to delete and 0 to exit: "))
        if selected_contact != 0:
            contact_list.pop(selected_contact-1)
            delete_contact()
    menu()


# save all current data to the a csv file named contact_list.csv in the base directory
def save_to_csv():
    file = open("contact_list.csv", "w", newline='')
    csvwriter = csv.writer(file)
    csvwriter.writerow(["Name", "Number"])

    for i in contact_list:
        li = str(i).split(" ")
        csvwriter.writerow(li)
    file.close()
    menu()


# load all contacts from a csv file by creating Contact objects from the csv data and then adding tem to the contact list
def load_contacts_from_csv():
    file = open("contact_list.csv", 'r', newline='')
    reader = csv.reader(file)
    loaded_data = list(reader)
    loaded_data.pop(0)
    contact_list.clear()
    for i in loaded_data:
        name = i[0]
        number = i[1]
        new_contact = Contact(name, number)
        contact_list.append(new_contact)
    menu()


cls()
menu()
