import os

FILE_NAME = "tasks.txt"

def load_tasks():
    if not os.path.exists(FILE_NAME):
        return []
    with open(FILE_NAME, "r") as file:
        return file.read().splitlines()

def save_tasks(tasks):
    with open(FILE_NAME, "w") as file:
        for task in tasks:
            file.write(task + "\n")

def show_tasks(tasks):
    if not tasks:
        print("No tasks found.")
        return
    print("\nYour Tasks:")
    for i, task in enumerate(tasks, 1):
        print(f"{i}. {task}")

def add_task(tasks):
    task = input("Enter new task: ")
    tasks.append(task)
    save_tasks(tasks)
    print("Task added successfully!")

def remove_task(tasks):
    show_tasks(tasks)
    try:
        index = int(input("Enter task number to remove: ")) - 1
        removed = tasks.pop(index)
        save_tasks(tasks)
        print(f"Removed task: {removed}")
    except (ValueError, IndexError):
        print("Invalid selection.")

def main():
    tasks = load_tasks()

    while True:
        print("\nTask Manager")
        print("1 - Show tasks")
        print("2 - Add task")
        print("3 - Remove task")
        print("4 - Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            show_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            remove_task(tasks)
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid option.")

if __name__ == "__main__":
    main()
