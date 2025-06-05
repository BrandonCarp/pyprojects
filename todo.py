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
        json.dump({str(k): v for k, v in task_list.items()}, f)


# Load tasks at startup
task_list = load_tasks()

def handle_view():
    if not task_list:
        print("No tasks.")
    else:
        for tid, desc in task_list.items():
            print(f"[{tid}] {desc}")

   


def handle_add():
    new_key = max(task_list.keys(), default=-1) + 1
    task_list[new_key] = questionary.text("Enter task description:").ask()
    print(f"Added task {new_key}: {task_list[new_key]}")
    save_tasks()
    handle_view()

def handle_delete():
    handle_view()
    try:
        task_id = int(questionary.text("Enter task ID to delete:").ask())
    except ValueError:
        print("Invalid input. Please enter a number.")
        return
    if task_id in task_list:
        del task_list[task_id]
        print(f"Deleted task {task_id}")
        save_tasks()
        handle_view()
    else:
        print("Invalid ID")

def handle_edit():
    print(task_list.keys())
    task_id = int(questionary.text("Enter task ID to edit:").ask())
    if task_id in task_list:
        new_task = questionary.text("Enter new task description:").ask()
        task_list[task_id] = new_task
        print(f"Updated task {task_id}: {new_task}")
        save_tasks()
        handle_view()
    else:
        print("Invalid ID")

def handle_exit():
    save_tasks()
    print("Changes saved. Exiting...")
    return True

    

option_handlers = {
    "View": handle_view,
    "Add": handle_add,
    "Delete": handle_delete,
    "Edit": handle_edit,
    "Exit": handle_exit
}



def user_todo():
    option_list()
    


def option_list():
    while True:
        choice = questionary.select(
            "What do you want to do?",
            choices=list(option_handlers.keys())
        ).ask()

        handler = option_handlers.get(choice)

        if handler:
            if handler == handle_exit:
                handler()     
                break         
            else:
                handler()
        else:
            print("Invalid choice")
  


user_todo()