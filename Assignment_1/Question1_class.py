from dataclasses import dataclass


@dataclass
class Rectangle:
    """
    A class that calculates perimeter and area of a rectangle, and prints visual representation
    from inputs height and width.
    """
    height: int
    width: int

    def getPerimeter(self, height, width):
        return 2 * (height + width)

    def getArea(self, height, width):
        return height * width

    def visual(self):
        width2 = self.width
        width3 = self.width - 2
        print("* " * width2)
        height2 = self.height
        for h in range(1, height2 - 1):
            print("*", "  " * width3, f"{'*':<30}")
        print("* " * width2)