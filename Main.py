# TO-DO LIST APPLICATION. Follow the Comments to understand how things work.

# Created by JaVion Briscoe a 2nd Year Computer Science Student at the University of Missouri Kansas City

# CS101 Intro to Programming I

import json 
import time 
import os 


def load_tasks(): # This function loads the task automatically if JSON fails to a DEcodeError or a FileNotFoundError
    try:
        with open("tasks.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        return []


def save_tasks(tasks): # This function saves the task using JavaScript Object Notation (JSON)
    print("Saving to: ", os.path.abspath("tasks.json"))
    with open("tasks.json", "w") as file:
        json.dump(tasks, file, indent=4)
        
    print("\nTask Successfully Saved!")
        

def view_tasks(tasks): # This function allows the user to view all the task they have.
    print("\n===== YOUR TASK =====")

    if not tasks:
        print("\nNo task here in your list :D")
    

    for task in tasks:
        if task["completed"]:
            check = "100%"
        else:
            check = "0%"
            

        print(f'{task["id"]}. [{check}] {task["task"]}')

def add_task(tasks): # This function adds a new task for the user.
    task_name = input("Enter a new task: ")

    if tasks:
        new_task_id = max(task["id"] for task in tasks) + 1 
    else:
        new_task_id = 1 

    new_task = {"id": new_task_id, "task": task_name, "completed": False}

    tasks.append(new_task)

    save_tasks(tasks)

    print("\nSuccessfully added a new Task!")



def complete_task(tasks): # This function completes the user task showing them they reached %100 on the task.
    while True:
        try:
            task_id = int(input("\nEnter Task ID to complete: "))
            if task_id <=0:
                print("\nInvalid ID! Needs to be greater than 0. Please try again.")
            else:

                found = False

                for task in tasks:
                    if task["id"] == task_id:
                        task["completed"] = True
                        found = True
                        break
                if found:
                    print("Completing Task...")
                    time.sleep(5)
                    break
                else:
                    print("\nNo task here to complete :D")
                    break
                            
        except ValueError:
            print("\nPlease enter an integer not a string!")
    


def delete_task(tasks): # This function allows the users to delete and remove the task they have.
    while True:
        try:
            task_id = int(input("Enter Task ID delete: "))
            if task_id <=0:
                print("\nInvalid ID! Needs to be greater than 0. Please try again.")
            else:
                found = False
                for task in tasks:
                    if task["id"] == task_id:
                        tasks.remove(task)
                        found = True
                        break
                if found:
                    print("Deleting task from the list...")
                    time.sleep(5)
                    print("\nTask Deleted!")
                    break
                else:
                    print("\nNo task here to delete :D")
                    break
                            
        except ValueError:
            print("\nPlease enter an integer not a string!")

def display_menu(): # Menu that displays what the users can choose. 
    print("\n===== TO-DO LIST APPLICATION =====")
    print("1. Save Task (Just to be safe.)")
    print("2. View Task")
    print("3. Add Task")
    print("4. Complete Task")
    print("5. Delete Task")
    print("6. Exit")

    print("\n*Task automatically get saved but can use the save option to hardcode save it.*")

def main(): # Main function

    tasks = load_tasks()

    while True:
        display_menu()

        try:
            choice = int(input("\nPick an Option: "))
            if choice <=0 or choice > 6:
                print("\nINVALID OPTION! Please choose a number between (1-6)")
            elif choice == 1:
                save_tasks(tasks)
            elif choice == 2:
                view_tasks(tasks)
            elif choice == 3:
                add_task(tasks)
            elif choice == 4:
                complete_task(tasks)
            elif choice == 5:
                delete_task(tasks)
            elif choice == 6:
                print("Goodbye! :D")
                break
        except ValueError:
            print("\nPlease enter only integers not characters, strings, etc!")
main()

            


