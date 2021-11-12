# Задача 2. Створити клас ДАТИ з полями у закритій частині: день (1-31), місяць (1- 12), рік (ціле число).
# Клас має конструктор, методи встановлення дня, місяця і року, методи отримання значень дня, місяця і року,
# а також два методи виведення за шаблонами: "12 лютого 2020 року" і "12.02.2020".
# Методи встановлення полів класу повинні перевіряти коректність параметрів, що задаються.

class Date:
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year

    @property
    def day(self):
        return self.__day

    @day.setter
    def day(self, day):
        if not isinstance(day, int):
            raise TypeError("Day value must be type of int")

        if day < 1 or day > 31:
            raise ValueError("Day value must be between 1 and 31")

        self.__day = day

    @property
    def month(self):
        return self.__month

    @month.setter
    def month(self, month):
        if not isinstance(month, int):
            raise TypeError("Month value must be type of int")

        if month < 1 or month > 12:
            raise ValueError("Month value must be between 1 and 12")

        self.__month = month

    @property
    def year(self):
        return self.__year

    @year.setter
    def year(self, year):
        if not isinstance(year, int):
            raise TypeError("Year value must be type of int")

        if year <= 0:
            raise ValueError("Year value must be positive and nonzero")

        self.__year = year

    def get_month_name(self):
        month_dict = {
            "1": "січня",
            "2": "лютого",
            "3": "березня",
            "4": "квітня",
            "5": "травня",
            "6": "червня",
            "7": "липня",
            "8": "серпня",
            "9": "вересня",
            "10": "жовтня",
            "11": "листопада",
            "12": "грудня",
        }

        return month_dict[str(self.month)]

    def get_date_words(self):
        return f'{self.day} {self.get_month_name()} {self.year} року'

    def get_date_digits(self):
        return f'{self.day if self.day >= 10 else "0" + str(self.day)}.{self.month if self.month >= 10 else "0" + str(self.month)}.{self.year}'


today = Date(28, 10, 2021)
print(today.get_date_words())
print(today.get_date_digits())