class Person:
    def __init__(self, name, greeting):
        self.name = name
        self.greeting = greeting

    def greet(self):
        print(f"{self.name} говорит: {self.greeting}")
    
class Student(Person):
    def __init__(self, name, greeting, major):
        super().__init__(name, greeting)
        self.major = major 

    def greet(self):
        print(f"Студент {self.name} (специальность: {self.major}) говорит: {self.greeting}")

class Teacher(Person):
    def __init__(self, name, greeting, subject):
        super().__init__(name, greeting)
        self.subject = subject

    def greet(self):
        print(f"Учитель {self.name} (предмет: {self.subject}) говорит: {self.greeting}")

student = Student("Алексей", "Привет!", "Информатика")
teacher = Teacher("Мария", "Здравствуйте!", "Математика")

student.greet()
teacher.greet()