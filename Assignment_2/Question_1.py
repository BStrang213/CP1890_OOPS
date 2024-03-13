from Question_1_classes import Customer, Employee, Person


def title():
    print("Customer/Employee Data Entry")


def person():
    first = input("First name: ")
    last = input("Last name: ")
    email = input("Email: ")
    person1 = Person(f_name=first, l_name=last, email=email)
    return person1


def employee():
    num = input("SSN: ")
    return num


def custom():
    num = input("Number: ")
    return num


def show_person():
    full = Person.fullName
    print(f"{'Name:':} {full}")
    if isinstance(Person, Employee):
        print(f"{'SSN':} {Employee.ssn}")
    elif isinstance(Person, Customer.num):
        print(f"{'Number':} {Customer.num}")
    print()


def main():
    title()

    cont = "y"
    while cont == "y":
        user = input("Customer or Employee? (c/e): ")
        if user == "c":
            person()
            custom()
            print("CUSTOMER")
            show_person()
            cont = input("Continue?: ")
        elif user == "e":
            person()
            employee()
            print("EMPLOYEE")
            show_person()
            cont = input("Continue?: ")
        else:
            print("invalid, try again")

    print("Bye!")


if __name__ == "__main__":
    main()
