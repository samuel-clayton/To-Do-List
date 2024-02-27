import json, functions  # Importing necessary modules
from datetime import datetime  # Importing datetime module for handling dates

print("To-Do List Application")  # Printing application title

functions.list_commands()  # Calling function to list available commands
while True:  # Infinite loop for user interaction
    choice = input("><> ").lower()  # Prompting user for input and converting it to lowercase

    while choice == "":  # Loop to ensure non-empty input
        choice = input("><> ").lower()

    command = choice.split()[0]  # Extracting command from user input
    arguments = " ".join(choice.split()[1:])  # Extracting arguments from user input

    if command == "add" or command == "a":  # If command is add
        while arguments == "":  # Loop to ensure non-empty task name
            arguments = input("Please input a name for the task\n><> ")
        date = input("Please add a date as DD/MM/YYYY (leave blank for today)\n><> ")  # Prompting for date
        if date == "": date = datetime.today().strftime("%d/%m/%Y")  # Setting default date to today
        while not functions.is_valid_date(date):  # Loop until valid date is provided
            print("ValueError:",str(functions.is_valid_date(date)[1]).replace("%d/%m/%Y", "DD/MM/YY"))  # Error message for invalid date
            date = input("><> ")  # Prompting for date again
        
        time = input("Please add the deadline time in 24-hour clock format, if applicable\n><> ")  # Prompting for time
        while True:  # Loop for validating time
            result, error = functions.is_valid_time(time)  # Checking if time is valid
            if not result and time != "":  # If time is not valid and not empty
                print("ValueError:", str(error).replace("%H:%M", "HH:MM"))  # Error message for invalid time
                time = input("><> ")  # Prompting for time again
            else:
                break  # Exiting loop if time is valid

        functions.write_task(arguments, date, time)  # Calling function to add task to list

    elif command == "view" or command == "v":  # If command is view
        file_name = "tasks.json"  # Defining file name for task list
        try:  # Trying to open and read task list file
            with open(file_name, "r") as file:
                tasks = json.load(file)
        except:  # Handling case where no tasks are available
            print("There are no tasks!")
        else:  # If tasks are available
            task_number = 1
            for task in tasks:  # Looping through tasks to display them
                task_name = task["task"] 
                completed = task["completed"]
                due_date = task["due_date"]
                deadline_time = task["deadline_time"]

                if completed == True: completed = "Yes"
                elif completed == False: completed = "No"

                list = f"Task {task_number}: {task_name}\nCompleted: {completed}\nDue Date: {due_date}"
                if task_number == len(tasks):
                    if deadline_time != "": list += f"\n{deadline_time}"
                else:list += f"\n{deadline_time}"

                print(list)  # Printing task details
                task_number+=1
            print("-----------------------")

    elif command == "complete" or command == "c":  # If command is complete
        while not arguments.isdigit():  # Loop to ensure valid index input
            arguments = input("Please input a valid index\n><> ")

        file_name = "tasks.json"  # Defining file name for task list
        try:  # Trying to open and read task list file
            with open(file_name, "r") as file:
                tasks = json.load(file)
        except:  # Handling case where no tasks are available
            print("There are no tasks!")
        else:  # If tasks are available
            task_number = 1
            for task in tasks:  # Looping through tasks to mark selected task as complete
                task_name = task["task"]
                id = task["id"] 
                if task_number == int(id): 
                    task["completed"] = True
                    break
                task_number+=1
            with open(file_name, "w") as file:  # Writing updated task list to file
                json.dump(tasks, file, indent=4)
                print(f"Task: {task_name} has been marked as complete!\n-----------------------")
            
    elif command == "delete" or command == "d":  # If command is delete
        while not arguments.isdigit():  # Loop to ensure valid index input
            arguments = input("Please input a valid index\n><> ")

        file_name = "tasks.json"  # Defining file name for task list
        try:  # Trying to open and read task list file
            with open(file_name, "r") as file:
                tasks = json.load(file)
        except:  # Handling case where no tasks are available
            print("There are no tasks!")
        else:  # If tasks are available
            task_number = 1
            for task in tasks:  # Looping through tasks to delete selected task
                task_name = task["task"]
                id = task["id"] 
                if task_number == int(id): 
                    tasks.pop(id-1)
                    break
                task_number+=1
            with open(file_name, "w") as file:  # Writing updated task list to file
                json.dump(tasks, file, indent=4)
                print(f"Task: {task_name} has been deleted!\n-----------------------")

    elif command == "help" or command == "h" or command == "?":  # If command is help
        functions.list_commands()  # Calling function to display available commands
    elif command == "exit" or command == "e":  # If command is exit
        break  # Exiting the loop and terminating the program
