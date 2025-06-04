# Description: Create a command-line or simple GUI to-do list app that allows the user to add, remove, and update tasks. This project will help with working with lists and user input.





import questionary

task_list = {}  # Dictionary for task storage

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