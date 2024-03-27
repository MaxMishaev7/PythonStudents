class Student:
    students = []
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        Student.students.append(self)

    def __str__(self):
        return f"\nСТУДЕНТ\nИмя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: ОЦЕНКА\nКурсы в процессе изучения: {', '.join(self.courses_in_progress)}\nЗавершённые курсы: Введение в программирование\n"

    def lecturers_grade(self, lecturer, lecturer_course, lecturer_grade):
        if isinstance(lecturer,
                      Lecturer) and lecturer_course in lecturer.courses_attached and lecturer_course in self.courses_in_progress:
            if lecturer_course in lecturer.courses_grades:
                lecturer.courses_grades[lecturer_course] += [lecturer_grade]
            else:
                lecturer.courses_grades[lecturer_course] = [lecturer_grade]
        else:
            print("Оценка за курс лектору не выставлена")


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    lecturers = []
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.courses_grades = {}
        Lecturer.lecturers.append(self)

    def __str__(self):
        return f"\nЛЕКТОР:\nИмя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: Оценка\n"


class Reviewer(Mentor):
    reviewers = []
    def __init__(self, name, surname):
        super().__init__(name, surname)
        Reviewer.reviewers.append(self)

    def __str__(self):
        return f"\nРЕВЬЮЕР:\nИмя: {self.name}\nФамилия: {self.surname}\n"

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'


def average(object_list, course):
    # lst = object_list[0].grades[course]
    # print(lst)
    s = 0
    for obj in object_list:
        print(obj)
        if course in obj.grades:
            print(f"KEY {course} {obj.grades[course]}")
            s += sum(obj.grades[course])
    print(f"СУММА: {s}")


best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']
best_student.courses_in_progress += ['Java']

super_best_student = Student("Strange", "Stranger", "male")
super_best_student.courses_in_progress += ['Java']
super_best_student.courses_in_progress += ['C++']
print(super_best_student)

best_lecturer = Lecturer("Visio", "Visioner")
best_lecturer.courses_attached += ['Java']
best_lecturer.courses_attached += ['Python']
print(f"Grades for lector: {best_lecturer.courses_grades}")
print(f"BestLecturer`s courses: {best_lecturer.courses_attached}")

super_lecturer = Lecturer("Whatis", "Yourname")
super_lecturer.courses_attached += ['Java']
super_lecturer.courses_attached += ['Python']
print(super_lecturer)
print(f"SuperLecturer`s courses: {super_lecturer.courses_attached}")

super_best_student.lecturers_grade(best_lecturer, 'Java', 8)
best_student.lecturers_grade(best_lecturer, 'Python', 7)

cool_reviewer = Reviewer('Some', 'Buddy')
cool_reviewer.courses_attached += ['Python']
print(cool_reviewer)

cool_reviewer.rate_hw(best_student, 'Python', 7)
cool_reviewer.rate_hw(best_student, 'Python', 8)
cool_reviewer.rate_hw(best_student, 'Python', 5)
cool_reviewer.rate_hw(best_student, 'Java', 5)
cool_reviewer.rate_hw(best_student, 'Java', 8)

average(Student.students, 'Python')



print(best_lecturer)
# print(best_lecturer.courses_grades)

best_student.lecturers_grade(best_lecturer, 'Python', 8)
# best_student.lecturers_grade(best_lecturer, 'C++', 10)

print(best_student.grades)
print(best_lecturer.courses_grades)
