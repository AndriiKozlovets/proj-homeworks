-- 1. Create table

CREATE TABLE student (
    id serial PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    age INT NOT NULL
);

CREATE TABLE subject (
    id serial PRIMARY KEY,
    name VARCHAR(50) NOT NULL
);

CREATE TABLE student_subject (
    id serial PRIMARY KEY,
    student_id INT NOT NULL,
    subject_id INT NOT NULL,

    FOREIGN KEY (student_id)
        REFERENCES student (id),
    FOREIGN KEY (subject_id)
        REFERENCES subject (id)
);

-- 2. INSERT

-- Add students

INSERT INTO student (name, age)
VALUES
    ('Bae', 18),
    ('Eddy', 21),
    ('Lily', 22),
    ('Jenny', 19);

-- Add subject

INSERT INTO subject (name)
VALUES
    ('English'),
    ('Math'),
    ('Spanish'),
    ('Unkrainian');

-- Add student_subject

INSERT INTO student_subject (student_id, subject_id)
VALUES
    (1, 1),
    (2, 2),
    (3, 3),
    (4, 4),
    (1, 3);

-- 3. Select

SELECT name FROM student WHERE age < 20 AND age > 10;

SELECT name FROM student WHERE age < 20 OR name = 'John';

-- 4. Order by

SELECT name, age FROM student ORDER BY age;

SELECT name, age FROM student WHERE age = 20 ORDER BY age DESC;

-- 5. Inner join

-- Simple join between two tables

SELECT *
FROM student
INNER JOIN student_subject
ON student.id = student_subject.student_id;

-- Select columns during the join

SELECT student.name, student_subject.student_id
FROM student
INNER JOIN student_subject
ON student.id = student_subject.student_id;

-- Join with three tables

SELECT *
FROM student
INNER JOIN student_subject ON student.id = student_subject.student_id
INNER JOIN subject ON subject.id = student_subject.student_id;

SELECT * from (
    SELECT student.id, subject.id
    FROM student
    INNER JOIN subject ON subject.id = student.id
);

-- 6. Full join

SELECT *
FROM student
FULL JOIN student_subject
ON student.id = student_subject.student_id;

-- 7. Left/right join

SELECT *
FROM student
LEFT JOIN student_subject
ON student.id = student_subject.student_id;

SELECT *
FROM student
RIGHT JOIN student_subject
ON student.id = student_subject.student_id;

-- 8. Aggregate functions

SELECT COUNT(*) FROM student;

SELECT MIN(age) FROM student;

SELECT AVG(age) FROM student;

-- 9. Update 

UPDATE student SET age = 20 WHERE name = 'Bae';

-- 10. Delete 

DELETE FROM student WHERE name = 'Bae';

DELETE FROM student;