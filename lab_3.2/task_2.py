# Pizzeria offers pizza-of-the-day for business lunch. The type of pizza-of-the-day depends on the day of week.
# Having a pizza-of-the-day simplifies ordering for customers. They don't have to be experts on specific
# types of pizza.
# Also, customers can add extra ingredients to the pizza-of-the-day. Write a program that will form
# orders from customers.

# 7 classes of pizza
# get day in system time
# find out what is a factory and how it can be implemented in this task
import json
import os
from datetime import date
import calendar


class PizzaOfTheDay:
    __pizza_data = {}

    def __init__(self, day):
        self.__pizza_obj = PizzaOfTheDay.__pizza_data[day]
        self.pizza_name = self.__pizza_obj['name']
        self.pizza_price = self.__pizza_obj['price']
        self.pizza_ingredients = []
        for item in self.__pizza_obj['ingredients']:
            self.pizza_ingredients.append(item)
        self.pizza_day = day

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

    @property
    def pizza_day(self):
        return self.__pizza_day

    @pizza_day.setter
    def pizza_day(self, pizza_day):
        self.__pizza_day = pizza_day

    def add_ingredients(self, args: dict):
        if not isinstance(args, dict):
            raise TypeError("Args must be a dictionary")

        for item in args:
            self.pizza_ingredients.append(item)
            self.pizza_price += args[item]

    def get_pizza_data(self):
        data = {
            "pizzaName": self.pizza_name,
            "pizzaPrice": self.pizza_price,
            "pizzaIngredients": self.pizza_ingredients
        }

        return data

    def __str__(self):
        return f'Pizza name: {self.pizza_name}, price: {self.pizza_price}, ingredients: {", ".join(self.pizza_ingredients)}, pizza day: {self.pizza_day}'


class MondayPizza(PizzaOfTheDay):
    def __init__(self, day):
        super().__init__(day)


class TuesdayPizza(PizzaOfTheDay):
    def __init__(self, day):
        super().__init__(day)


class WednesdayPizza(PizzaOfTheDay):
    def __init__(self, day):
        super().__init__(day)


class ThursdayPizza(PizzaOfTheDay):
    def __init__(self, day):
        super().__init__(day)


class FridayPizza(PizzaOfTheDay):
    def __init__(self, day):
        super().__init__(day)


class SaturdayPizza(PizzaOfTheDay):
    def __init__(self, day):
        super().__init__(day)


class SundayPizza(PizzaOfTheDay):
    def __init__(self, day):
        super().__init__(day)


class PizzaFactory:
    @staticmethod
    def get_pizza_by_day(day: str):
        pizza_dict = {
            "monday": MondayPizza,
            "tuesday": TuesdayPizza,
            "wednesday": WednesdayPizza,
            "thursday": ThursdayPizza,
            "friday": FridayPizza,
            "saturday": SaturdayPizza,
            "sunday": SundayPizza
        }

        if day not in pizza_dict:
            raise ValueError("Such day doesn`t exist")

        return pizza_dict[day](day)


class Order:
    __order_id = 0

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
        Order.__order_id += 1
        data = {
            "orderId": Order.__order_id,
            "price": self.calculate_value(),
            "products": list(map(lambda x: x.get_pizza_data(), self.products_info))
        }

        if Order.__order_id == 1:
            with open(filename, 'w') as f:
                json.dump([data], f, indent=2)
        else:
            with open(filename, 'r') as f:
                data_json = json.load(f)

            data_json.append(data)

            with open(filename, 'w') as f:
                json.dump(data_json, f, indent=2)


def __str__(self):
    return f'{self.calculate_value()}, {self.get_products_info()}'


def main():
    PizzaOfTheDay.get_data("task2.json")
    week_day = calendar.day_name[date.today().weekday()].lower()
    pizza = PizzaFactory.get_pizza_by_day(week_day)
    pizza.add_ingredients({"tomatoes": 15, "bacon": 30})
    pizza2 = PizzaFactory.get_pizza_by_day(week_day)
    order_file = "order.json"
    Order([pizza, pizza2]).create_json(order_file)
    Order([pizza]).create_json(order_file)


if __name__ == "__main__":
    main()
