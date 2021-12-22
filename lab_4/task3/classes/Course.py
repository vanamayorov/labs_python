from lab_4.task3.interfaces.icourse import ICourse
from lab_4.task3.classes.Teacher import Teacher
from lab_4.task3.classes.Database import Database
from lab_4.task3 import config


class Course(ICourse):
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
        with Database(config.db_path) as db:
            db.execute(f"SELECT program_name FROM programs WHERE id={self.program_id}")
            programs = db.fetchone()[0]
        if not programs:
            raise ValueError("No such program in programs table")

        return programs
