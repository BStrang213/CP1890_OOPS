import sqlite3
import Database_Class_Exercise_Classes_UNFUNCTIONAL


def menu():
    print("COMMAND MENU")
    print("cat  - View movies by category")
    print("year - View movies by year")
    print("add  - Add a movie")
    print("del  - Delete a movie")
    print("exit - Exit program")


def view_category():
    print("Place Holder1\n")


def get_year():
    print("Place Holder2\n")


def add_movie():
    print("Place Holder3\n")


def delete_movie():
    print("Place Holder4\n")


def main():
    print("The Movie List program\n")
    menu()
    view_category()

    choice = input("Command: ")
    while choice != "exit":
        if choice == "cat":
            view_category()
            choice = input("Command: ")
        elif choice == "year":
            get_year()
            choice = input("Command: ")
        elif choice == "add":
            add_movie()
            choice = input("Command: ")
        elif choice == "del":
            delete_movie()
            choice = input("Command: ")
        elif choice == "exit":
            break
        else:
            print("Invalid")
            choice = input("Command: ")
    print("Bye!")


if __name__ == "__main__":
    main()
