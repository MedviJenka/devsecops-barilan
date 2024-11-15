from dataclasses import dataclass


@dataclass
class Person:
    name: str
    age: int
    email: str

    def info(self) -> dict:
        return {
            'name': self.name,
            'age': self.age
        }

    @property
    def get_email(self) -> str:
        return self.email
