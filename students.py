class Student:
    # lst = []
    students = []

    def __init__(self, name, surname, gender):
        # super().__init__()
        self.name = name
        self.surname = surname
        self.gender = gender
        self.courses_in_progress = []
        self.finished_courses = []
        self.grades = {}
        Student.students.append(self)

    def student_add_courses(self, course):
        self.courses_in_progress.append(course)

    def average_grade(self, grades_dict):
        sum_grades = 0
        for grade in grades_dict.values():
            if len(grade) > 0 and len(grades_dict) > 0:
                sum_grades += sum(grade) / len(grade)
                return sum_grades / len(grades_dict)
            else:
                return 0

    def __lt__(self, other):
        return self.average_grade(self.grades) < other.average_grade(other.grades)

    def __gt__(self, other):
        return self.average_grade(self.grades) > other.average_grade(other.grades)

    def __eq__(self, other):
        return self.average_grade(self.grades) == other.average_grade(other.grades)

    def __str__(self):
        return f'\nИмя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {self.average_grade(self.grades)}\nКурсы в процессе изучения: {", ".join(self.courses_in_progress)}\nЗавершенные курсы: {", ".join(self.finished_courses)}\n'

    def student_evaluates_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer,
                      Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached and 1 <= grade <= 10:
            if course in lecturer.grades:
                print(
                    f'Студент {self.name} {self.surname} поставил лектору {lecturer.name} {lecturer.surname} первую оценку за лекцию по курсу {course}\n')
                lecturer.grades[course] += [grade]
            else:
                print(
                    f'Студент {self.name} {self.surname} поставил оценку лектору {lecturer.name} {lecturer.surname} за лекцию по курсу {course}\n')
                lecturer.grades[course] = [grade]
        else:
            print(
                f"Студент {self.name} {self.surname} не может добавить оценку лектору {lecturer.name} {lecturer.surname} за курс {course}\n")

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

class Reviewer(Mentor):
    reviewers = []
    def __init__(self, name, surname):
        super().__init__(name, surname)
        # self.name = name
        # self.surname = surname
        # self.courses_attached = []
        Reviewer.reviewers.append(self)

    def set_grades(self, student, course, grade):
        if isinstance(student, Student) and course in student.courses_in_progress and 1 <= grade <= 10:
            if course in student.grades:
                print(
                    f'Ревьюер {self.name} {self.surname} поставил оценку {grade} студенту {student.name} {student.surname} за курс {course}\n')
                student.grades[course] += [grade]
            else:
                print(
                    f'Ревьюер {self.name} {self.surname} добавил студенту {student.name} {student.surname} новый курс {course} и первую оценку за курс {grade}\n')
                student.grades[course] = [grade]
        else:
            print("Оценка от ревьюера не добавлена (целый ряд причин)\n")




class Lecturer(Mentor):
    lecturers = []
    def __init__(self, name, surname):
        super().__init__(name, surname)
        # self.name = name
        # self.surname = surname
        # self.courses_attached = []
        self.grades = {}
        Lecturer.lecturers.append(self)

    def add_courses_attached(self, course):
        self.courses_attached.append(course)

    def average_grade_for_course(self, grades, course):
        if course in grades and len(grades[course]) > 0:
            return sum(grades[course]) / len(grades[course])
        else:
            return 0

    def average_grade_for_all_courses(self, grades):
        sum_grades = 0
        for grade in grades.values():
            if len(grade) > 0:
                sum_grades += sum(grade) / len(grade)
                return sum_grades / len(grades)
            else:
                return 0

    def __lt__(self, other):
        return self.average_grade_for_all_courses(self.grades) < other.average_grade_for_all_courses(other.grades)

    def __gt__(self, other):
        return self.average_grade_for_all_courses(self.grades) > other.average_grade_for_all_courses(other.grades)

    def __eq__(self, other):
        return self.average_grade_for_all_courses(self.grades) == other.average_grade_for_all_courses(other.grades)

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.average_grade_for_all_courses(self.grades)}\n'


# Основной код
def average_all_students_for_course(course, students):
    print(f'Средняя оценка за домашние задания по всем студентам в рамках курса {course}:')
    sum_grades = 0
    sum_lens = 0
    for student in students:
        if course in student.grades and len(student.grades[course]) > 0:
            sum_grades += sum(student.grades[course])
            sum_lens += len(student.grades[course])
    return sum_grades / sum_lens


def average_all_lecturers_for_course(course, lecturers):
    print(f'Средняя оценка за лекции всех лекторов в рамках курса {course}:')
    sum_grades = 0
    sum_lens = 0
    for lecturer in lecturers:
        if course in lecturer.grades and len(lecturer.grades[course]) > 0:
            sum_grades += sum(lecturer.grades[course])
            sum_lens += len(lecturer.grades[course])
    return sum_grades / sum_lens


lect1 = Lecturer("Sam", "Semenov")
lect1.add_courses_attached(course="Python")
lect1.add_courses_attached(course="Java")

lect2 = Lecturer("Tano", "Corridi")
lect2.add_courses_attached(course="Python")
lect2.add_courses_attached(course="Java")

stud1 = Student("George", "Lucas", "male")
stud1.student_add_courses(course="Python")
stud1.student_add_courses(course="Java")
stud1.finished_courses.append("Введение в программирование")
stud1.student_evaluates_lecturer(lect1, "Python", 10)
stud1.student_evaluates_lecturer(lect1, "Python", 7)
stud1.student_evaluates_lecturer(lect1, "Python", 7)
stud1.student_evaluates_lecturer(lect2, "Python", 5)

stud2 = Student("Steven", "Spielberg", "male")
stud2.student_add_courses(course="Python")
stud2.student_add_courses(course="Java")
stud2.finished_courses.append("Введение в специальность")
stud2.student_evaluates_lecturer(lect2, "Python", 9)
stud2.student_evaluates_lecturer(lect2, "Python", 8)
stud2.student_evaluates_lecturer(lect2, "Python", 9)
stud2.student_evaluates_lecturer(lect1, "Python", 6)

# stud1.lst = [1, 2, 3]
# stud2.lst = [10, 20, 30]

rev1 = Reviewer("Ivan", "Ivanov")
# rev1.add_courses_attached(course="Python")
rev1.set_grades(stud1, "Python", 8)
rev1.set_grades(stud1, "Python", 9)
rev1.set_grades(stud1, "Python", 6)
# print(stud1.grades)
rev2 = Reviewer("Alex", "Alexandrov")
rev2.set_grades(stud2, "Python", 10)
rev2.set_grades(stud2, "Python", 3)
rev2.set_grades(stud2, "Python", 5)

print(stud1)
print(stud2)
print(lect1)
print(lect2)
print(lect1 == lect2)
print(lect2 > lect1)
print(lect2 < lect1)
print()
print(stud1 == stud2)
print(stud2 < stud1)
print(stud2 > stud1)
print()
print(average_all_students_for_course("Python", Student.students))
print(average_all_lecturers_for_course("Python", Lecturer.lecturers))

