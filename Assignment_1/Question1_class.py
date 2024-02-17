from dataclasses import dataclass
@dataclass
class Rectangle:
    """
    A class that calculates perimeter and area of a rectangle
    from input height, and width.
    """
    height: int
    width: int

    def getPerimeter(self, height, width):
        return 2 * (height + width)

    def getArea(self, height, width):
        return height * width

    def visual(self):
        width2 = self.width
        # width3 variable for formatting, need 2 less spaces than width number to account for the 2 lines of "*".
        width3 = self.width - 2
        print("* " * width2)
        height2 = self.height
        for h in range(1, height2 - 1):
            # field width format specifier set as width3 so that width can vary significantly and rectangle will still line up.
            print("*", " " * width3, f"{'*':>{width3}}")
        print("* " * width2)