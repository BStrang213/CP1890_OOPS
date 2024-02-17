from Question1_class import Rectangle


def main():
    while True:
        height = int(input("\nHeight:\t\t "))
        width = int(input("Width:\t\t "))
        # Assigning user's inputs as height and width attributes for rectangle class.
        Rectangle1 = Rectangle(height=height, width=width)
        # Printing perimeter to user using class method getPerimeter.
        print(f"Perimeter\t{Rectangle1.getPerimeter(height, width)}")
        # Printing area to user using class getArea.
        print(f"Area:\t\t{Rectangle1.getArea(height, width)}")
        # Printing visual representation of rectangle to user using class method visual.
        Rectangle1.visual()
        selection = input("\nContinue? (y/n): ")
        if selection == 'y':
            continue
        elif selection == 'n':
            print("\nBye!")
            break
        else:
            print("\nInvalid selection please try again.")
            continue

if __name__ == '__main__':
    main()