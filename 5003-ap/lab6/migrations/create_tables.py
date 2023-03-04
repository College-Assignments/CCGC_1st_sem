import utils.db


def migrate(instance: utils.db.db):
    instance.raw(
        queries="""
        DROP DATABASE IF EXISTS ap5003;
        CREATE DATABASE IF NOT EXISTS ap5003;
        USE ap5003;
        CREATE TABLE student (
          student_id VARCHAR(50) PRIMARY KEY,
          first_name VARCHAR(50),
          last_name VARCHAR(50),
          email VARCHAR(100)
        );
        CREATE TABLE course (
          course_id VARCHAR(50) PRIMARY KEY,
          course_name VARCHAR(100),
          course_credits INT
        );
        CREATE TABLE registration (
          registration_id INT AUTO_INCREMENT PRIMARY KEY,
          student_id VARCHAR(50) NOT NULL,
          course_id VARCHAR(50) NOT NULL,
          enrollment_semester VARCHAR(50) NOT NULL,
          FOREIGN KEY (student_id) REFERENCES student(student_id) ON DELETE CASCADE,
          FOREIGN KEY (course_id) REFERENCES course(course_id) ON DELETE CASCADE,
          CONSTRAINT unique_enrollment UNIQUE (student_id, course_id, enrollment_semester)
        );
        INSERT INTO course (course_name, course_id, course_credits)
        VALUES ('Operating Systems', '5000', 3),
               ('Virtualization', '5001', 3),
               ('SDN', '5002', 3),
               ('Database', '5003', 3);
        """
    )
