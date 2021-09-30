# 1. Create a class Rectangle with attributes length and width, each of which defaults to 1.
# Provide methods that calculate the perimeter and the area of the rectangle.
# Also, provide setter and getter for the length and width attributes.
# The setter should verify that length and width are each floating-point numbers larger than 0.0 and less than 20.0.

class Rectangle:

    def __init__(self):
        self.length = 1
        self.width = 1

    def get_perimeter(self):
        return round((self.width + self.length) * 2, 3)

    def get_area(self):
        return self.width * self.length

    def get_width(self):
        return self.width

    def get_length(self):
        return self.length

    def set_width(self, width):
        if (isinstance(width, int) or isinstance(width, float)) and (width > 0 and width < 20):
            self.width = width
        else:
            raise TypeError("Invalid type or value of width, try again")

    def set_length(self, length):
        if (isinstance(length, int) or isinstance(length, float)) and (length > 0 and length < 20):
            self.length = length
        else:
            raise TypeError("Invalid type or value of length, try again")

    def __str__(self):
        return "length = {}, width = {}".format(self.get_length(), self.get_width())


def main():
    rect = Rectangle()
    rect.set_length(2)
    rect.set_width(5)
    print(rect)
    print(rect.get_area())
    print(rect.get_perimeter())

    try:
        false_rect = Rectangle()
        false_rect.set_length('a')
    except Exception as e:
        print(e)

if __name__ == '__main__':
    main()
