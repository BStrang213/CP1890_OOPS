from Question1_class import Rectangle
def main():
    while True:
        height = int(input("Height:\t\t "))
        width = int(input("Width:\t\t "))
        Rectangle1 = Rectangle(height=height, width=width)
        print(f"Perimeter\t{Rectangle1.getPerimeter(height, width)}")
        print(f"Area:\t\t{Rectangle1.getArea(height, width)}")
        Rectangle1.visual()
        print("\n")
        selection = input("Continue? (y/n): ")
        if selection == 'y':
            print("\n")
            continue
        elif selection == 'n':
            print("\nBye!")
            break
        else:
            print("Invalid selection please try again.")
            continue

if __name__ == '__main__':
    main()