from flask import Flask


app = Flask(__name__)


@app.route('/')
def main() -> str:
    return 'home'


@app.route('/health', methods=['GET'])
def health_check() -> dict:
    return {'service': 'healthy'}


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=88, debug=True)
