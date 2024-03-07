from Question_1_classes import Customer, Employee

def title():
    print("Customer/Employee Data Entry")

def main():
    title()

    cont = "y"
    while cont == "y":
        user = input("Customer or Employee? (c/e): ")
        if user == "c":
            Customer()
            cont = input("Continue?: ")
        elif user == "e":
            Employee()
            cont = input("Continue?: ")
        else:
            print("invalid, try again")

    print("Bye!")


if __name__ == "__main__":
    main()