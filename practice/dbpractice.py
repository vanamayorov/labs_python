# A software academy teaches two types of courses: local courses that are held in some of the academy’s
# local labs and offsite courses held in some other town outside of the academy’s headquarters.
# Each course has a name, a teacher assigned to teach it and a course program (sequence of topics).
# Each teacher has a name and knows the courses he or she teaches. Both courses and teachers could be
# printed in human-readable text form. All your courses should implement ICourse.
# Teachers should implement ITeacher. Local and offsite courses should implement
# ILocalCourse and IOffsiteCourse respectively. Courses and teachers should be created
# only through the ICourseFactory interface implemented by a class named CourseFactory.
# Write a program that will form courses of software academy.

import sqlite3

try:
    connection = sqlite3.connect("mydb.db")
    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS courses(
        id INTEGER PRIMARY KEY,
        course_name TEXT NOT NULL,
        teacher_id INTEGER NOT NULL,
        type_id INTEGER NOT NULL,
        program_id INTEGER NOT NULL,
        FOREIGN KEY (teacher_id)
            REFERENCES teachers (id)
        FOREIGN KEY (program_id)
            REFERENCES programs(id)
        FOREIGN KEY (type_id)
            REFERENCES course_types (id)
        );
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS teachers(
        id INTEGER PRIMARY KEY,
        teacher_name TEXT NOT NULL,
        course_id INTEGER NOT NULL,
        FOREIGN KEY (course_id)
            REFERENCES courses (id)
        );""")

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS programs(
        id INTEGER PRIMARY KEY,
        program_name TEXT NOT NULL,
        topics TEXT NOT NULL
        );
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS course_types(
        id INTEGER PRIMARY KEY,
        course_type_name TEXT NOT NULL
        );
    """)
    connection.commit()

    cursor.execute(f"INSERT INTO courses (id, course_name, teacher_id, type_id, program_id) VALUES(?, ?, ?, ?, ?)",
                   (1, "Python for beginners", 1, 1, 1))
    cursor.execute(f"INSERT INTO teachers (id, teacher_name, course_id) VALUES(?, ?, ?)",
                   (1, "John Doe", 1))
    cursor.execute(f"INSERT INTO programs (id, program_name,topics) VALUES(?, ?, ?)",
                   (1, "Elementary", "Algorithms, Loops etc"))
    cursor.execute(f"INSERT INTO course_types (id, course_type_name) VALUES(?, ?) ",
                   (1, "Local"))

    connection.commit()
except Exception as e:
    cursor.execute(""" SELECT topics FROM programs WHERE id=1 """)
    result = cursor.fetchone()
    print(result[0])
