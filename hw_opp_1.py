class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def __str__(self):
        grades_avg = self._calculate_avg_grade()
        return f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {grades_avg}'

    def _calculate_avg_grade(self):
        total = 0
        count = 0
        for course in self.grades.values():
            total += sum(course)
            count += len(course)
        if count == 0:
            return 0
        return total / count

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            raise TypeError("Both objects must be of type Lecturer")
        return self._calculate_avg_grade() < other._calculate_avg_grade()

    def __le__(self, other):
        if not isinstance(other, Lecturer):
            raise TypeError("Both objects must be of type Lecturer")
        return self._calculate_avg_grade() <= other._calculate_avg_grade()

    def __gt__(self, other):
        if not isinstance(other, Lecturer):
            raise TypeError("Both objects must be of type Lecturer")
        return self._calculate_avg_grade() > other._calculate_avg_grade()

    def __ge__(self, other):
        if not isinstance(other, Lecturer):
            raise TypeError("Both objects must be of type Lecturer")
        return self._calculate_avg_grade() >= other._calculate_avg_grade()

class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}'

class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        grades_avg = self._calculate_avg_grade()
        return f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {grades_avg}\nКурсы в процессе изучения: {", ".join(self.courses_in_progress)}\nЗавершенные курсы: {", ".join(self.finished_courses)}'

    def _calculate_avg_grade(self):
        total = 0
        count = 0
        for course in self.grades.values():
            total += sum(course)
            count += len(course)
        if count == 0:
            return 0
        return total / count

    def __lt__(self, other):
        if not isinstance(other, Student):
            raise TypeError("Both objects must be of type Student")
        return self._calculate_avg_grade() < other._calculate_avg_grade()

    def __le__(self, other):
        if not isinstance(other, Student):
            raise TypeError("Both objects must be of type Student")
        return self._calculate_avg_grade() <= other._calculate_avg_grade()

    def __gt__(self, other):
        if not isinstance(other, Student):
            raise TypeError("Both objects must be of type Student")
        return self._calculate_avg_grade() > other._calculate_avg_grade()

    def __ge__(self, other):
        if not isinstance(other, Student):
            raise TypeError("Both objects must be of type Student")
        return self._calculate_avg_grade() >= other._calculate_avg_grade()

# Создаем экземпляры классов
best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python', 'Git']
best_student2 = Student('John', 'Doe', 'male')
best_student2.courses_in_progress += ['Python', 'Git']

cool_lecturer = Lecturer('Some', 'Buddy')
cool_lecturer.courses_attached += ['Python', 'Git']
cool_lecturer2 = Lecturer('Another', 'Buddy')
cool_lecturer2.courses_attached += ['Python', 'Git']

cool_reviewer = Reviewer('Another', 'Buddy')
cool_reviewer.courses_attached += ['Python', 'Git']
cool_reviewer2 = Reviewer('Some', 'Buddy')
cool_reviewer2.courses_attached += ['Python', 'Git']

# Вызываем методы
best_student.rate_lecturer(cool_lecturer, 'Python', 10)
best_student.rate_lecturer(cool_lecturer, 'Python', 10)
best_student.rate_lecturer(cool_lecturer, 'Python', 10)

best_student2.rate_lecturer(cool_lecturer2, 'Python', 9)
best_student2.rate_lecturer(cool_lecturer2, 'Python', 9)
best_student2.rate_lecturer(cool_lecturer2, 'Python', 9)

cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Python', 10)

cool_reviewer2.rate_hw(best_student2, 'Python', 9)
cool_reviewer2.rate_hw(best_student2, 'Python', 9)
cool_reviewer2.rate_hw(best_student2, 'Python', 9)

print(cool_lecturer)
print(best_student)

print(cool_lecturer2)
print(best_student2)

print(cool_reviewer)
print(cool_reviewer2)

# Функции для подсчета средней оценки
def calculate_avg_hw_grade(students, course):
    total = 0
    count = 0
    for student in students:
        if course in student.grades:
            total += sum(student.grades[course])
            count += len(student.grades[course])
    if count == 0:
        return 0
    return total / count

def calculate_avg_lecturer_grade(lecturers, course):
    total = 0
    count = 0
    for lecturer in lecturers:
        if course in lecturer.grades:
            total += sum(lecturer.grades[course])
            count += len(lecturer.grades[course])
    if count == 0:
        return 0
    return total / count

# Вызываем функции
students = [best_student, best_student2]
lecturers = [cool_lecturer, cool_lecturer2]

print(f'Средняя оценка за домашние задания по курсу Python: {calculate_avg_hw_grade(students, "Python")}')
print(f'Средняя оценка за лекции по курсу Python: {calculate_avg_lecturer_grade(lecturers, "Python")}')