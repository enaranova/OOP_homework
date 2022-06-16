class Student:
    students_list = []
    
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.students_list.append(self)
        self.av = 0
 
    def add_courses(self, course_name):
        self.finished_courses.append(course_name)

    # def rate_lecturer(self, lecturer, course, grade):
    #     if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
    #         if course in lecturer.grades:
    #             lecturer.grades[course] += [grade]
    #         else:
    #             lecturer.grades[course] = [grade]
    #     else:
    #         return 'Ошибка'

    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached:
            if course in self.courses_in_progress or course in self.finished_courses:
                if course in lecturer.grades:
                    lecturer.grades[course] += [grade]
                else:
                    lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        grades_list = []
        for k, v in self.grades.items():
            for i in v:
                grades_list.append(i)
        av = sum(grades_list)/len(grades_list)
        return f"""
Имя: {self.name} 
Фамилия: {self.surname}
Средняя оценка за домашние задания: {av}
Курсы в процессе изучения:  {", ".join(self.courses_in_progress)}
Завершенные курсы: {", ".join(self.finished_courses)}
        """
    
    def __lt__(self, other):
        if not isinstance(other, Student):
            return 'Ошибка'
        grades_list = []
        for k, v in self.grades.items():
            for i in v:
                grades_list.append(i)
        self.av = sum(grades_list)/len(grades_list)
        return self.av < other.av

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        self.av = 0
        
    # def rate_hw(self, student, course, grade):
    #     if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
    #         if course in student.grades:
    #             student.grades[course] += [grade]
    #         else:
    #             student.grades[course] = [grade]
    #     else:
    #         return 'Ошибка'

class Lecturer(Mentor):
    lecturers_list = []
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}
        self.lecturers_list.append(self)
    
    def __str__(self):
        grades_list = []
        for k, v in self.grades.items():
            for i in v:
                grades_list.append(i)
        av = sum(grades_list)/len(grades_list)
        res = f"""
Имя: {self.name} 
Фамилия: {self.surname}
Средняя оценка за лекции: {av}
        """
        return res

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            return 'Ошибка'
        grades_list = []
        for k, v in self.grades.items():
            for i in v:
                grades_list.append(i)
        self.av = sum(grades_list)/len(grades_list)
        return self.av < other.av

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
        res = f"""
Имя: {self.name} 
Фамилия: {self.surname}
        """
        return res

student_1 = Student('Ruoy', 'Eman', 'your_gender')
# print(student_1.__dict__)
student_2 = Student('Brad', 'Pitt', 'male')
# print(student_2.__dict__)

student_1.courses_in_progress.append('Python')
student_1.courses_in_progress.append('Git')
# print(student_1.courses_in_progress)
student_2.courses_in_progress.append('C++')
student_2.courses_in_progress.append('Git')
# print(student_2.courses_in_progress)

student_1.add_courses('Введение в программирование')
# print(student_1.finished_courses)

student_2.add_courses('Введение в программирование')
student_2.add_courses('Справочник по языку C++')
# print(student_2.finished_courses)

lecturer_1 = Lecturer('Гвидо', 'ван Россум')
# print(lecturer_1.name)
# print(lecturer_1.surname)
lecturer_2 = Lecturer('Бьёрн', 'Страуструп')
# print(lecturer_2.__dict__)

lecturer_1.courses_attached.append('Введение в программирование')
lecturer_1.courses_attached.append('Python')
lecturer_1.courses_attached.append('Git')
# print(lecturer_1.courses_attached)

lecturer_2.courses_attached.append('Справочник по языку C++')
lecturer_2.courses_attached.append('C++')
# print(lecturer_2.courses_attached)

student_1.rate_lecturer(lecturer_1, 'Введение в программирование', 10)
student_1.rate_lecturer(lecturer_1, 'Введение в программирование', 9)

student_1.rate_lecturer(lecturer_1, 'Python', 10)
student_1.rate_lecturer(lecturer_1, 'Python', 9)
student_1.rate_lecturer(lecturer_1, 'Python', 8)

student_1.rate_lecturer(lecturer_1, 'Git', 10)
student_1.rate_lecturer(lecturer_1, 'Git', 9)
student_1.rate_lecturer(lecturer_1, 'Git', 8)
student_1.rate_lecturer(lecturer_1, 'Git', 7)

student_2.rate_lecturer(lecturer_1, 'Введение в программирование', 10)
student_2.rate_lecturer(lecturer_1, 'Введение в программирование', 9)

student_2.rate_lecturer(lecturer_2, 'Справочник по языку C++', 8)
student_2.rate_lecturer(lecturer_2, 'Справочник по языку C++', 7)
student_2.rate_lecturer(lecturer_2, 'Справочник по языку C++', 6)

student_2.rate_lecturer(lecturer_2, 'C++', 5)
student_2.rate_lecturer(lecturer_2, 'C++', 4)
student_2.rate_lecturer(lecturer_2, 'C++', 3)

student_2.rate_lecturer(lecturer_1, 'Git', 2)
student_2.rate_lecturer(lecturer_1, 'Git', 1)
student_2.rate_lecturer(lecturer_1, 'Git', 0)

# print(lecturer_1.grades)
# print(lecturer_2.grades)

# print(lecturer_1.__str__())
# print(lecturer_2.__str__())

reviewer_1 = Reviewer('Билл', 'Гейтс')
reviewer_2 = Reviewer('Стив', 'Джобс')

# print(reviewer_1.__str__())
# print(reviewer_2.__str__())

reviewer_1.courses_attached.append('Python')
reviewer_1.courses_attached.append('Git')

reviewer_2.courses_attached.append('C++')

reviewer_1.rate_hw(student_1, 'Python', 10)
reviewer_1.rate_hw(student_1, 'Python', 8)

reviewer_2.rate_hw(student_2, 'C++', 9)
reviewer_2.rate_hw(student_2, 'C++', 6)
reviewer_2.rate_hw(student_2, 'C++', 3)

reviewer_1.rate_hw(student_1, 'Git', 10)
reviewer_1.rate_hw(student_1, 'Git', 9)
reviewer_1.rate_hw(student_2, 'Git', 8)
reviewer_1.rate_hw(student_2, 'Git', 7)

# print(student_1.grades)
# print(student_2.grades)

# print(student_1.__str__())
# print(student_2.__str__())

# print(student_1.__lt__(student_2))
# print(lecturer_1.__lt__(lecturer_2))

def course_average_stud(list, course):
    grades_list = []
    for student in list:
        for k, v in student.grades.items():
            if course in k:
                for i in v:
                    grades_list.append(i)
    course_av = sum(grades_list)/len(grades_list)
    return course_av

print(course_average_stud(Student.students_list, 'Python'))
print(course_average_stud(Student.students_list, 'C++'))
print(course_average_stud(Student.students_list, 'Git'))

def course_average_lect(list, course):
    grades_list = []
    for lecturer in list:
        for k, v in lecturer.grades.items():
            if course in k:
                for i in v:
                    grades_list.append(i)
    course_av = sum(grades_list)/len(grades_list)
    return course_av

print(course_average_lect(Lecturer.lecturers_list, 'Python'))
print(course_average_lect(Lecturer.lecturers_list, 'C++'))
print(course_average_lect(Lecturer.lecturers_list, 'Git'))
print(course_average_lect(Lecturer.lecturers_list, 'Введение в программирование'))
print(course_average_lect(Lecturer.lecturers_list, 'Справочник по языку C++'))