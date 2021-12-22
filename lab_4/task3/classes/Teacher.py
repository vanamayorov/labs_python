from abc import ABC, abstractmethod
from lab_4.task3.interfaces.iteacher import ITeacher


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
