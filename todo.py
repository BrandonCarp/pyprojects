# Description: Create a command-line or simple GUI to-do list app that allows the user to add, remove, and update tasks. This project will help with working with lists and user input.




# Also, list_handler is defined after the function handle_add(), so when Python hits that function, it doesn't yet know what list_handler is.

# 🤔 Here's how you can think about it:
# If you want to store tasks with a simple number as the key (like an auto-incrementing ID), how would you find the next available number?

# Since list_handler is a dictionary, how do you assign a new key-value pair to it?

# How will you let the functions access list_handler if it’s defined outside them?

# You’re on the right track—just need to think through how that data flows and how to add to a dictionary the proper way. Wanna try fixing that handle_add() with those hints, or need a little more nudge?

import questionary

list_handler = {
 
}


def handle_add():
    list_handler.update({"Task": input("Add Task"), "Completation Status": "TBD"})
    print(list_handler[{0}])

def handle_delete():
    print("list_handler")
    print("You selected Delete")

def handle_edit():
    print("You selected Edit")

def handle_exit():
    print("You selected Exit")

option_handlers = {
    "Add": handle_add,
    "Delete": handle_delete,
    "Edit": handle_edit,
    "Exit": handle_exit
}



def userTodo():
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





userTodo()