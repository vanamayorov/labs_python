from lab_4.task3.interfaces.icoursefactory import ICourseFactory
from lab_4.task3.classes.Database import Database
from lab_4.task3.classes.LocalCourse import LocalCourse
from lab_4.task3.classes.OffsiteCourse import OffsiteCourse
from lab_4.task3.classes.Teacher import Teacher
from lab_4.task3 import config


class CourseFactory(ICourseFactory):
    @staticmethod
    def create_teacher(name, course_id, teacher_id):
        with Database(config.db_path) as db:
            db.execute(f"SELECT * FROM teachers WHERE id={teacher_id}")
            result = db.fetchone()
            if result:
                return Teacher(name, course_id, teacher_id)

        teacher = Teacher(name, course_id, teacher_id)

        with Database(config.db_path) as db:
            db.execute("INSERT INTO teachers (id, teacher_name, course_id) VALUES (?, ?, ?)",
                       (teacher_id, name, course_id))

        return teacher

    # name, teacher_obj, program_id, course_id, type_id
    @staticmethod
    def form_course(name, teacher_obj, program_id, course_id, type_id):
        course_dict = {
            "1": LocalCourse,
            "2": OffsiteCourse
        }
        with Database(config.db_path) as db:
            db.execute(f"SELECT * FROM courses WHERE id={course_id}")
            result = db.fetchone()
            if result:
                return course_dict[str(type_id)](name, teacher_obj, program_id, course_id, type_id)

        if str(type_id) not in course_dict:
            raise ValueError("No such type of course")

        course = course_dict[str(type_id)](name, teacher_obj, program_id, course_id, type_id)

        with Database(config.db_path) as db:
            db.execute("INSERT INTO courses(id, course_name, teacher_id, type_id, program_id) VALUES(?, ?, ?, ?, ?)",
                       (course_id, name, teacher_obj.teacher_id, type_id, program_id))

        return course
