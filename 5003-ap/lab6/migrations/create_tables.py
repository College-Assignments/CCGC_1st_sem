import utils.db


def migrate(instance: utils.db.db):
    instance.raw(
        queries="""
        DROP DATABASE IF EXISTS ap5003;
        CREATE DATABASE IF NOT EXISTS ap5003;
        USE ap5003;
        CREATE TABLE student (
          student_id INT PRIMARY KEY AUTO_INCREMENT,
          first_name VARCHAR(50),
          last_name VARCHAR(50),
          email VARCHAR(100)
        );
        CREATE TABLE course (
          course_id INT PRIMARY KEY AUTO_INCREMENT,
          course_name VARCHAR(100),
          course_code VARCHAR(50),
          course_credits INT
        );
        CREATE TABLE registration (
          registration_id INT AUTO_INCREMENT PRIMARY KEY,
          student_id INT NOT NULL,
          course_id INT NOT NULL,
          enrollment_semester VARCHAR(50) NOT NULL,
          FOREIGN KEY (student_id) REFERENCES student(student_id) ON DELETE CASCADE,
          FOREIGN KEY (course_id) REFERENCES course(course_id) ON DELETE CASCADE,
          CONSTRAINT unique_enrollment UNIQUE (student_id, course_id, enrollment_semester)
        );
        """
    )
