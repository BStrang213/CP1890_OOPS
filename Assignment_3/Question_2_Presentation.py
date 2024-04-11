import Question_2_Buisness


def title():
    print("Player Manager")
    print()
    print("COMMAND MENU")
    print("view - View Players")
    print("add  - Add a Player")
    print("del  - Delete a Player")
    print("exit - Exit Program")
    print()


def view():
    print("place holder")


def add():
    print("place holder")


def delete():
    print("place holder")


def main():
    title()

    while True:
        choice = input("Command: ")
        if choice == "view":
            view()
        elif choice == "add":
            add()
        elif choice == "del":
            delete()
        elif choice == "exit":
            break
        else:
            print("invalid choice. Try again!")

    print("Bye!")


if __name__ == "__main__":
    main()
