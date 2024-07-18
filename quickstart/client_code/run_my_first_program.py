# To-Do List Manager in Python

# Define the structure of a To-Do item using a class
class TodoItem:
    def __init__(self, id, task):
        self.id = id
        self.task = task
        self.completed = False

# Define the to-do list array
todo_list = []

# Function to add a new task to the list
def add_task(task):
    id = len(todo_list) + 1
    new_task = TodoItem(id, task)
    todo_list.append(new_task)
    print(f"Task added: {task}")

# Function to mark a task as completed
def complete_task(id):
    for item in todo_list:
        if item.id == id:
            item.completed = True
            print(f"Task completed: {item.task}")
            return
    print("Task not found.")

# Function to display all tasks
def display_tasks():
    print("To-Do List:")
    for item in todo_list:
        status = "Completed" if item.completed else "Pending"
        print(f"ID: {item.id} | Task: {item.task} | Status: {status}")

# Main program loop
while True:
    print("\nTo-Do List Manager")
    print("1. Add Task")
    print("2. Complete Task")
    print("3. Display Tasks")
    print("4. Exit")
    choice = int(input("Enter your choice: "))

    if choice == 1:
        task = input("Enter task description: ")
        add_task(task)
    elif choice == 2:
        id = int(input("Enter task ID to complete: "))
        complete_task(id)
    elif choice == 3:
        display_tasks()
    elif choice == 4:
        print("Exiting the program.")
        break
    else:
        print("Invalid choice. Please try again.")
