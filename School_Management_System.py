class School:
    def __init__(self,name, address) -> None:
        self.name = name
        self.address = address
        self.teachers = {}
        self.classrooms = {}

    def add_classroom(self, classroom):
        self.classrooms[classroom.name] = classroom

    def add_teacher(self, subject, teacher):
        self.teachers[subject] = teacher

    def student_addmission(self, student):
        classname = student.classroom.name
        self.classrooms[classname].add_student(student)
    
    @staticmethod
    def calculate_grade(marks):
        if marks>=80 and marks<=100:
            return 'A+' 
        elif marks>=70 and marks<=79:
            return 'A'
        elif marks>=60 and marks<=69:
            return 'A-'
        elif marks>=50 and marks<=59:
            return 'B'
        elif marks>=40 and marks<=49:
            return 'C'
        elif marks>=33 and marks<=39:
            return 'D'
        elif marks>=0 and marks<=32:
            return 'F'
        
    @staticmethod
    def grade_to_value(grade):
        grade_map = {
            'A+' : 5.00,
            'A' : 4.00,
            'A-' : 3.50,
            'B' : 3.00,
            'C' : 2.00,
            'D' : 1.00,
            'F' : 0.00,
        }
        return grade_map[grade]
    
    @staticmethod
    def value_to_grade(value):
        if value == 5.00:
            return 'A+'
        elif value>=4.00 and value<=4.99:
            return 'A'
        elif value>=3.50 and value<=3.99:
            return 'A-'
        elif value>=3.00 and value<=3.49:
            return 'B'
        elif value>=2.00 and value<=2.99:
            return 'C'
        elif value>=1.00 and value<=1.99:
            return 'D'
        elif value < 1.00:
            return 'F'
        
    def __repr__(self):
        for key in self.classrooms.keys():
            print(key)
        print("All Students")
        result = ''
        for key, value in self.classrooms.items():
            result += f"---{key.upper()} Classroom Students\n"
            for student in value.students:
                result += f"{student.name}\n"
        print(result)

        subject = ''
        for key, value in self.classrooms.items():
            subject += f"---{key.upper()} Classroom Subjects\n"
            for sub in value.subjects:
                subject += f"{sub.name}\n"
        print(subject)

        print("All Teachers")
        tchr = ''
        for subject, teacher in self.teachers.items():
            tchr += f"---{subject.upper()} Department Teacher\n"
            tchr += f"{teacher.name}\n"
        print(tchr)

        print("Students Results")
        for key, value in self.classrooms.items():
            for student in value.students:
                for k, i in student.marks.items():
                    print(student.name,k,i,student.subject_grade[k])
                print(student.calculate_final_grade())
        return ''


class Person:
    def __init__(self,name) -> None:
        self.name = name

import random

class Teacher(Person):
    def __init__(self, name) -> None:
        super().__init__(name)

    def evaluate_exam(self):
        return random.randint(50, 100)
    
class Student(Person):
    def __init__(self, name, classroom) -> None:
        super().__init__(name)
        self.classroom = classroom
        self.__id = None
        self.marks = {}
        self.subject_grade = {}
        self.grade = None

    def calculate_final_grade(self):
        sum = 0
        for grade in self.subject_grade.values():
            point = School.grade_to_value(grade)
            sum += point
        if sum == 0:
            gpa = 0.00
            self.grade = 'F'
        else:
            gpa = sum / len(self.subject_grade)
            self.grade = School.value_to_grade(gpa)
        return f"{self.name} Final Grade : {self.grade} with GPA = {gpa}\n"
    
    @property
    def id(self):
        return self.__id
    
    @id.setter
    def id(self, value):
        self.__id = value

class Subject:
    def __init__(self, name, teacher) -> None:
        self.name = name
        self.teacher = teacher
        self.max_marks = 100
        self.pass_marks = 33

    def exam(self, students):
        for student in students:
            mark = self.teacher.evaluate_exam()
            student.marks[self.name] = mark
            student.subject_grade[self.name] = School.calculate_grade(mark)

class Classroom:
    def __init__(self, name) -> None:
        self.name = name
        self.students = []
        self.subjects = []
    
    def add_student(self, student):
        roll_no = f"{self.name}-{len(self.students)+1}"
        student.id = roll_no
        self.students.append(student)
    
    def add_subjects(self, subject):
        self.subjects.append(subject)
    
    def take_semester_final_exam(self):
        for subject in self.subjects:
            subject.exam(self.students)
        for student in self.students:
            student.calculate_final_grade()


school = School("Blue Bird", "Bhairab")

eight = Classroom("Eight")
nine = Classroom("Nine")
ten = Classroom("Ten")

school.add_classroom(eight)
school.add_classroom(nine)
school.add_classroom(ten)

rahim = Student("Rahim", eight)
karim = Student("Karim", nine)
salam = Student("Salam", ten)
emon = Student("Emon", ten)

school.student_addmission(rahim)
school.student_addmission(karim)
school.student_addmission(salam)
school.student_addmission(emon)

alam = Teacher("Alam")
raima = Teacher("Raima")
roni = Teacher("Roni")

school.add_teacher("English", alam)
school.add_teacher("Chemistry", raima)
school.add_teacher("Higher Math", roni)
school.add_teacher("Biology", alam)

english = Subject("English", alam)
chemistry = Subject("Chemistry", raima)
higher_math = Subject("Higher Math", roni)
biology = Subject("Biology", alam)

eight.add_subjects(english)
eight.add_subjects(chemistry)
eight.add_subjects(biology)
nine.add_subjects(higher_math)
nine.add_subjects(english)
nine.add_subjects(biology)
nine.add_subjects(chemistry)
ten.add_subjects(english)
ten.add_subjects(chemistry)
ten.add_subjects(higher_math)
ten.add_subjects(biology)

eight.take_semester_final_exam()
nine.take_semester_final_exam()
ten.take_semester_final_exam()

print(school)