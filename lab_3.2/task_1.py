# Task 1.
# Write a program for selling tickets to IT-events.
# Each ticket has a unique number and a price.
# There are four types of tickets: regular ticket, advance ticket (purchased 60 or more days before the event),
# late ticket (purchased fewer than 10 days before the event) and student ticket.
# Additional information:
# -advance ticket - discount 40% of the regular ticket price;
# -student ticket - discount 50% of the regular ticket price;
# -late ticket - additional 10% to the regular ticket price.
# All tickets must have the following properties:
# - the ability to construct a ticket by number;
# - the ability to ask for a ticket’s price;
# - the ability to print a ticket as a String.

import json
import os


class RegularTicket:
    __last_id = 0
    __all_tickets = []

    def __init__(self):
        self.ticket_id = self.__generate_id()
        RegularTicket.__all_tickets.append({self.ticket_id: self})

    @classmethod
    def deserialize(cls, filepath):
        if not os.path.exists(filepath):
            raise FileNotFoundError

        with open(filepath, 'r') as f:
            content = json.load(f)

        cls.__PRICE = content['price']
        cls.__NUM_OF_TICKETS = content['num0fTickets']

    @classmethod
    def get_ticket_by_id(cls, ticket_id):
        for ticket in cls.__all_tickets:
            if ticket.get(ticket_id):
                return ticket.get(ticket_id)

        raise Exception(f"Ticket with id {ticket_id} wasn't found")

    @property
    def ticket_id(self):
        return self.__ticket_id

    @ticket_id.setter
    def ticket_id(self, value):
        self.__ticket_id = value

    def __generate_id(self):
        if RegularTicket.__last_id + 1 > self.__NUM_OF_TICKETS:
            raise OverflowError('No tickets for an event left')

        RegularTicket.__last_id += 1

        return RegularTicket.__last_id

    def __get_ticket_dict(self):
        return {
            "id": self.ticket_id,
            "price": self.get_ticket_price()
        }

    def get_ticket_price(self):
        return self.__PRICE

    def serialize(self):
        with open(f'tickets/{self.__class__.__name__}-{self.ticket_id}.json', 'w', encoding='utf-8') as f:
            json.dump(self.__get_ticket_dict(), f, indent=2)

    def __str__(self):
        return f'Ticket №{self.ticket_id}, Price: {self.get_ticket_price()}'


class AdvanceTicket(RegularTicket):
    def __init__(self):
        super().__init__()

    @classmethod
    def deserialize(cls, filepath):
        if not os.path.exists(filepath):
            raise FileNotFoundError

        with open(filepath, 'r') as f:
            content = json.load(f)

        cls.__COEFFICIENT = content['advance_coefficient']

    def get_ticket_price(self):
        return round(super().get_ticket_price() * AdvanceTicket.__COEFFICIENT)


class StudentTicket(RegularTicket):
    def __init__(self):
        super().__init__()

    @classmethod
    def deserialize(cls, filepath):
        if not os.path.exists(filepath):
            raise FileNotFoundError

        with open(filepath, 'r') as f:
            content = json.load(f)

        cls.__COEFFICIENT = content['student_coefficient']

    def get_ticket_price(self):
        return round(super().get_ticket_price() * StudentTicket.__COEFFICIENT)


class LateTicket(RegularTicket):
    def __init__(self):
        super().__init__()

    @classmethod
    def deserialize(cls, filepath):
        if not os.path.exists(filepath):
            raise FileNotFoundError

        with open(filepath, 'r') as f:
            content = json.load(f)

        cls.__COEFFICIENT = content['late_coefficient']

    def get_ticket_price(self):
        return round(super().get_ticket_price() * LateTicket.__COEFFICIENT)


def main():
    json_file = "task1.json"
    RegularTicket.deserialize(json_file)
    StudentTicket.deserialize(json_file)
    LateTicket.deserialize(json_file)
    AdvanceTicket.deserialize(json_file)

    t1 = RegularTicket()
    t2 = StudentTicket()
    t3 = LateTicket()

    t3.serialize()

    print(t1)
    print(t2)
    print(t3)

    print(RegularTicket.get_ticket_by_id(2))


if __name__ == '__main__':
    main()
