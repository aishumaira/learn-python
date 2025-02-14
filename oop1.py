class Person:
    def __init__(self,name, age):
        self.name = name
        self.age = age

    def getInfo(self):
        print(f"This person's name is {self.name} and they are {self.age} years old")
#Child class student yang mewarisi person
class Student(Person):
    def __init__(self, name, age, nis, grade):
        super().__init__(name, age) #Memanggil konstruktor parent
        self.nis = nis
        self.grade = grade

    def getInfo(self):
        print(f"This student's name is {self.name}, they are {self.age}, and they are in grade {self.grade}")

    def study(self, subject):
        print(self.name, "is studying", subject)

#Membuat objek dari kelas person
person1 = Person("Ahmad", 30)
person1.getInfo()

#membuat objek dari kelas student
student1 = Student("Beni", 16, "20211243", "10th")
student1.getInfo()
student1.study("Math")