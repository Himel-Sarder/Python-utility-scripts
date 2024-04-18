from datetime import datetime

tasks = []


def add_task():
    name = input("Enter task name: ")
    date_str = input("Enter due date (YYYY-MM-DD): ")
    time_str = input("Enter due time (HH:MM): ")
    due_datetime = datetime.strptime(date_str + ' ' + time_str, '%Y-%m-%d %H:%M')
    tasks.append({'name': name, 'due_datetime': due_datetime})
    print("Task added successfully.")


def view_tasks():
    if tasks:
        print("Upcoming Tasks:")
        for idx, task in enumerate(tasks, start=1):
            print(f"{idx}. {task['name']} - Due: {task['due_datetime'].strftime('%Y-%m-%d %H:%M')}")
    else:
        print("No tasks found.")


# Add more functions for editing tasks, deleting tasks, and displaying notifications

def main():
    while True:
        print("\nOptions:")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            add_task()
        elif choice == '2':
            view_tasks()
        elif choice == '3':
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
