
# Simple To-Do List

tasks = []  # list of tasks

def show_tasks():
    if not tasks:
        print("No tasks yet!")
    else:
        print("\nCurrent tasks:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")

def add_task():
    task = input("Enter a new task: ")
    tasks.append(task)
    print(f"Task '{task}' added!")

def remove_task():
    show_tasks()
    if tasks:
        try:
            num = int(input("Enter the number of the task to remove: "))
            if 1 <= num <= len(tasks):
                removed = tasks.pop(num - 1)
                print(f"Task '{removed}' removed!")
            else:
                print("Invalid number.")
        except ValueError:
            print("Please enter a number.")

while True:
    print("\n--- To-Do List ---")
    print("1. Show tasks")
    print("2. Add task")
    print("3. Remove task")
    print("4. Exit")

    choice = input("Your choice: ")

    if choice == "1":
        show_tasks()
    elif choice == "2":
        add_task()
    elif choice == "3":
        remove_task()
    elif choice == "4":
        print("Exiting...")
        break
    else:
        print("Please choose a valid option.")