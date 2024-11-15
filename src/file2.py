class Person:

    def __init__(self, *, name: str, age: int) -> None:
        self.name = name
        self.age = age


class Student(Person):

    def get_person_data(self) -> str:
        return f'name: {self.name} age: {self.age}'


if __name__ == '__main__':
    s = Student(name='jenia', age=44)
    print(s.get_person_data())
