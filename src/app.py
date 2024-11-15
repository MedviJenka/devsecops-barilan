from src.contants import JSON_DATA
from src.core.student import Student
from flask import Flask, jsonify, Response


app = Flask(__name__)
student = Student(name='jenia', age=30, email='jenia@gmail.com')


@app.route('/', methods=['GET'])
def main() -> Response:
    return jsonify(student.get_person_data(JSON_DATA))


@app.route('/email', methods=['GET'])
def get_email() -> Response:
    return jsonify(student.get_email)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8083, debug=True)
