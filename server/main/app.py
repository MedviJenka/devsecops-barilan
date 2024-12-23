from server.core.config import Config
from flask import Flask


app = Flask(__name__)
config = Config()


@app.route('/')
def main() -> str:
    return 'Flask Project'


if __name__ == '__main__':
    app.run(host=Config.HOST, port=Config.APP_PORT, debug=Config.DEBUG)
