class Student:

    def __init__(self, name , age , grade):
        self.name = name
        self.age = age
        self.grade = grade

    def get_grade(self):
        return self.grade
    

class Course:

    def __init__(self, name , max_students):
        self.name = name
        self.max_students = max_students
        self.students = []

    def add_student(self, student: Student):
        if len(self.students) < self.max_students:
            self.students.append(student)
            return True
        else:
            return False
        
    def get_average_grade(self):
        total = 0
        for student in self.students:
            total = total + student.get_grade()
        
        return total/len(self.students)

s1 = Student('Tim', 19, 95)
s2 = Student('Bill', 19, 75)
s3 = Student('Gill', 19, 65)

course = Course('Science', 2)
course.add_student(s1)
course.add_student(s2)

avg = course.get_average_grade()
print(avg)