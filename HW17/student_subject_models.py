from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import func

# 1 Add models for student, subject and student_subject in SQLAlchemy

Base = declarative_base()


class Student(Base):
    __tablename__ = 'student'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    age = Column(Integer, nullable=False)
    subjects = relationship('Subject', secondary='student_subject')


class Subject(Base):
    __tablename__ = 'subject'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)


class StudentSubject(Base):
    __tablename__ = 'student_subject'
    id = Column(Integer, primary_key=True)
    student_id = Column(Integer, ForeignKey('student.id'), nullable=False)
    subject_id = Column(Integer, ForeignKey('subject.id'), nullable=False)


# Connect

DATABASE_URI = 'postgresql://{user}:{password}@{host}:{port}/{database}'


engine = create_engine(
    DATABASE_URI.format(
        host='localhost',
        database='postgres',
        user='user',
        password='password',
        port=5432,
    )
)

# Insert data

Session = sessionmaker(bind=engine)
session = Session()

student1 = Student(name='Bae', age=18)
student2 = Student(name='Eddy', age=21)
student3 = Student(name='Lily', age=22)
student4 = Student(name='Jenny', age=19)

subject1 = Subject(name='English')
subject2 = Subject(name='Math')
subject3 = Subject(name='Spanish')
subject4 = Subject(name='Ukrainian')

session.add_all(
    [student1, student2, student3, student4,
     subject1, subject2, subject3, subject4]
     )
session.commit()

# 2 Find all 'students' name that visited 'English' classes

english_students = session.query(Student)\
    .join(StudentSubject)\
    .join(Subject)\
    .filter(Subject.name == 'English').all()

for student in english_students:
    print(student.name)

# 3 (Optional): Rewrite all queries using SQLAlchemy

# 1 Select
young_students = session.query(Student)\
    .filter(Student.age < 20, Student.age > 10).all()

students_under_20_or_named_john = session.query(Student)\
    .filter((Student.age < 20) | (Student.name == 'John')).all()

# 2 Order by
students_sorted_by_age = session.query(Student.name, Student.age)\
    .order_by(Student.age).all()

students_age_20_descending = session.query(Student.name, Student.age)\
    .filter(Student.age == 20).order_by(Student.age.desc()).all()

# 3 Inner join
# Simple join between two tables
students_with_subjects = session.query(Student, StudentSubject)\
    .join(StudentSubject, Student.id == StudentSubject.student_id).all()

# Select columns during the join
student_names_with_ids = session\
    .query(Student.name, StudentSubject.student_id)\
    .join(StudentSubject, Student.id == StudentSubject.student_id).all()

# Join with three tables
students_with_subjects_and_names = session\
    .query(Student, StudentSubject, Subject)\
    .join(StudentSubject, Student.id == StudentSubject.student_id)\
    .join(Subject, Subject.id == StudentSubject.subject_id).all()

students_and_subject_ids = session.query(Student.id, Subject.id)\
    .join(Subject, Subject.id == Student.id).all()

# 4 Left/right join
left_join_result = session.query(Student, StudentSubject)\
    .outerjoin(StudentSubject, Student.id == StudentSubject.student_id).all()

right_join_result = session.query(Student, StudentSubject)\
    .outerjoin(Student, Student.id == StudentSubject.student_id).all()

# 5 Aggregate functions

student_count = session.query(func.count(Student.id)).scalar()

min_age = session.query(func.min(Student.age)).scalar()

average_age = session.query(func.avg(Student.age)).scalar()

# 6 Update

session.query(Student).filter(Student.name == 'Bae').update({'age': 20})
session.commit()

# 7 Delete
session.query(Student).filter(Student.name == 'Bae').delete()
session.commit()

session.query(Student).delete()
session.commit()
