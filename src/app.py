from flask import Flask, jsonify, Response
from dataclasses import dataclass

from src.file1 import get_all

app = Flask(__name__)


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


data = Person(name='jenia', age=30, email='jenia@gmail.com')


@app.route('/', methods=['GET'])
def main() -> Response:
    return jsonify(get_all())


@app.route('/email', methods=['GET'])
def get_email() -> Response:
    return jsonify(data.get_email)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8083, debug=True)
