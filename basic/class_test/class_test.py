class Person:
    ### 基本属性
    name = ""
    age = 0
    ## 私有属性
    __weight = 0

    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.__weight = weight

    def speak(self):
        print(f"My name is: {self.name}, I'm {self.age} years old and {self.__weight} weight.")

class Student(Person):
    grade = ""

    def __init__(self, name, age, weight, grade):
        Person.__init__(self, name, age, weight)
        self.grade = grade

    def speak(self):
        print(f"I'm a Student and in {self.grade}, My name is: {self.name}, I'm {self.age} years old.")


p = Person("larry", 34, 96)
p.speak()
s = Student("Jack", 9, 35, "Grade 3")
s.speak()


