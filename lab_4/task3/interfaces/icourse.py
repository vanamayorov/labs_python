from abc import ABC, abstractmethod


class ICourse(ABC):
    """The interface of the course in the software academy."""
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
    def teacher_obj(self):
        pass

    @teacher_obj.setter
    @abstractmethod
    def teacher_obj(self, teacher_obj):
        pass

    @property
    @abstractmethod
    def course_id(self):
        pass

    @course_id.setter
    @abstractmethod
    def course_id(self, course_id):
        pass

    @property
    @abstractmethod
    def program_id(self):
        pass

    @program_id.setter
    @abstractmethod
    def program_id(self, program_id):
        pass

    @property
    @abstractmethod
    def type_id(self):
        pass

    @type_id.setter
    @abstractmethod
    def type_id(self, type_id):
        pass
