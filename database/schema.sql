CREATE DATABASE IF NOT EXISTS student_management;

USE student_management;


CREATE TABLE students (
    student_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE,
    department VARCHAR(50) NOT NULL,
    year INT NOT NULL
);


CREATE TABLE subjects (
    subject_id INT AUTO_INCREMENT PRIMARY KEY,
    subject_name VARCHAR(100) NOT NULL UNIQUE
);


CREATE TABLE marks (
    mark_id INT AUTO_INCREMENT PRIMARY KEY,
    student_id INT NOT NULL,
    subject_id INT NOT NULL,
    marks INT NOT NULL,

    FOREIGN KEY (student_id)
        REFERENCES students(student_id),

    FOREIGN KEY (subject_id)
        REFERENCES subjects(subject_id),

    CHECK (marks BETWEEN 0 AND 100)
);


INSERT INTO subjects (subject_name) VALUES
('Python'),
('AI'),
('Database Management Systems'),
('Computer Networks'),
('SQL');