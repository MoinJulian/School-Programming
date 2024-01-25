import json

def print_menu():
    print("1. View To-Do List")
    print("2. Add Task")
    print("3. Remove Task")
    print("4. Save and Quit")

def view_todo_list(todo_list):
    print("\n--- To-Do List ---")
    for index, task in enumerate(todo_list, start=1):
        print(f"{index}. {task}")
    print()

def add_task(todo_list):
    task = input("Enter the task: ")
    todo_list.append(task)
    print(f"Task '{task}' added to the list.")

def remove_task(todo_list):
    view_todo_list(todo_list)
    try:
        task_index = int(input("Enter the task number to remove: "))
        removed_task = todo_list.pop(task_index - 1)
        print(f"Task '{removed_task}' removed from the list.")
    except (IndexError, ValueError):
        print("Invalid input. Please enter a valid task number.")

def save_and_quit(todo_list):
    with open("todo_list.json", "w") as file:
        json.dump(todo_list, file)
    print("To-Do List saved. Exiting program.")

def main():
    try:
        with open("todo_list.json", "r") as file:
            todo_list = json.load(file)
    except FileNotFoundError:
        todo_list = []

    while True:
        print_menu()
        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            view_todo_list(todo_list)
        elif choice == "2":
            add_task(todo_list)
        elif choice == "3":
            remove_task(todo_list)
        elif choice == "4":
            save_and_quit(todo_list)
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()
