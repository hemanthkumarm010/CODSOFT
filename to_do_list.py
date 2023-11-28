import os
import json

# File to store the to-do list data
TODO_FILE = "todo.json"

def load_todo():
    """Load existing to-do list from file."""
    if os.path.exists(TODO_FILE):
        with open(TODO_FILE, "r") as file:
            return json.load(file)
    return {}

def save_todo(todo):
    """Save to-do list to file."""
    with open(TODO_FILE, "w") as file:
        json.dump(todo, file)

def display_todo(todo):
    """Display the current to-do list."""
    print("To-Do List:")
    if not todo:
        print("No tasks.")
    else:
        for task, status in todo.items():
            print(f"[{'X' if status else ' '}] {task}")

def add_task(todo, task):
    """Add a new task to the to-do list."""
    todo[task] = False
    print(f"Task '{task}' added to the to-do list.")

def update_task(todo, task, status):
    """Update the status of a task."""
    if task in todo:
        todo[task] = status
        print(f"Task '{task}' marked as {'done' if status else 'not done'}.")
    else:
        print(f"Task '{task}' not found in the to-do list.")

def update_description(todo, task, new_description):
    """Update the description of a task."""
    if task in todo:
        todo[new_description] = todo.pop(task)
        print(f"Task '{task}' description updated to '{new_description}'.")
    else:
        print(f"Task '{task}' not found in the to-do list.")

def main():
    """Main function to run the to-do list application."""
    todo = load_todo()

    while True:
        print("\n1. Display To-Do List")
        print("2. Add Task")
        print("3. Mark Task as Done")
        print("4. Update Task Description")
        print("5. Quit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            display_todo(todo)
        elif choice == "2":
            task = input("Enter the task to add: ")
            add_task(todo, task)
        elif choice == "3":
            task = input("Enter the task to mark as done: ")
            update_task(todo, task, True)
        elif choice == "4":
            task = input("Enter the task to update: ")
            new_description = input("Enter the new description: ")
            update_description(todo, task, new_description)
        elif choice == "5":
            save_todo(todo)
            print("Exiting the to-do list application. Your to-do list has been saved.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()
