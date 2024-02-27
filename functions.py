from colorama import init, Fore  # Importing necessary modules for colored output
import json  # Importing json module for JSON operations
from datetime import datetime  # Importing datetime module for date and time handling

def list_commands():
    """
    Function to display available commands.
    """
    print("-----------------------\nCommands:")  # Printing commands header
    print(f"- {Fore.MAGENTA}add", end=" ")  # Printing add command
    print(f"{Fore.BLUE}<task_description>", end= "")  # Printing add command description
    print(": Add a new task to the list")  # Printing add command explanation

    print(f"- {Fore.MAGENTA}view", end="")  # Printing view command
    print(": View all tasks")  # Printing view command explanation

    print(f"- {Fore.MAGENTA}complete", end=" ")  # Printing complete command
    print(f"{Fore.BLUE}<task_index>", end= "")  # Printing complete command description
    print(": Mark task as completed")  # Printing complete command explanation

    print(f"- {Fore.MAGENTA}delete", end=" ")  # Printing delete command
    print(f"{Fore.BLUE}<task_index>", end= "")  # Printing delete command description
    print(": Delete a task")  # Printing delete command explanation

    print(f"- {Fore.MAGENTA}help", end="")  # Printing help command
    print(": Show available commands")  # Printing help command explanation

    print(f"- {Fore.MAGENTA}exit", end="")  # Printing exit command
    print(": Exit the application")  # Printing exit command explanation

    print("-----------------------")  # Printing commands footer

def write_task(arguments, date, time):
    """
    Function to write a task to the task list.
    Args:
        arguments (str): Description of the task.
        date (str): Due date of the task (format: DD/MM/YYYY).
        time (str): Deadline time of the task (format: HH:MM).
    """
    file_name = "tasks.json"  # Defining file name for task list
    
    try:  # Trying to read existing task list file
        with open(file_name, 'r') as file:
            tasks = json.load(file)
    except:  # Handling case where no task list exists
        tasks = []
      
    for task in tasks:  # Looping through tasks to get the latest task id
        id = task["id"]
    if "id" not in locals(): id = 0  # If no tasks exist, setting id to 0

    tasks.append({  # Appending new task to task list
        "id": id+1,
        "task": arguments,
        "due_date": date,
        "deadline_time": time,
        "completed": False
    })

    try:  # Trying to write updated task list to file
        with open(file_name, 'w') as file:
            json.dump(tasks, file, indent=4)  # Writing JSON data to file
        print(f"Data was successfully written to {file_name}\n-----------------------")  # Success message
    except Exception as e:  # Handling write errors
        print("Error:", e)  # Printing error message

def is_valid_date(date):
    """
    Function to validate date format.
    Args:
        date (str): Date string to validate (format: DD/MM/YYYY).
    Returns:
        bool: True if date is valid, False otherwise.
        str: Error message if date is invalid.
    """
    try:
        datetime.strptime(date, "%d/%m/%Y")  # Parsing date string
        return True, None  # Returning True if date is valid
    except ValueError as e:  # Handling invalid date format
        return False, e  # Returning False and error message

def is_valid_time(time):
    """
    Function to validate time format.
    Args:
        time (str): Time string to validate (format: HH:MM).
    Returns:
        bool: True if time is valid, False otherwise.
        str: Error message if time is invalid.
    """
    try:
        datetime.strptime(time, "%H:%M")  # Parsing time string
        return True, None  # Returning True if time is valid
    except ValueError as e:  # Handling invalid time format
        return False, e  # Returning False and error message
