class Student:
    name = ""
    grade = ""

    def __init__(self, student_name, student_grade):
        self.name = student_name
        self.grade = student_grade

    def study(self, subject):
        print(f"{self.name} on grade {self.grade} is studying {subject}")

student1 = Student("Ahmad", "3")
student1.study("biologi")

student2 = Student("Salman", "5")
student2.study("fisika")

