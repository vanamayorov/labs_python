from lab_4.task3.interfaces.ilocalcourse import ILocalCourse
from lab_4.task3.classes.Course import Course


class LocalCourse(Course, ILocalCourse):
    """The class that describes local course."""
    def __init__(self, name, teacher_obj, program_id, course_id, type_id):
        super().__init__(name, teacher_obj, program_id, course_id, type_id)

    def __str__(self):
        return f"[LocalCourse]: {self.name}, teacher: {self.teacher_obj}, course id: {self.course_id}, programs: {self.get_programs()}"
