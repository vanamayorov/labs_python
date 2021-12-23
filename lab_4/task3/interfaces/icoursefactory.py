from abc import ABC, abstractmethod


class ICourseFactory(ABC):
    """An interface of the teachers and courses factory."""
    @staticmethod
    @abstractmethod
    def create_teacher(name, course_id, teacher_id):
        pass

    @staticmethod
    @abstractmethod
    def form_course(name, teacher_obj, program_id, course_id, type_id):
        pass
