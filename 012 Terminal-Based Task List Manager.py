"""
 Challenge: Terminal-Based Task List Manager

Create a Python script that lets users manage a to-do list directly from the terminal.

Your program should:
1. Allow users to:
   - Add a task
   - View all tasks
   - Mark a task as completed
   - Delete a task
   - Exit the app
2. Save all tasks in a text file named `tasks.txt` so data persists between runs.
3. Display tasks with an index number and a ✔ if completed.

Example menu:
1. Add Task
2. View Tasks
3. Mark Task as Completed
4. Delete Task
5. Exit

Example output:
Your Tasks:

Buy groceries||not_done
Finish Python project||done
Read a || book||not_done


Bonus:
- Prevent empty tasks from being added
- Validate task numbers before completing/deleting
"""

from pathlib import Path

TASK_FILE = Path(__file__).with_name("tasks.txt")


def load_tasks():
    tasks = []
    if TASK_FILE.exists():
        with TASK_FILE.open("r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if not line or "||" not in line:
                    continue  # skip malformed rows
                text, status = line.rsplit("||", 1)
                tasks.append({"text": text.strip(), "done": status == "done"})
    return tasks


def save_tasks(tasks):
    with TASK_FILE.open("w", encoding="utf-8") as f:
        for task in tasks:
            status = "done" if task["done"] else "not_done"
            f.write(f"{task['text']}||{status}\n")


def display_tasks(tasks):
    if not tasks:
        print("No tasks found.")
        return

    for i, task in enumerate(tasks, 1):
        checkbox = "x" if task["done"] else " "
        print(f"{i}. [{checkbox}] {task['text']}")
    print()


def prompt_task_text():
    text = input("Enter your task: ").strip()
    while not text:
        print("Task cannot be empty. Try again.")
        text = input("Enter your task: ").strip()
    return text


def prompt_task_number(tasks, action):
    if not tasks:
        print("No tasks to select.")
        return None

    display_tasks(tasks)
    raw = input(f"Enter task number to {action}: ").strip()
    if not raw.isdigit():
        print("Please enter a valid number.")
        return None

    num = int(raw)
    if 1 <= num <= len(tasks):
        return num - 1

    print("Invalid task number.")
    return None


def add_task(tasks):
    text = prompt_task_text()
    tasks.append({"text": text, "done": False})
    save_tasks(tasks)
    print("Task added.")


def mark_task(tasks):
    idx = prompt_task_number(tasks, "toggle")
    if idx is None:
        return

    tasks[idx]["done"] = not tasks[idx]["done"]
    save_tasks(tasks)
    status = "DONE" if tasks[idx]["done"] else "NOT DONE"
    print(f"Task marked as {status}.")


def delete_task(tasks):
    idx = prompt_task_number(tasks, "delete")
    if idx is None:
        return

    removed = tasks.pop(idx)
    save_tasks(tasks)
    print(f"Removed: {removed['text']}")


def task_manager():
    tasks = load_tasks()

    menu = (
        "\n------ Task List Manager ------\n"
        "1. Add Task\n"
        "2. View Tasks\n"
        "3. Toggle Task Complete\n"
        "4. Delete Task\n"
        "5. Exit\n"
    )

    while True:
        print(menu)
        choice = input("Choose an option (1-5): ").strip()

        match choice:
            case "1":
                add_task(tasks)
            case "2":
                display_tasks(tasks)
            case "3":
                mark_task(tasks)
            case "4":
                delete_task(tasks)
            case "5":
                print("Exiting Task Manager.")
                break
            case _:
                print("Please choose a valid option (1-5).")


if __name__ == "__main__":
    task_manager()
