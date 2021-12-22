# A software academy teaches two types of courses: local courses that are held in some of the
# academy’s local labs and offsite courses held in some other town outside of the academy’s headquarters.
# Each course has a name, a teacher assigned to teach it and a course program (sequence of topics).
# Each teacher has a name and knows the courses he or she teaches. Both courses and teachers could be
# printed in human-readable text form. All your courses should implement ICourse.
# Teachers should implement ITeacher. Local and offsite courses should
# implement ILocalCourse and IOffsiteCourse respectively.
# Courses and teachers should be created only through the ICourseFactory interface implemented by a
# class named CourseFactory. Write a program that will form courses of software academy.
from classes.CourseFactory import CourseFactory
import config

from classes.Database import Database

if __name__ == "__main__":
    try:
        teacher_one = CourseFactory.create_teacher("John Lennon", 3, 3)
        course_one = CourseFactory.form_course("JS for beginners", teacher_one, 2, 3, 2)
        print(teacher_one)
        print(course_one)
        with Database(config.db_path) as db:
            db.execute(""" SELECT * FROM teachers """)
            print(db.fetchall())
    except Exception as e:
        print(e)
