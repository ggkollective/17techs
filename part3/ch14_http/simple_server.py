# 이 코드를 실행하기 위해서는 다음 모듈을 설치해야 합니다.
# flask

from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, World!'


app.run()
