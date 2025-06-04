# Description: Create a command-line or simple GUI to-do list app that allows the user to add, remove, and update tasks. This project will help with working with lists and user input.




import json
import os
import questionary


FILENAME = "tasks.json"

def load_tasks():
    if os.path.exists(FILENAME):
        with open(FILENAME, "r") as f:
            return {int(k): v for k, v in json.load(f).items()}  # Convert keys back to int
    return {}

def save_tasks():
    with open(FILENAME, "w") as f:
        json.dump(task_list, f)

# Load tasks at startup
task_list = load_tasks()

def handle_view():
    if not task_list:
        print("No tasks.")
    else:
        for tid, desc in task_list.items():
            print(f"[{tid}] {desc}")

    option_handlers["View"] = handle_view


def handle_add():
    new_key = max(task_list.keys(), default=-1) + 1
    task_list[new_key] = questionary.text("Enter task description:").ask()
    print(f"Added task {new_key}: {task_list[new_key]}")

def handle_delete():
    task_id = int(questionary.text("Enter task ID to delete:").ask())
    if task_id in task_list:
        del task_list[task_id]
        print(f"Deleted task {task_id}")
    else:
        print("Invalid ID")

def handle_edit():
    print(task_list.keys())
    task_id = int(questionary.text("Enter task ID to edit:").ask())
    if task_id in task_list:
        new_task = questionary.text("Enter new task description:").ask()
        task_list[task_id] = new_task
        print(f"Updated task {task_id}: {new_task}")
    else:
        print("Invalid ID")

def handle_exit():
    print("You selected Exit")

option_handlers = {
    "View": handle_view,
    "Add": handle_add,
    "Delete": handle_delete,
    "Edit": handle_edit,
    "Exit": handle_exit
}



def user_todo():
    # option = input("What would you like to do ?")
    option_list()
    


def option_list():
    choice = questionary.select(
        "What do you want to do?",
        choices=list(option_handlers.keys())
    ).ask()

    handler = option_handlers.get(choice)
    if handler:
        handler()
    else:
        print("Invalid choice")




user_todo()