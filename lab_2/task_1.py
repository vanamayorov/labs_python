# 1. Create a class Rectangle with attributes length and width, each of which defaults to 1.
# Provide methods that calculate the perimeter and the area of the rectangle.
# Also, provide setter and getter for the length and width attributes.
# The setter should verify that length and width are each floating-point numbers larger than 0.0 and less than 20.0.

class Rectangle:

    def __init__(self, length=1, width=1):
        self.length = self.set_length(length)
        self.width = self.set_width(width)

    def get_perimeter(self):
        return round((self.width + self.length) * 2, 3)

    def get_area(self):
        return self.width * self.length

    def get_width(self):
        return self.width

    def get_length(self):
        return self.length

    @staticmethod
    def set_width(self, width):
        if not isinstance(width, int):
            raise TypeError("Invalid type or value of width, try again")

        if not width > 0 and not width < 20:
            raise ValueError("Value interval for width between 0 and 20")

        return width

    @staticmethod
    def set_length(self, length):
        if not isinstance(length, int):
            raise TypeError("Invalid type or value of width, try again")

        if not length > 0 and not length < 20:
            raise ValueError("Value interval for length between 0 and 20")

        return length

    def __str__(self):
        return "length = {}, width = {}".format(self.get_length(), self.get_width())


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
