class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def add_courses(self, name_course):
        self.finished_courses.append(name_course)

    def rate_hw(self, lecturer, course, grade):
        if isinstance(lecturer,
                      Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def aver_rate_stud(self):
        sum1 = 0
        len1 = 0
        for _, grades_list in self.grades.items():
            sum1 += sum(grades_list)
            len1 += len(grades_list)
        return (round(sum1 / len1, 2))

    def __lt__(self, other):
        if self.aver_rate_stud() < other.aver_rate_stud():
            return f'У студента {self.name} хуже оценки, чем у студента {other.name}'
        elif self.aver_rate_stud() > other.aver_rate_stud():
            return f'У студента {self.name} лучше оценки, чем у студетна {other.name}'
        else:
            return f' У студентов {self.name} и {other.name} одинаковые оценки'

    def __str__(self):
        some_student = f"""Студент
Имя : {self.name}
Фамилия : {self.surname}
Средняя оценка за лекции: {self.aver_rate_stud()}
Курсы в процессе изучения: {','.join(self.courses_in_progress)}
Завершенные курсы: {','.join(self.finished_courses)}"""

        return some_student


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def aver_rate_lec(self):
        return Student.aver_rate_stud(self)

    def __lt__(self, other):
        if self.aver_rate_lec() < other.aver_rate_lec():
            return f'У лектора {self.name} хуже оценки, чем у лектора {other.name}'
        elif self.aver_rate_lec() > other.aver_rate_lec():
            return f'У лектора {self.name} лучше оценки, чем у лектора {other.name}'
        else:
            return f' У лекторов {self.name} и {other.name} одинаковые оценки'

    def __str__(self):
        some_lecturer = f'Лектор:\nИмя : {self.name}\nФамилия : {self.surname}\nСредняя оценка за лекции: {self.aver_rate_lec()}'
        return some_lecturer


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

    def __str__(self):
        some_reviewer = f'Проверяющий:\nИмя : {self.name}\nФамилия : {self.surname}'
        return some_reviewer


# STUDENTS:

first_student = Student('Ivan', 'Ivanov', 'mail')
first_student.add_courses('Введение в программирование')
first_student.courses_in_progress += ['Python', 'Git']

second_student = Student('Olesya', 'Ivanova', 'femail')
second_student.add_courses('Введение в программирование')
second_student.courses_in_progress += ['Python', 'Git']

# LECTURERS:

first_lecturer = Lecturer('Petr', 'Petrov')
first_lecturer.courses_attached += ['Python', 'Git']

second_lecturer = Lecturer('Inna', 'Petrova')
second_lecturer.courses_attached += ['Python', 'Git']

# REVIEWERS:

first_reviewer = Reviewer('Petr', 'Petrov')
first_reviewer.courses_attached += ['Python', 'Git']

second_reviewer = Reviewer('Inna', 'Petrova')
second_reviewer.courses_attached += ['Python', 'Git']

# STUDENTS rate_hw:

first_student.rate_hw(first_lecturer, 'Python', 5)
first_student.rate_hw(first_lecturer, 'Python', 8)
first_student.rate_hw(first_lecturer, 'Git', 10)
first_student.rate_hw(first_lecturer, 'Git', 6)
first_student.rate_hw(second_lecturer, 'Python', 8)
first_student.rate_hw(second_lecturer, 'Python', 7)
first_student.rate_hw(second_lecturer, 'Git', 3)
first_student.rate_hw(second_lecturer, 'Git', 5)

second_student.rate_hw(first_lecturer, 'Python', 4)
second_student.rate_hw(first_lecturer, 'Python', 8)
second_student.rate_hw(first_lecturer, 'Git', 10)
second_student.rate_hw(first_lecturer, 'Git', 6)
second_student.rate_hw(second_lecturer, 'Python', 9)
second_student.rate_hw(second_lecturer, 'Python', 7)
second_student.rate_hw(second_lecturer, 'Git', 9)
second_student.rate_hw(second_lecturer, 'Git', 3)

# REVIEWERS rate_hw:

first_reviewer.rate_hw(first_student, 'Python', 10)
first_reviewer.rate_hw(first_student, 'Python', 7)
first_reviewer.rate_hw(first_student, 'Git', 10)
first_reviewer.rate_hw(first_student, 'Git', 4)
first_reviewer.rate_hw(second_student, 'Python', 9)
first_reviewer.rate_hw(second_student, 'Python', 7)
first_reviewer.rate_hw(second_student, 'Git', 5)
first_reviewer.rate_hw(second_student, 'Git', 5)

second_reviewer.rate_hw(first_student, 'Python', 10)
second_reviewer.rate_hw(first_student, 'Python', 8)
second_reviewer.rate_hw(first_student, 'Git', 9)
second_reviewer.rate_hw(first_student, 'Git', 6)
second_reviewer.rate_hw(second_student, 'Python', 9)
second_reviewer.rate_hw(second_student, 'Python', 7)
second_reviewer.rate_hw(second_student, 'Git', 9)
second_reviewer.rate_hw(second_student, 'Git', 5)

student_list = [first_student, second_student]
lecturer_list = [first_lecturer, second_lecturer]


def aver_stud_rate1(stud_list, course):
    common_mark = 0
    quantity = 0
    for stud in stud_list:
        common_mark += sum(stud.grades[course])
        quantity += len(stud.grades[course])
    return f'Средняя оценка за домашнее задание: {round(common_mark / quantity, 2)}'


def aver_lect_rate1(lect_list, course):
    common_mark = 0
    quantity = 0
    for lect in lect_list:
        common_mark += sum(lect.grades[course])
        quantity += len(lect.grades[course])
    return f'Средняя оценка за лекции: {round(common_mark / quantity, 2)}'


print(first_student)
print("-" * 50)
print(second_student)
print("-" * 50)
print(first_lecturer)
print("-" * 50)
print(second_lecturer)
print("-" * 50)
print(first_reviewer)
print("-" * 50)
print(second_reviewer)
print("-" * 50)

print(first_student > second_student)
print(first_lecturer > second_lecturer)
print("-" * 50)
print(aver_stud_rate1(student_list, 'Git'))
print(aver_lect_rate1(lecturer_list, 'Python'))
