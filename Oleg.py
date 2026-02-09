class Human:
    def __init__(self, name, age):
        self.name = name
        self.__age = age

    def get_age(self):
        return self.__age

    def set_age(self, age):
        if age > 0:
            self.__age = age

    def info(self):
        return f"Ім'я: {self.name}, Вік: {self.__age}"

    def activity(self):
        return "Людина живе та працює"


class Student(Human):
    def __init__(self, name, age, university):
        super().__init__(name, age)
        self.university = university

    def info(self):
        return f"Ім'я: {self.name}, Вік: {self.get_age()}, Університет: {self.university}"

    def activity(self):
        return "Студент навчається"


def main():
    human = Human("Іван", 35)
    student = Student("Олег", 17, "Ліцей №1")

    print(human.info())
    print(human.activity())

    print(student.info())
    print(student.activity())


if __name__ == "__main__":
    main()
