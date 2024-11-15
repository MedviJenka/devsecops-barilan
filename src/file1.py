from src.file2 import Student

data = [
    {'name': 'jenia', 'age': 44},
    {'name': 'noam', 'age': 33},
    {'name': 'menahem', 'age': 66},
]


def get_all() -> list:
    _list = []
    for each in data:
        s = Student(**each)
        _list.append(s.get_person_data())
    return _list
