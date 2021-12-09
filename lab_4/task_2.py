# Create a class COMPOSITION with the names of goods, their quantity and price. Define methods for working with these
# data fields and overload operations to replenish product information, retrieve product information, generate a report
# on the availability of goods in stock according to the request.


class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if not isinstance(name, str):
            raise TypeError('Name must be str type')

        if len(name) <= 1:
            raise ValueError("Name must be longer than 2 symbols")

        self.__name = name

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, price):
        if not isinstance(price, int):
            raise TypeError('Price must be int type')

        if price <= 0:
            raise ValueError("Price must be positive")

        self.__price = price

    def __str__(self):
        return f'Name: {self.name}, price: {self.price}'


class Composition:
    def __init__(self):
        self.__stock = {}

    def __iadd__(self, other):
        if not isinstance(other, Product):
            raise TypeError("Wrong Product type")

        if other not in self.__stock:
            self.__stock.update({other: 1})
        else:
            self.__stock[other] += 1

        return self

    def __isub__(self, other):
        if not isinstance(other, Product):
            raise TypeError("Wrong Product type")

        if other not in self.__stock:
            raise ValueError("Product is not in stock anymore")

        self.__stock[other] -= 1

        if self.__stock[other] <= 0:
            self.__stock[other] = 0

        return self

    def __mul__(self, other):
        if not isinstance(other, Product):
            raise TypeError("Wrong Product type")

        if other not in self.__stock:
            output_str = f'{other.name} not in stock'
        else:
            output_str = f'Name: {other.name}, price: {other.price}, available in stock: {self.__stock[other]}'

        return output_str

    def __str__(self):
        return f'{self.__stock}'


product = Product("iphone", 799)
comp = Composition()
comp += product
comp -= product
output = comp * product
print(output)
print(comp)
