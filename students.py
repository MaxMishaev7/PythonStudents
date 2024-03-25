class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def lecturers_grade(self, lecturer, lecturer_course, lecturer_grade):
        if isinstance(lecturer, Lecturer) and lecturer_course in lecturer.courses_attached and lecturer_course in self.courses_in_progress:
            if lecturer_course in lecturer.courses_grades:
                lecturer.courses_grades[lecturer_course] += [lecturer_grade]
            else:
                lecturer.courses_grades[lecturer_course] = [lecturer_grade]
        else:
            print("Ошибка")




class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.courses_grades = {}


class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']

cool_reviewer = Reviewer('Some', 'Buddy')
cool_reviewer.courses_attached += ['Python']

cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Python', 10)

best_lecturer = Lecturer("Viso", "Visioner")
print(best_lecturer.name)
print(best_lecturer.surname)

best_lecturer.courses_grades = ['Java']
best_lecturer.courses_grades['Java'] = 5
print(best_lecturer.courses_grades)
# best_student.lecturers_grade(best_lecturer, 'Java', 8)
# best_student.lecturers_grade(best_lecturer, 'C++', 10)

print(best_student.grades)
print(best_lecturer.courses_grades)