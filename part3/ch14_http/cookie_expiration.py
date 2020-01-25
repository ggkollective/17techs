# 이 코드를 실행하기 위해서는 다음 모듈을 설치해야 합니다.
# flask

from flask import Flask
from flask import request
from flask import make_response
import uuid
app = Flask(__name__)


@app.route('/')
def hello_world():
    cookies = request.cookies

    if 'sessionId' in cookies:
        response = make_response(
            '기존 연결입니다: sessionId={0}'.format(cookies['sessionId']))
    else:
        new_session_id = str(uuid.uuid4())
        response = make_response(
            '새 연결입니다: sessionId={0}'.format(new_session_id))
        # 쿠키 만료 시간(max_age)은 5초입니다.
        response.set_cookie('sessionId', new_session_id, max_age=5)

    return response


app.run()
