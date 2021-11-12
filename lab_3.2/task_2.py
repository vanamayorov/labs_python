# Pizzeria offers pizza-of-the-day for business lunch. The type of pizza-of-the-day depends on the day of week.
# Having a pizza-of-the-day simplifies ordering for customers. They don't have to be experts on specific
# types of pizza.
# Also, customers can add extra ingredients to the pizza-of-the-day. Write a program that will form
# orders from customers.
import json
import os


class PizzaOfTheDay:

    def __init__(self, day):
        self.pizza_obj = PizzaOfTheDay.__pizza_data[day]
        self.pizza_name = self.pizza_obj['name']
        self.pizza_price = self.pizza_obj['price']
        self.pizza_ingredients = self.pizza_obj['ingredients']

    @classmethod
    def get_data(cls, path):
        if not os.path.exists(path):
            raise FileNotFoundError

        with open(path, 'r') as f:
            content = json.load(f)

        cls.__pizza_data = content

    @property
    def pizza_name(self):
        return self.__pizza_name

    @pizza_name.setter
    def pizza_name(self, pizza_name):
        self.__pizza_name = pizza_name

    @property
    def pizza_price(self):
        return self.__pizza_price

    @pizza_price.setter
    def pizza_price(self, pizza_price):
        self.__pizza_price = pizza_price

    @property
    def pizza_ingredients(self):
        return self.__pizza_ingredients

    @pizza_ingredients.setter
    def pizza_ingredients(self, pizza_ingredients):
        self.__pizza_ingredients = pizza_ingredients

    def add_ingredients(self, args: dict):
        if not isinstance(args, dict):
            raise TypeError("Args must be a dictionary")

        for item in args:
            self.pizza_ingredients.append(item)
            self.pizza_price += args[item]

        return self

    def get_pizza_data(self):
        data = {
            "pizzaName": self.pizza_name,
            "pizzaPrice": self.pizza_price,
            "pizzaIngredients": self.pizza_ingredients
        }

        return data

    def __str__(self):
        return f'Pizza name: {self.pizza_name}, price: {self.pizza_price}, ingredients: {", ".join(self.pizza_ingredients)}'


class Order:
    def __init__(self, args):
        if not all(isinstance(item, PizzaOfTheDay) for item in args):
            raise TypeError("Pizzas in argument aren`t instances of PizzaOfTheDay classes")

        self.products_info = {pizza: args.count(pizza) for pizza in args}

    def calculate_value(self):
        total_value = 0
        for pizza in list(self.products_info.items()):
            total_value += int(pizza[0].pizza_price) * int(pizza[1])

        return total_value

    def get_products_info(self):
        output = ''
        for pizza in list(self.products_info.items()):
            output += f'{pizza[0].pizza_name} - {pizza[1]}, '
        return output.strip(', ')

    def add_product(self, pizza):
        if not isinstance(pizza, PizzaOfTheDay):
            raise TypeError("Your pizza is not an instance of the PizzaOfTheDay class")

        if pizza not in self.products_info:
            self.products_info[pizza] = 1
        else:
            self.products_info[pizza] += 1

    def delete_product(self, pizza):
        if not isinstance(pizza, PizzaOfTheDay):
            raise TypeError("Your pizza is not an instance of the PizzaOfTheDay class")

        if pizza not in self.products_info:
            raise ValueError("Your pizza is not in order anymore")

        self.products_info[pizza] -= 1

        if self.products_info[pizza] <= 0:
            del self.products_info[pizza]

    def create_json(self, filename):

        data = {
            "price": self.calculate_value(),
            "products": list(map(lambda x: x.get_pizza_data(), self.products_info))
        }

        with open(filename, 'w') as f:
            json.dump(data, f, indent=2)

    def __str__(self):
        return f'{self.calculate_value()}, {self.get_products_info()}'


def main():
    PizzaOfTheDay.get_data("task2.json")
    pizza = PizzaOfTheDay("saturday")
    pizza.add_ingredients({"tomatoes": 15, "bacon": 30})
    Order([pizza, PizzaOfTheDay("saturday")]).create_json("test.json")


if __name__ == "__main__":
    main()
