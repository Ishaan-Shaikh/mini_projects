# TODO
# [✅] initialise empty list
# [✅] create menu
# [✅] def functions of menu
# [] complete the functions

def main():
    task = []
    menu = "\n■■■■■MENU■■■■■\n1 Add Task\n2 View Task\n 3 Update Task\n4 Delete Task\n5 Exit"
    choice = input("\nOption Number -> ")
    while True:
        if choice == "1":
            add_task()
        elif choice == "2":
            view_task()
        elif choice == "3":
            update_task()
        elif choice == "4":
            del_task()
        elif choice == "5":
            break


def add_task():
    ...


def view_task():
    ...


def update_task():
    ...


def del_task():
    ...


if __name__ == "__main__":
    main()
