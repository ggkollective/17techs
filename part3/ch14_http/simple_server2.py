# 이 코드를 실행하기 위해서는 다음 모듈을 설치해야 합니다.
# flask

from flask import Flask
from flask import request
app = Flask(__name__)


@app.route('/')
def hello_world():
    user_agent = request.headers.get('User-Agent')
    print('user agent={0}'.format(user_agent))
    return 'Hello, World!'


app.run()
