import json
import os

FILE_NAME = "tasks.json"


def load_tasks():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    return []


def save_tasks(tasks):
    with open(FILE_NAME, "w") as file:
        json.dump(tasks, file, indent=4)


def add_task(tasks):
    subject = input("Enter subject: ")
    task = input("Enter task: ")
    deadline = input("Enter deadline (DD-MM-YYYY): ")

    new_task = {
        "subject": subject,
        "task": task,
        "deadline": deadline,
        "completed": False
    }

    tasks.append(new_task)
    save_tasks(tasks)
    print("Task added successfully!")


def view_tasks(tasks):
    if not tasks:
        print("No tasks available.")
        return

    for index, task in enumerate(tasks, start=1):
        status = "Completed" if task["completed"] else "Pending"

        print(f"\n{index}. {task['task']}")
        print(f"Subject: {task['subject']}")
        print(f"Deadline: {task['deadline']}")
        print(f"Status: {status}")


def main():
    tasks = load_tasks()

    while True:
        print("\n===== SMART STUDY PLANNER =====")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()
