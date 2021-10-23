# 1. Create a class Rectangle with attributes length and width, each of which defaults to 1.
# Provide methods that calculate the perimeter and the area of the rectangle.
# Also, provide setter and getter for the length and width attributes.
# The setter should verify that length and width are each floating-point numbers larger than 0.0 and less than 20.0.
"""Script with a rectangle class"""


class Rectangle:
    """Rectangle class with setters, getters, get perimeter, and get area methods"""

    def __init__(self, length=1, width=1):
        self.length = length
        self.width = width

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, width):
        if not isinstance(width, int):
            raise TypeError("Invalid type or value of width, try again")

        if width < 0 or width > 20:
            raise ValueError("Value interval for width between 0 and 20")

        self.__width = width

    @property
    def length(self):
        return self.__length

    @length.setter
    def length(self, length):
        if not isinstance(length, int):
            raise TypeError("Invalid type or value of width, try again")

        if length < 0 or length > 20:
            raise ValueError("Value interval for length between 0 and 20")

        self.__length = length

    def get_perimeter(self):
        """Get perimeter

        Returns perimeter of a rectangle"""
        return round((self.width + self.length) * 2, 3)

    def get_area(self):
        """Get area

        Returns area of a rectangle"""
        return self.width * self.length

    def __str__(self):
        return "length = {}, width = {}".format(self.length, self.width)


def main():
    rect = Rectangle(2, 5)
    print(rect)
    print(rect.get_area())
    print(rect.get_perimeter())

    try:
        false_rect = Rectangle('a', 'b')
    except Exception as e:
        print(e)


if __name__ == '__main__':
    main()
