from flask import Flask, jsonify, Response

app = Flask(__name__)


def person(name: str, person_id: str) -> Response:
    return jsonify([name, person_id])


@app.route('/', methods=['GET'])
def main() -> Response:
    return person(name='jenia', person_id='1234567')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
