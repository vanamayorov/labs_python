# 1. Розробити клас ОРГАНІЗАЦІЯ, який містить дані про назву організації, телефон, адресу та ін.+
# 2. Визначити методи для зміни і читання значень полів цього класу.+
# 3. Перевантажити необхідні оператори. +
# 4. Створити похідний клас КАФЕДРА з додатковими полями: спеціальність, кількість бакалаврів,
# спеціалістів і магістрів. Визначити необхідні дані, методи, методи або перевизначені оператори. +
# 6. Розробити клас ФАКУЛЬТЕТ, у закритій частині якого розміщено послідовність об'єктів з даними про кафедри.
# Визначити загальну кількість студентів. +
# 7. Для роботи із послідовністю об'єктів побудувати та використати ітератор. +

import phonenumbers


class Organization:
    def __init__(self, name, phone, address):
        self.name = name
        self.phone = phone
        self.address = address

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if not isinstance(name, str):
            raise TypeError("Name must be a string")

        if len(name) < 2:
            raise ValueError("Name must contain at least 2 characters")

        self.__name = name

    @property
    def phone(self):
        return self.__phone

    @phone.setter
    def phone(self, phone):
        if not isinstance(phone, str):
            raise TypeError("Phone must be a string")

        if not phonenumbers.is_possible_number(phonenumbers.parse(phone, "UA")):
            raise ValueError("Customer phone is not valid")

        self.__phone = phone

    @property
    def address(self):
        return self.__address

    @address.setter
    def address(self, address):
        if not isinstance(address, str):
            raise TypeError("Address must be a string")

        self.__address = address

    def __str__(self):
        return f'[Organization]: {self.name}, phone: {self.phone}, address: {self.address}'


# ФАКУЛЬТЕТ
class Faculty:
    def __init__(self, name):
        self.name = name
        self.__department_seq = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if not isinstance(name, str):
            raise TypeError("Name must be a string")

        self.__name = name

    def __iadd__(self, other):
        if not isinstance(other, Department):
            raise TypeError("Other must be an instance of Faculty Class")

        if not self.__department_seq:
            self.__department_seq.append(other)
        else:
            for item in self.__department_seq:
                if item.name == other.name:
                    raise ValueError("Such department already in your sequence")
                self.__department_seq.append(other)

        return self

    def __isub__(self, other):
        if not isinstance(other, Department):
            raise TypeError("Other must be an instance of Faculty Class")

        if not self.__department_seq:
            raise ValueError("There is nothing in department sequence")

        for item in self.__department_seq:
            if item.name == other.name:
                self.__department_seq.remove(item)

        return self

    def __lt__(self, other):
        if not isinstance(other, Department):
            raise ValueError("Other must be an instance of a Department class")

        return self.count_students() < other.count_students()

    def __gt__(self, other):
        if not isinstance(other, Department):
            raise ValueError("Other must be an instance of a Department class")

        return self.count_students() > other.count_students()

    def __eq__(self, other):
        if not isinstance(other, Department):
            raise ValueError("Other must be an instance of a Department class")

        return self.count_students() == other.count_students()

    def __iter__(self):
        return next(self.__department_seq)

    def count_students(self):
        num = (item.get_students for item in self.__department_seq)
        return sum(num)

    def __str__(self):
        return f'[Faculty]: {self.name}, {" ".join(list(map(str, self.__department_seq)))}'


# КАФЕДРА
class Department(Organization):
    def __init__(self, name, phone, address, speciality, bach_num, spec_num, mast_num):
        super().__init__(name, phone, address)
        self.speciality = speciality
        self.bach_num = bach_num
        self.spec_num = spec_num
        self.mast_num = mast_num

    @property
    def speciality(self):
        return self.__speciality

    @speciality.setter
    def speciality(self, speciality):
        if not isinstance(speciality, str):
            raise TypeError("Speciality must be a string")

        self.__speciality = speciality
    @property
    def bach_num(self):
        return self.__bach_num

    @bach_num.setter
    def bach_num(self, bach_num):
        if not isinstance(bach_num, int):
            raise TypeError("Bach num must be an int")

        if bach_num < 0:
            raise ValueError("Bach num must be a positive number")

        self.__bach_num = bach_num

    @property
    def spec_num(self):
        return self.__spec_num

    @spec_num.setter
    def spec_num(self, spec_num):
        if not isinstance(spec_num, int):
            raise TypeError("Bach num must be an int")

        if spec_num < 0:
            raise ValueError("Bach num must be a positive number")

        self.__spec_num = spec_num

    @property
    def mast_num(self):
        return self.__bach_num

    @mast_num.setter
    def mast_num(self, mast_num):
        if not isinstance(mast_num, int):
            raise TypeError("Mast num must be an int")

        if mast_num < 0:
            raise ValueError("Mast num must be a positive number")

        self.__mast_num = mast_num

    def get_students(self):
        return self.bach_num + self.spec_num + self.mast_num

    def __str__(self):
        return f'[Department]: {self.name}, {self.address}, {self.phone},' \
               f'{self.speciality}, {self.bach_num}, {self.mast_num}, {self.spec_num}, total: {self.get_students()}'


faculty = Faculty("tv01")
faculty += Department("hello", "+380673822144", "khm", "coder", 1, 2, 3)
print(faculty)
