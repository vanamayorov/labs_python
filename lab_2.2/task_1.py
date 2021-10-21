# Task 1.
# Create a class that descibes a Product of online store. As a Product fields you can use a price, description
# and product' dimensions.
# Create a class that describes a Customer. As a Customer fields you can use surname, name, patronymic,
# mobile phone, etc.
# Create a class that describes an Order.
# - the order must contain data about the customer who carried it out and products.
# Implement a method for calculating the total order value.
import re
import phonenumbers

"""Script with Product, Customer, and Order classes"""


class Product:
    """Product class with getters and setters"""
    def __init__(self, name, price, id_num, description=""):
        self.name = name
        self.price = price
        self.description = description
        self.id_num = id_num

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError("Product name must be a string")

        if len(value) <= 1:
            raise ValueError("Product name must contain at least 2 characters")

        self.__name = value

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if not isinstance(value, int) and not isinstance(value, float):
            raise TypeError("Product price must be a number")

        if value <= 0:
            raise ValueError("Product price must be a positive number")

        self.__price = value

    @property
    def description(self):
        return self.__description

    @description.setter
    def description(self, value):
        if not isinstance(value, str):
            raise TypeError("Description must be a string")

        if not value:
            raise ValueError("Description must contain text")

        self.__description = value

    @property
    def id_num(self):
        return self.__id_num

    @id_num.setter
    def id_num(self, value):
        if not isinstance(value, int):
            raise TypeError("Id must be a digit")

        self.__id_num = value

    def __str__(self):
        return f'{self.price}, {self.name} ,{self.description}'


class Customer:
    """Customer class with getters and setters"""
    def __init__(self, name, surname, phone, email):
        self.name = name
        self.surname = surname
        self.email = email
        self.phone = phone

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if not isinstance(name, str):
            raise TypeError("Customer name must be a string")

        if len(name) <= 1:
            raise ValueError("Customer name must contain at least 2 characters")

        self.__name = name

    @property
    def surname(self):
        return self.__surname

    @surname.setter
    def surname(self, surname):
        if not isinstance(surname, str):
            raise TypeError("Customer surname must be a string")

        if len(surname) <= 1:
            raise ValueError("Customer surname must contain at least 2 characters")

        self.__surname = surname

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, email):
        if not isinstance(email, str):
            raise TypeError("Email must be a string")

        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        if not re.fullmatch(regex, email):
            raise ValueError("Email is not valid")

        self.__email = email

    @property
    def phone(self):
        return self.__phone

    @phone.setter
    def phone(self, phone):
        if not isinstance(phone, str):
            raise TypeError("Customer phone must be a string")

        if not phonenumbers.is_possible_number(phonenumbers.parse(phone, "UA")):
            raise ValueError("Customer phone is not valid")

        self.__phone = phone

    def __str__(self):
        return f'{self.name}, {self.surname}, {self.email}'


class Order:
    """Order class with calculate_value, get_products_info, add_product, delete_product methods"""
    def __init__(self, customer, args):
        if not isinstance(customer, Customer):
            raise TypeError("Customer argument isn`t instance of Customer class")
        if not all(isinstance(item, Product) for item in args):
            raise TypeError("Products in argument aren`t instances of Product classes")
        self.customer_name = customer.name
        self.customer_surname = customer.surname
        self.products_info = {product: args.count(product) for product in args}

    def calculate_value(self):
        """Calculate value of products in order.

        Summarize all products` prices in products_info dictionary and returns total value
        """
        total_value = 0
        for product in list(self.products_info.items()):
            total_value += int(product[0].price) * int(product[1])
        return total_value

    def get_products_info(self):
        """Get info about all products in order, such as a product name and an amount of this product

        Forms a string with a product information and returns it
        """
        output = ''
        for product in list(self.products_info.items()):
            output += f'{product[0].name} - {product[1]}, '
        return output.strip(', ')

    def add_product(self, product):
        """Add product to order

        Adds the product to product list if it isn`t there, otherwise increases the amount of the product
        """
        if not isinstance(product, Product):
            raise TypeError("Your product is not an instance of the Product class")

        if product not in self.products_info:
            self.products_info[product] = 1
        else:
            self.products_info[product] += 1

    def delete_product(self, product):
        """Delete product from order

        Deletes the product from product list
        """
        if not isinstance(product, Product):
            raise TypeError("Your product is not an instance of the Product class")

        if product not in self.products_info:
            raise ValueError("Your product is not in order anymore")

        self.products_info[product] -= 1

        if self.products_info[product] <= 0:
            del self.products_info[product]

    def __str__(self):
        return f'{self.customer_name} {self.customer_surname}, {self.calculate_value()}, {self.get_products_info()}'


def main():
    try:
        iphone = Product("Iphone", 499, 1, "Brand new")
        xiaomi = Product("Xiaomi", 399, 2, "Brand new")
        john = Customer("John", "Doe", "+3805553535", "google@gmail.com")
        order = Order(john, [iphone, xiaomi, xiaomi])
        order.add_product(iphone)
        order.delete_product(iphone)
        print(order.calculate_value())
        print(order)
    except Exception as e:
        print(e)


main()
