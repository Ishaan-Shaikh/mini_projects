# TODO
# [✅] initialise empty list
# [✅] create menu
# [✅] def functions of menu
# [✅] complete the functions

def main():
    task = []
    menu = "\n■■■■■MENU■■■■■\n1 Add Task\n2 View Task\n3 Update Task\n4 Delete Task\n5 Exit"
    
    while True:
        print(menu)
        choice = input("\nOption Number -> ")
        
        if choice == "1":
            task = add_task(task)
        elif choice == "2":
            view_task(task)
        elif choice == "3":
            task = update_task(task)
        elif choice == "4":
            task = del_task(task)
        elif choice == "5":
            break
        else:
            print("Invalid choice! Please choose a valid option.")

def add_task(task):
    add = input("Enter the new task: ")
    task.append(add)
    print(f"'{add}' has been added to the list.")
    return task

def view_task(task):
    if not task:
        print("No tasks available.")
    else:
        print("\nCurrent Tasks:")
        for i, t in enumerate(task, start=1):
            print(f"{i}. {t}")

def update_task(task):
    view_task(task)
    if not task:
        return task
    try:
        task_num = int(input("\nEnter the task number to update: "))
        if 1 <= task_num <= len(task):
            new_task = input("Enter the updated task: ")
            task[task_num - 1] = new_task
            print("Task updated successfully.")
        else:
            print("Invalid task number!")
    except ValueError:
        print("Please enter a valid number.")
    return task

def del_task(task):
    view_task(task)
    if not task:
        return task
    try:
        task_num = int(input("\nEnter the task number to delete: "))
        if 1 <= task_num <= len(task):
            deleted_task = task.pop(task_num - 1)
            print(f"'{deleted_task}' has been deleted.")
        else:
            print("Invalid task number!")
    except ValueError:
        print("Please enter a valid number.")
    return task

if __name__ == "__main__":
    main()
