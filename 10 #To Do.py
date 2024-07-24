from datetime import datetime



class Task: # use of object to be more clean and readable
    def __init__(self, name, due_date, date_time, tasks):
        self.name = name
        self.date = due_date
        self.time = date_time
        tasks.append(self)
        


def add_task(tasks):
    try:
        name = str(input("Enter task name: "))
        date_str = str(input("Enter due date (YYYY-MM-DD): "))
        time_str = str(input("Enter due time (HH:MM): "))
        due_datetime = datetime.strptime(date_str + ' ' + time_str, '%Y-%m-%d %H:%M')
        Task(name, date_str, time_str, tasks)
        print("Task added successfully.")
    except:
        print("Wrong format please use the specified format.")
        add_task()

def delete_tasks(tasks):
    try:
        index = int(input("Which task do you want to delete ? (ex : 3)"))
        tasks.pop(index)
        print("Tasks deleted succefully")
    except:
        print("Wrong format please use the specified format.")
        delete_tasks(tasks)

def view_tasks(tasks):
    try:
        if tasks:
            for idx in range(len(tasks)):
                print(f'{idx}. name : {tasks[idx].name}\ndue to : {tasks[idx].date} at {tasks[idx].time}.\n')
        else:
            print("No tasks were found")
    except Exception as e:
        print("unwanted behavior : ", e)

        


def edit_task(tasks):
    try:
        index = int(input("Which task do you want to edit ? (ex : 3)\n"))
        info = str(input("Which info do you want to change ?\n- name\n- date\n- time\n"))
        if info not in ["name", "date", "time"]:
            print("invalid attributes, try again.")
            edit_task()
        else:
            new_value = str(input(f'New value to {info} = '))
            setattr(tasks[index], info, new_value) #function to set new value to attr name setattr(object, attr_name, new_value)
    except Exception as e:
        if e == IndexError:
            print("This Task does not exist")
        elif e == AttributeError:
            print("This Attributes does not exist.")
        else:
             print("unwanted behavior : ", e)

def main():
    tasks = [] #define tasks here si it can only be used inside main function call and not outside
    while True:
        print("\nOptions:")
        print("1. Add Task")
        print("2. Delete Tasks")
        print("3. View Tasks")
        print("4. Edit Tasks")
        print("5. Exit")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            add_task(tasks)
        elif choice == 2:
            delete_tasks(tasks)
        elif choice == 3:
            view_tasks(tasks)
        elif choice == 4:
            edit_task(tasks)
        elif choice == 5:
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
