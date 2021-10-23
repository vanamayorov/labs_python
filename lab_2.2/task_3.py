#  The class GROUP contains a sequence of instances of the class STUDENT.
#  The class STUDENT contains the student's name, surname, record book number and grades.
#  Determine the required attributes-data and attributes-methods in classes GROUP and STUDENT.
#  Find the average score of each student.
#  Output to the standard output stream the five students with the highest average score.
#  Assume that there can be no more than 20 students in a group, as well as students with the same name and surname.


"""Script with Group and Student classes"""


class Student:
    """Student class with setters, getters and get average score method"""

    def __init__(self, name, surname, record_book_num, grades):
        self.name = name
        self.surname = surname
        self.record_book_num = record_book_num
        self.grades = grades

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if not isinstance(name, str):
            raise TypeError("Name must be a string")

        if len(name) <= 1:
            raise ValueError("Name must contain at least 2 characters")

        self.__name = name

    @property
    def surname(self):
        return self.__surname

    @surname.setter
    def surname(self, surname):
        if not isinstance(surname, str):
            raise TypeError("Surname must be a string")

        if len(surname) <= 1:
            raise ValueError("Surname must contain at least 2 characters")

        self.__surname = surname

    @property
    def record_book_num(self):
        return self.__record_book_num

    @record_book_num.setter
    def record_book_num(self, record_book_num):
        if not isinstance(record_book_num, int):
            raise TypeError("Record book num must be a digit")

        if record_book_num <= 0:
            raise ValueError("Record book num must contain at least 1 character")

        self.__record_book_num = record_book_num

    @property
    def grades(self):
        return self.__grades

    @grades.setter
    def grades(self, grades):
        if not all(isinstance(grade, int) for grade in grades):
            raise TypeError("All grades must be digits")

        if not all(grade > 0 for grade in grades):
            raise ValueError("Grades cannot be negative")

        self.__grades = grades

    def get_avg_score(self):
        """Get an average score

        Returns an average score of a student
        """
        avg_score = 0
        for item in self.grades:
            avg_score += item
        return avg_score / len(self.grades)

    def __str__(self):
        return f'Name: {self.name}, surname: {self.surname}, record book num: {self.record_book_num}, grades: ' \
               f'{", ".join(map(str, self.grades))}\n'


class Group:
    """Group class with setters, getters, get top students, add student, and delete student methods"""
    __MAX_QTY_OF_STUDENTS = 20
    __QTY_OF_SUCCESSFUL_STUDENTS = 5

    def __init__(self, group_name, students=list):
        self.group_name = group_name
        self.students_list = students

    @property
    def group_name(self):
        return self.__group_name

    @group_name.setter
    def group_name(self, group_name):
        if not isinstance(group_name, str):
            raise TypeError("Group name must be a string")
        if len(group_name) < 2:
            raise ValueError("Group name must contain at least 2 characters")

        self.__group_name = group_name

    @property
    def students_list(self):
        return self.__students_list

    @students_list.setter
    def students_list(self, students):
        if not isinstance(students, list):
            raise TypeError("Students must be a list")
        if len(students) > Group.__MAX_QTY_OF_STUDENTS:
            raise OverflowError(f"Group cannot contain more than {Group.__MAX_QTY_OF_STUDENTS} students")
        if not all(isinstance(student, Student) for student in students):
            raise TypeError("All students must be instances of Student class")
        self.d = {f'{student.name} {student.surname}': student for student in students}
        if not len(self.d) == len(students):
            raise ValueError("Group cannot contain students with the same name and surname")

        self.__students_list = [student for student in students]

    def get_top_students(self):
        """Get top students

        Returns sliced sorted list by student average score"""
        return sorted(self.students_list, key=lambda student: student.get_avg_score(), reverse=True)[
               :Group.__QTY_OF_SUCCESSFUL_STUDENTS]

    def add_student(self, student):
        """Add student to a group

        Adds student to a students list in a group"""
        if not isinstance(student, Student):
            raise TypeError("Student must be instance of Student class")

        if f"{student.name} {student.surname}" in self.d:
            raise ValueError("Student with the same name and surname already exists in group")

        if len(self.students_list) + 1 > 20:
            raise OverflowError(f"Group cannot contain more than {Group.__MAX_QTY_OF_STUDENTS} students")

        self.d.update({f"{student.name} {student.surname}": student})
        self.students_list.append(student)

    def del_student(self, student):
        """Delete student from group

        Deletes student from a  students list in a group"""
        if not isinstance(student, Student):
            raise TypeError("Student must be instance of Student class")

        del self.d[f"{student.name} {student.surname}"]
        self.students_list.remove(student)

    def __str__(self):
        return f'Group name: {self.group_name}, students list: \n{"".join(map(str, self.students_list))}'


def main():
    lenin = Student("Vladimir", "Ulyanov", 113, [12, 12, 12, 12, 12])
    krupskaya = Student("Nadezhda", "Krupskaya", 114, [11, 11, 11, 11, 11])
    stalin = Student("Joseph", "Stalin", 115, [8, 8, 8, 8, 8])
    trotsky = Student("Leon", "Trotsky", 116, [10, 10, 10, 10, 10])
    kalinin = Student("Mikhail", "Kalinin", 117, [9, 9, 9, 9, 9])
    molotov = Student("Vyacheslav", "Molotov", 118, [7, 7, 7, 7, 7])
    voroshilov = Student("Kliment", "Voroshilov", 119, [6, 6, 6, 6, 6])
    kaganovich = Student("Lazar", "Kaganovich", 120, [5, 5, 5, 5, 5])

    group_list = [lenin, krupskaya, stalin, trotsky, kalinin, molotov, voroshilov]
    group = Group("Bolsheviks party", group_list)

    for student in group.get_top_students():
        print(student)
    group.add_student(kaganovich)
    group.del_student(trotsky)
    print(group)


if __name__ == '__main__':
    main()
