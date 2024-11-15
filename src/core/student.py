import json
from src.core.person import Person


class Student(Person):

    @staticmethod
    def get_person_data(json_path: str) -> list:
        with open(json_path, 'r') as file:
            json_file = json.load(file)
            _list = []
            for each in json_file:
                _list.append(each)
            return _list
