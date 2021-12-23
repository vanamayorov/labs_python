from abc import ABC, abstractmethod


class ITeacher(ABC):
    """An interface of the teacher in the software academy."""
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def __str__(self):
        pass

    @property
    @abstractmethod
    def name(self):
        pass

    @name.setter
    @abstractmethod
    def name(self, name):
        pass

    @property
    @abstractmethod
    def course_id(self):
        return self.__course_id

    @course_id.setter
    @abstractmethod
    def course_id(self, course_id):
        pass

    @property
    @abstractmethod
    def teacher_id(self):
        pass

    @teacher_id.setter
    @abstractmethod
    def teacher_id(self, teacher_id):
        pass
