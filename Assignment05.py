# ------------------------------------------------------------------------ #
# Title: Assignment 05
# Description: Working with Dictionaries and Files
#              When the program starts, load each "row" of data
#              in "ToDoToDoList.txt" into a python Dictionary.
#              Add the each dictionary "row" to a python list "table"
# ChangeLog (Who,When,What):
# EGleixner, 2/15/2023, Script created, starter code imported.
# EGleixner, 2/15/2023, Step 1 written in scratch file, transferred to this script
# EGleixner, 2/15/2023, Step 2-7 added
# EGleixner, 2/15/2023, test and refine.

# ------------------------------------------------------------------------ #

# -- Data -- #
# declare variables and constants
objFile = "ToDoList.txt"   # An object that represents a file
strData = ""  # A row of text data from the file
dicRow = {}    # A row of data separated into elements of a dictionary {Task,Priority}
lstTable = []  # A list that acts as a 'table' of rows
strMenu = ""   # A menu of user options
strChoice = ""  # A Capture the user option selection


# -- Processing -- #
# Step 1 - When the program starts, load the any data you have
# in a text file called ToDoList.txt into a python list of dictionaries rows (like Lab 5-2)

objFile = open("ToDoList.txt","a") # Create and Open txt file
dicRow = {"Task":"Sample Task", "Priority":"H/M/L"} # Add Sample Entry
lstTable = [dicRow]
for row in dicRow:
    objFile.write(dicRow["Task"] + ", " + dicRow["Priority"] + "\n") # write entry to file
objFile.close()


# -- Input/Output -- #
# Step 2 - Display a menu of choices to the user
while (True):
    print("""
    Menu of Options
    1) Show current data
    2) Add a new item.
    3) Remove an existing item.
    4) Save Data to File
    5) Exit Program
    """)
    strChoice = str(input("Which option would you like to perform? [1 to 5] - "))
    print()  # adding a new line for looks

    # Step 3 - Show the current items in the table
    if (strChoice.strip() == '1'):
        print("Tasks \t Priority Level.")
        for row in lstTable:
            print(row["Task"] + "," + row["Priority"])

        continue

    # Step 4 - Add a new item to the list/Table using function
    elif (strChoice.strip() == '2'):
        dicRow = {"Task":input("Submit next task: "),
                  "Priority":input("List priority of task as (H)igh/(M)edium/(L)ow: ")} # immediately store user input
        lstTable.append(dicRow)
        print("New task item added to list. \n")
        continue

    # Step 5 - Remove a new item from the list/Table
    elif (strChoice.strip() == '3'):
        strKeyToRemove = input("Which task would you like removed? -")
        blnItemRemoved = False  # use this to verify that the data was found and removed
        for row in lstTable:
            Task, Priority = dict(row).values()
            if Task == strKeyToRemove:
                lstTable.remove(row)
                blnItemRemoved = True

            if blnItemRemoved == True:  # Update user on the status
                print("The task was removed. \n")
            else:
                print("Task not found. Please try again.")

            print("Current Task List")  # show the current items in the table
            for row in lstTable:
                print(row["Task"] + "," + row["Priority"])
        continue

    # Step 6 - Save tasks to the ToDoToDoList.txt file
    elif (strChoice.strip() == '4'):
        objFile = open("ToDoList.txt","w")
        for row in lstTable:
            objFile.write(dicRow["Task"] + "," + dicRow["Priority"] + "\n")
        objFile.close()
        print("File Saved.")
        continue

    # Step 7 - Exit program
    elif (strChoice.strip() == '5'):
        print("Exiting program....")
        break  # and Exit the program