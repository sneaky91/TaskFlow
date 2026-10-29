## -----------------> TaskFlow <------------------------------ ##

#making json (start)

import json

try:
    with open("tasks.json", "r", encoding="utf-8") as file:
        tasks = json.load(file)
except FileNotFoundError:
    tasks = []

#making json (end)

# toggle tasks (start)

def toggle_task(tasks):
    try:
        number = int(input("Enter task number: "))

        if 1 <= number <= len(tasks):
            tasks[number - 1]["completed"] = not tasks[number - 1]["completed"]
            save_tasks(tasks)
            print("Task status updated")
        else:
            print("Invalid number")

    except ValueError:
        print("Please enter a valid number")

# Toggle tasks (end)

# SAVE TASKS (start)

def save_tasks(tasks):
    with open("tasks.json", "w", encoding="utf-8") as file:
        json.dump(tasks, file, indent=4, ensure_ascii=False)

# SAVE TASKS (end)

# SHOW MENU (start)

def show_menu():
    print("=====TaskFlow=====")
    print("1. Add task")
    print("2. show tasks")
    print("3. Remove task")
    print("4. Toggle task")
    print("5. Edit task")
    print("6. Show completed")
    print("7. Show Pending")
    print("8. Show statistics")
    print("9. Search tasks")
    print("10. Sort tasks")
    print("0. Exit")

# SHOW MENU (end)

# SHOW TASKS (start)

def show_tasks(tasks):
    for number, task in enumerate(tasks, start=1):
        if task["completed"]:
            status = "[x]"
        else:
            status = "[ ]"

        print(f'{number}. {status} {task["title"]}')

# SHOW TASKS (end)

# ADD TASKS (start)

def add_task(tasks):
    new_task = input("Enter new task: ").strip()
    if new_task == "":
        print("task cannot be empty")
        return
    tasks.append({
        "title": new_task,
        "completed": False
    })
    save_tasks(tasks)

# ADD TASKS (end)

# REMOVE TASKS (start)

def remove_task(tasks):
    try:
        rm_task = int(input("Enter task number: "))
        if 1 <= rm_task <= len(tasks):
            tasks.pop(rm_task - 1)
            save_tasks(tasks)
            print("Task removed")
        else:
            print("Invalid number")
    except ValueError:
        print('EBnuti? Please enter a valid number')

# REMOVE TASKS (end)

# EDIT TASKS (start)

def edit_task(tasks):
    try:
        number = int(input("Enter task number: "))

        if 1 <= number <= len(tasks):
            new_title = input("Enter new title: ").strip()

            if new_title == "":
                print("Task cannot be empty")
                return

            tasks[number - 1]["title"] = new_title
            save_tasks(tasks)
            print("Task updated")
        else:
            print("Invalid number")

    except ValueError:
        print("Please enter a valid number")

# EDIT TASKS (end)

# SHOWING COMPLITED and PENDING (start)

def show_completed(tasks):
    print("Completed tasks:")
    for task in tasks:
        if task["completed"]:
            print(task["title"])


def show_pending(tasks):
    print("Pending tasks:")
    for task in tasks:
        if not task["completed"]:
            print(task["title"])

# SHOWING COMPLITED and PENDING (end)


# Show statistics (start)

def show_statistics(tasks):
    total = len(tasks)
    completed = 0

    for task in tasks:
        if task["completed"]:
            completed += 1

    pending = total - completed

    print("Total tasks:", total)
    print("Completed tasks:", completed)
    print("Pending tasks:", pending)

# Show statistics (end)

#search tasks (start)

def search_tasks(tasks):
    search = input("Enter search term: ").strip().lower()
    found = 0
    if search == "":
        print("Search cannot be empty")
        return
    for task in tasks:
        if search in task["title"].lower():
            print(task["title"])
            found += 1

    print("Found tasks:", found)

#search tasks (end)

#sorting tasks (start)

def sort_tasks(tasks):
    sorted_tasks = sorted(tasks, key=lambda task: task["title"].lower())

    for task in sorted_tasks:
        print(task["title"])

#sorting tasks (end)


# While (starts)

while True:
    show_menu()

    task = input("Choose option: ")

    if task == "0":
        break
    elif task == "1":
        add_task(tasks)
    elif task == "2":
        show_tasks(tasks)
    elif task == "3":
        remove_task(tasks)
    elif task == "4":
        toggle_task(tasks)
    elif task == "5":
        edit_task(tasks)
    elif task == "6":
        show_completed(tasks)
    elif task == "7":
        show_pending(tasks)
    elif task == "8":
        show_statistics(tasks)
    elif task == "9":
        search_tasks(tasks)
    elif task == "10":
        sort_tasks(tasks)
    else:
        print("wrong option")

# While (end)