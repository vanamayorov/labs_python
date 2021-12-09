def substitute_class(cls):
    def substitute(*args, **kwargs):
        new_instance = Teacher(*args, **kwargs)
        return new_instance
    return substitute


@substitute_class
class Student:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def __str__(self):
        return f'[Student] name: {self.name}, surname: {self.surname}'


class Teacher:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def __str__(self):
        return f'[Teacher] name: {self.name}, surname: {self.surname}'


x = Student('Ivan', 'Ivanov')
print(x)