import pandas as pd
import json
import os
from person_class import Person
from student_class import Student
from employee_class import Employee
from MenuOptions import MenuOptions

try:
    def emptyDict(dict):
        if not dict:
            print("Error: The dictionary is empty")
            return True
        
    def errorNumber(name_value, value):
        print("Error: " + name_value + " must be a number. " + value + " is not a number")

    def saveNewEntry(people_dict):
        person_types = [Student, Employee, Person]
        for i, value in enumerate(person_types):
            print("For saving a " + value.__name__ + " please press "+ str(i + 1))
        
        type_input = input("Please enter your choice: ")
        type_input_index = int(type_input) - 1
        try:
            if type_input_index not in range(len(person_types)) :
                print("Option '" + type_input + "' does not exist. Please try again")
                return 0
        except:
            print("Option '" + type_input + "' does not exist. Please try again")

        id_input = input("ID: ")
        if id_input.isdigit(): #check if id is a integer
            if id_input in people_dict:
                print("Error: ID already exists: " + str(people_dict[id_input]))
                return 0
        else:
            errorNumber("ID", id_input)
            return 0
        
        name_input = input("Name: ")
        age_input = input("Age: ")
        if age_input.isdigit() == False: #check if age is not a integer
            errorNumber("Age", age_input)
            return 0
    
        person = person_types[type_input_index](id_input, name_input, age_input)
        people_dict[person.getId()] = person
        print("ID [" + str(person.getId()) + "] saved successfuly")
        return int(person.getAge())
              
    def searchByID(people_dict):
        if emptyDict(people_dict):
            return None
        id_search = input("Please enter the ID you want to look for: ")
        try:
            if id_search in people_dict:
                people_dict[id_search].printType()
                people_dict[id_search].printDetails()
            else:
                print("Error: ID " + id_search +" is not saved")
        except:
            errorNumber("ID", id_search)
            return

    def printAgesAverage(count, sum):
        if count == 0:
            print("There are no saved people on the list")
        else:
            result = sum / count
            print(result)

    def printAllNames(people_dict):
        emptyDict(people_dict)
        for index, id in enumerate(people_dict):
            print(str(index) + ". " + people_dict[id].getName())

    def printAllIDs(people_dict):
        emptyDict(people_dict)
        for index, id in enumerate(people_dict):
            print(str(index) + ". " + id)

    def printAllEntries(people_dict):
        emptyDict(people_dict)
        for index, id in enumerate(people_dict):
            print(str(index) + ". ")
            people_dict[id].printType()
            people_dict[id].printMySelf()
            
    def printEntryByIndex(people_dict):
        if emptyDict(people_dict):
            return None
        search_index = input("Please enter the index of the entry you want to print: ")
        try:
            if int(search_index) in range(len(people_dict)):
                for index, id in enumerate(people_dict):
                    if search_index == str(index):
                        people_dict[id].printType()
                        people_dict[id].printDetails()
                        break    
            else:
                print("Error: Index out of range. The minimum index allowed is 0" + 
                        "\nThe maximum index allowed is " + str(len(people_dict) - 1))
        except:
            errorNumber("index", search_index)

    def saveAllData(people_dict):
        if emptyDict(people_dict):
            return None
        file_name = input("What is your output file name? ")
        people_list = []
        for id in people_dict.keys():
            people_list.append(people_dict[id].getInfoDict())
        df = pd.DataFrame(people_list)
        close_file_flag = True
        while close_file_flag:
            try:
                df.to_csv("C:\\Users\\Tehila\\Desktop\\Easy High-Tech\\PYTHON\\3\\" + file_name + ".csv", index=False)
                print("The file " + file_name + " was saved successfully")
                close_file_flag = False
            except PermissionError:
                print("Error: The file '" + file_name + ".csv' is open")
                input("Please close the file and then press enter to continue")

    users_dict = {}
    user_choice = ""
    sum_ages = 0
    while True:
        flag_y = False
        flag_n = False
        for option in MenuOptions:
            print("To " + option.name + " please press " + str(option.value))
        user_choice = input("Please enter your choice: ")
        try:
            user_choice = MenuOptions(int(user_choice))
        except:
            print("Option [" + user_choice + "] does not exist. Please try again")  
            continue
        
        if user_choice == MenuOptions.SAVE_NEW_ENTRY:
            sum_ages += saveNewEntry(users_dict)
        elif user_choice == MenuOptions.SEARCH_ENTRY_BY_ID:
            searchByID(users_dict)
        elif user_choice == MenuOptions.PRINT_AVE_AGES:
            printAgesAverage(len(users_dict), sum_ages)
        elif user_choice == MenuOptions.PRINT_NAMES:
            printAllNames(users_dict)
        elif user_choice == MenuOptions.PRINT_IDS:
            printAllIDs(users_dict)
        elif user_choice == MenuOptions.PRINT_ALL_ENTRIES:
            printAllEntries(users_dict)
        elif user_choice == MenuOptions.PRINT_ENTRY_BY_INDEX:
            printEntryByIndex(users_dict)
        elif user_choice == MenuOptions.SAVE_DATA_TO_FILE:
            saveAllData(users_dict)
        elif user_choice == MenuOptions.EXIT:
            while True:
                answer = input("Are you sure? (y/n) ")
                if answer == "y":
                    print("Goodbye!")
                    flag_y = True
                    break
                elif answer == "n":
                    flag_n = True
                    break  
            
        if flag_y: #if the user want to exit
            break
        if flag_n: #if the user want to stay
            continue
        
        input("Press Enter to continue ")
except KeyboardInterrupt:
        print("\nGoodbye!")     