# ✅ TaskFlow

**TaskFlow** is a simple command-line task manager built with Python. It helps users organize daily tasks, track their progress, and manage priorities.

This project was created as part of my Python learning journey to practice core programming concepts and working with JSON files.

## ✨ Features

- **Add tasks** — Create tasks with a title and priority.
- **View tasks** — Display all tasks with their completion status.
- **Remove tasks** — Delete tasks by their number.
- **Edit tasks** — Update existing task titles.
- **Toggle completion** — Mark tasks as completed or pending.
- **Filter tasks** — View completed and pending tasks separately.
- **Statistics** — See total, completed, and pending task counts.
- **Search** — Find tasks by keywords.
- **Sort alphabetically** — Sort tasks by title.
- **Sort by priority** — Display High-priority tasks first.
- **JSON storage** — Automatically save tasks between sessions.

## 🛠️ Tech Stack

- **Python 3**
- **JSON** — Local data storage
- **Python Standard Library** — No external dependencies

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/TaskFlow.git
cd TaskFlow
```

### 2. Run the application

Make sure Python 3 is installed.

```bash
python main.py
```

On some systems, use:

```bash
python3 main.py
```

*Replace `main.py` with your actual Python filename if it is different.*

## 💻 Example Usage

When you launch TaskFlow, you will see:

```text
=====TaskFlow=====
1. Add task
2. Show tasks
3. Remove task
4. Toggle task
5. Edit task
6. Show completed
7. Show pending
8. Show statistics
9. Search tasks
10. Sort tasks
11. Sort by priority
0. Exit
```

### Adding a task

```text
Choose option: 1
Enter new task: Learn Python
Enter priority (Low/Medium/High): high
```

### Viewing tasks

```text
Choose option: 2

1. [ ] Learn Python | High
2. [x] Finish homework | Medium
3. [ ] Read a book | Low
```

### Sorting by priority

```text
Choose option: 11

Learn Python | High
Finish homework | Medium
Read a book | Low
```

## 📂 Project Structure

```text
TaskFlow/
├── main.py
├── tasks.json
└── README.md
```

- `main.py` — Main application logic.
- `tasks.json` — Stores tasks locally.
- `README.md` — Project documentation.

The `tasks.json` file is created when tasks are first saved.

## 💾 Data Storage

TaskFlow stores tasks in JSON format:

```json
[
    {
        "title": "Learn Python",
        "completed": false,
        "priority": "High"
    },
    {
        "title": "Read a book",
        "completed": true,
        "priority": "Low"
    }
]
```

Supported priorities:

- `High` — Important tasks
- `Medium` — Normal tasks
- `Low` — Less urgent tasks

Older tasks without a priority are treated as `Medium`.

## 🧠 What I Learned

During development, I practiced:

- Python functions and loops
- Conditional statements
- Lists and dictionaries
- File handling and JSON
- Exception handling
- Searching and filtering data
- Sorting with `sorted()` and `lambda`
- Organizing a command-line application

## 🗺️ Roadmap

Future improvements:

- [ ] Task deadlines
- [ ] Task categories
- [ ] Better error handling
- [ ] Code refactoring
- [ ] Object-oriented programming (OOP)
- [ ] Automated tests with pytest

## 👨‍💻 Author

Created by [**sneaky91**](https://github.com/sneaky91) .

---

⭐ If you find this project useful, consider giving it a star!
