
CREATE DATABASE college_users_db;
CREATE DATABASE college_courses_db;
CREATE DATABASE college_enrollments_db;
CREATE DATABASE college_feedback_db;

USE college_users_db;
CREATE TABLE users(
id INT AUTO_INCREMENT PRIMARY KEY,
name VARCHAR(100),
email VARCHAR(100),
role VARCHAR(50)
);

USE college_courses_db;
CREATE TABLE courses(
id INT AUTO_INCREMENT PRIMARY KEY,
course_name VARCHAR(100),
duration VARCHAR(50)
);

USE college_enrollments_db;
CREATE TABLE enrollments(
id INT AUTO_INCREMENT PRIMARY KEY,
student_id INT,
course_id INT
);

USE college_feedback_db;
CREATE TABLE feedback(
id INT AUTO_INCREMENT PRIMARY KEY,
message TEXT
);
