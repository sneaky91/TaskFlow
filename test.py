# with open("tasks.txt", 'w') as file:
#    file.write()

# with open("tasks.txt", 'w') as file:
#    file.write(input("New task"))

## --> TASKFLOW TEST OF SAVING TASKS <--  ##

# new_task = input("New task: ")

# with open("tasks.txt", "a") as file:
#    file.write(new_task + '\n')


# with open("tasks.txt", "r") as file:
#    tasks = file.read().splitlines()


# for number, task in enumerate(tasks, start=1):
#    print(f"{number}. {task}")

## --> TaskFlow compliting tasks test <-- ##

# task = {
#    "title": "Learn Python",
#    "completed": False
# }

# Name Print

# print(task["title"])

# Зміни статус

# task["completed"] = True


# print(task["completed"])

# tasks = []

# def show_tasks(tasks):
# for number, task in enumerate(tasks, start=1):
# if task["completed"]:
# status = "[x]"
# else:
# status = "[ ]"

# print(f'{number}. {status} {task["title"]}')

# def add_task(tasks):
# new_task = input("Enter new task: ").strip()
# if new_task == "":
# print("Task cannot be empty")
# return

# tasks.append({
# "title": new_task,
# "completed": False
#    })

# def toggle_task(tasks):

# try:
# number = int(input("Enter task number: "))

# if 1 <= number <= len(tasks):
# tasks[number - 1]["completed"] = not tasks[number - 1]["completed"]
# print("Task status updated")
# else:
# print("Invalid number")
# except ValueError:
# print("Please enter a valid number")


# add_task(tasks)
# add_task(tasks)

# show_tasks(tasks)

# toggle_task(tasks)

# show_tasks(tasks)

# -----------> testing only completed tasks <-----------#

##tasks = [
# {"title": "Python", "completed": True},
# {"title": "Gym", "completed": False},
# {"title": "School", "completed": False}
# ]

# print("Completed tasks:")

# Тут напиши цикл, який показує тільки виконані
# for task in tasks:
# if task["completed"]:
# print(task["title"])


# print("Pending tasks:")

# for task in tasks:
# i#f not task["completed"]:
# p#rint(task["title"])
# Тут напиши цикл, який показує тільки невиконані

# for formation test #
## -----------------> TaskFlow <------------------------------ ##
# import json

# try:
#    with open("tasks.json", "r", encoding="utf-8") as file:
#        tasks = json.load(file)
# except FileNotFoundError:
#    tasks = []
#
#
# test start #working stable :)
#
# def toggle_task(tasks):
#    try:
#        number = int(input("Enter task number: "))
#
#       if 1 <= number <= len(tasks):
#            tasks[number - 1]["completed"] = not tasks[number - 1]["completed"]
#            save_tasks(tasks)
#            print("Task status updated")
#        else:
#            print("Invalid number")
#
#  except ValueError:
#        print("Please enter a valid number")
##
#
# test end # stable
#
# def save_tasks(tasks):
#    with open("tasks.json", "w", encoding="utf-8") as file:
#        json.dump(tasks, file, indent=4, ensure_ascii=False)
#
#
# def show_menu():
# print("=====TaskFlow=====")
# print("1. Add task")
# print("2. show tasks")
#   print("3. Remove task")
#    print("4. Toggle task")
#   print("5. Edit task")
#   print("6. Show completed")
#    print("7. Show Pending")
#    print("0. Exit")
###############


# def show_tasks(tasks):
#    for number, task in enumerate(tasks, start=1):
#        if task["completed"]:
#           status = "[x]"
#       else:
#           status = "[ ]"

#        print(f'{number}. {status} {task["title"]}')


# def add_task(tasks):
# new_task = input("Enter new task: ").strip()
# if new_task == "":
# print("task cannot be empty")
# return
# tasks.append({
# "title": new_task,
# "completed": False
# })
# save_tasks(tasks)


# def remove_task(tasks):
# try:
# rm_task = int(input("Enter task number: "))
# if 1 <= rm_task <= len(tasks):
# tasks.pop(rm_task - 1)
# save_tasks(tasks)
# print("Task removed")
# else:
# print("Invalid number")
# except ValueError:
# print('EBnuti? Please enter a valid number')


# def edit_task(tasks):
# try:
# number = int(input("Enter task number: "))

# if 1 <= number <= len(tasks):
##new_title = input("Enter new title: ").strip()

# if new_title == "":
# print("Task cannot be empty")
# return

# tasks[number - 1]["title"] = new_title
# save_tasks(tasks)
# print("Task updated")
# else:
# print("Invalid number")

# except ValueError:
# print("Please enter a valid number")


# def show_completed(tasks):
# print("Completed tasks:")
# for task in tasks:
# if task["completed"]:
# print(task["title"])


# def show_pending(tasks):
# print("Pending tasks:")
# for task in tasks:
# if not task["completed"]:
# print(task["title"])


# while True:
# show_menu()

# task = input("Choose option: ")

# if task == "0":
# break
# elif task == "1":
# add_task(tasks)
# elif task == "2":
# show_tasks(tasks)
# elif task == "3":
# remove_task(tasks)
# elif task == "4":
# toggle_task(tasks)
# elif task == "5":
# edit_task(tasks)
# elif task == "6":
# show_completed(tasks)
# elif task == "7":
# show_pending(tasks)
# else:
# print("wrong option")


# --------> Search <---------#

#tasks = [
#    {"title": "Learn Python", "completed": False},
#    {"title": "Go to gym", "completed": True},
 #   {"title": "Python homework", "completed": False}
#]

#search = input("Search: ").lower()
#found = 0

#for task in tasks:
#    if search in task["title"].lower():
#        print(task["title"])
#        found += 1

#print("Found tasks:", found)

# ------> Sort <------#

tasks = [
    {"title": "Python", "completed": False},
    {"title": "Gym", "completed": True},
    {"title": "School", "completed": False},
    {"title": "Homework", "completed": False}
]

sorted_tasks = sorted(tasks, key=lambda task: task["title"], reverse=True)


# ТУТ ТВІЙ КОД
for task in sorted_tasks:
    print(task["title"])
