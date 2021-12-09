# A software academy teaches two types of courses: local courses that are held in some of the
# academy’s local labs and offsite courses held in some other town outside of the academy’s headquarters.
# Each course has a name, a teacher assigned to teach it and a course program (sequence of topics).
# Each teacher has a name and knows the courses he or she teaches. Both courses and teachers could be
# printed in human-readable text form. All your courses should implement ICourse.
# Teachers should implement ITeacher. Local and offsite courses should
# implement ILocalCourse and IOffsiteCourse respectively.
# Courses and teachers should be created only through the ICourseFactory interface implemented by a
# class named CourseFactory. Write a program that will form courses of software academy.
from abc import ABC, abstractmethod
import sqlite3

db_path = "mydb.db"


# interface
class ITeacher(ABC):
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def __str__(self):
        pass


class Teacher(ITeacher):
    def __init__(self, name, course_id, teacher_id):
        self.name = name
        self.course_id = course_id
        self.teacher_id = teacher_id

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
    def course_id(self):
        return self.__course_id

    @course_id.setter
    def course_id(self, course_id):
        if not isinstance(course_id, int):
            raise TypeError("Course id must be type of int")

        if course_id < 0:
            raise ValueError("Course id must be a positive number")

        self.__course_id = course_id

    @property
    def teacher_id(self):
        return self.__teacher_id

    @teacher_id.setter
    def teacher_id(self, teacher_id):
        if not isinstance(teacher_id, int):
            raise TypeError("Teacher id must be type of int")

        if teacher_id < 0:
            raise ValueError("Teacher id must be a positive number")

        self.__teacher_id = teacher_id

    def __str__(self):
        return f"[Teacher]: {self.name}, course_id: {self.course_id}, teacher_id: {self.teacher_id}"


# interface
class ICourse(ABC):
    @abstractmethod
    def create(self):
        pass


# interface
class ILocalCourse(ABC):
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def __str__(self):
        pass


# Base class for courses
# 1 - local
# 2 - offsite

class Course:
    def __init__(self, name, teacher_obj, program_id, course_id, type_id):
        self.name = name
        self.teacher_obj = teacher_obj
        self.program_id = program_id
        self.course_id = course_id
        self.type_id = type_id

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if not isinstance(name, str):
            raise TypeError("Course name must be a string")

        if len(name) < 2:
            raise ValueError("Course name must contain at least 2 characters")

        self.__name = name

    @property
    def teacher_obj(self):
        return self.__teacher_obj

    @teacher_obj.setter
    def teacher_obj(self, teacher_obj):
        if not isinstance(teacher_obj, Teacher):
            raise TypeError("Teacher must be type of Teacher")

        self.__teacher_obj = teacher_obj

    @property
    def course_id(self):
        return self.__course_id

    @course_id.setter
    def course_id(self, course_id):
        if not isinstance(course_id, int):
            raise TypeError

        if course_id < 0:
            raise ValueError

        self.__course_id = course_id

    @property
    def program_id(self):
        return self.__program_id

    @program_id.setter
    def program_id(self, program_id):
        if not isinstance(program_id, int):
            raise TypeError

        if program_id < 0:
            raise ValueError

        self.__program_id = program_id

    @property
    def type_id(self):
        return self.__type_id

    @type_id.setter
    def type_id(self, type_id):
        if not isinstance(type_id, int):
            raise TypeError

        if type_id < 0:
            raise ValueError

        self.__type_id = type_id

    def get_programs(self):
        with Database(db_path) as db:
            db.execute(f"SELECT program_name FROM programs WHERE id={self.program_id}")
            programs = db.fetchone()[0]
        if not programs:
            raise ValueError("No such program in programs table")

        return programs


class LocalCourse(Course, ILocalCourse):
    def __init__(self, name, teacher_obj, program_id, course_id, type_id):
        super().__init__(name, teacher_obj, program_id, course_id, type_id)

    def __str__(self):
        return f"[LocalCourse]: {self.name}, teacher: {self.teacher_obj}, course id: {self.course_id}, programs: {self.get_programs()}"


# interface
class IOffsiteCourse(ABC):
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def __str__(self):
        pass


class OffsiteCourse(Course, IOffsiteCourse):
    def __init__(self, name, teacher_obj, program_id, course_id, type_id):
        super().__init__(name, teacher_obj, program_id, course_id, type_id)

    def __str__(self):
        return f"[OffsiteCourse]: {self.name}, teacher: {self.teacher_obj}, course id: {self.course_id}, programs: {self.get_programs()}"


class ICourseFactory(ABC):
    @staticmethod
    @abstractmethod
    def create_teacher(name, course_id, teacher_id):
        pass

    @staticmethod
    @abstractmethod
    def form_course(name, teacher_obj, program_id, course_id, type_id):
        pass


class CourseFactory(ICourseFactory):
    @staticmethod
    def create_teacher(name, course_id, teacher_id):
        with Database(db_path) as db:
            db.execute(f"SELECT * FROM teachers WHERE id={teacher_id}")
            result = db.fetchone()
            if result:
                raise ValueError("Teacher with the same id already exists")

        teacher = Teacher(name, course_id, teacher_id)

        with Database(db_path) as db:
            db.execute("INSERT INTO teachers (id, teacher_name, course_id) VALUES (?, ?, ?)",
                       (teacher_id, name, course_id))

        return teacher

    # name, teacher_obj, program_id, course_id, type_id
    @staticmethod
    def form_course(name, teacher_obj, program_id, course_id, type_id):
        with Database(db_path) as db:
            db.execute(f"SELECT * FROM courses WHERE id={course_id}")
            result = db.fetchone()
            if result:
                raise ValueError("Course with the same id already exists")

        course_dict = {
            "1": LocalCourse,
            "2": OffsiteCourse
        }
        if str(type_id) not in course_dict:
            raise ValueError("No such type of course")

        course = course_dict[str(type_id)](name, teacher_obj, program_id, course_id, type_id)

        with Database(db_path) as db:
            db.execute("INSERT INTO courses(id, course_name, teacher_id, type_id, program_id) VALUES(?, ?, ?, ?, ?)",
                       (course_id, name, teacher_obj.teacher_id, type_id, program_id))

        return course


class Database:
    def __init__(self, name):
        self._conn = sqlite3.connect(name)
        self._cursor = self._conn.cursor()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()

    @property
    def connection(self):
        return self._conn

    @property
    def cursor(self):
        return self._cursor

    def commit(self):
        self.connection.commit()

    def close(self, commit=True):
        if commit:
            self.commit()
        self.connection.close()

    def execute(self, sql, params=None):
        self.cursor.execute(sql, params or ())

    def fetchall(self):
        return self.cursor.fetchall()

    def fetchone(self):
        return self.cursor.fetchone()

    def query(self, sql, params=None):
        self.cursor.execute(sql, params or ())
        return self.fetchall()


if __name__ == "__main__":
    try:
        teacher_one = CourseFactory.create_teacher("John Lennon", 3, 3)
        course_one = CourseFactory.form_course("JS for beginners", teacher_one, 2, 3, 2)
        print(teacher_one)
        print(course_one)
        with Database(db_path) as db:
            # db.execute(""" DELETE FROM courses WHERE id=3 """)
            # db.execute(""" DELETE FROM teachers WHERE id=3 """)
            db.execute(""" SELECT * FROM teachers """)
            print(db.fetchall())
    except Exception as e:
        print(e)
