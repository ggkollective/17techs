# 다음 코드를 실행하기 위해서는 flask 모듈을 설치해야 합니다.

import json
from dataclasses import dataclass
import datetime
from flask import request, Flask, Blueprint

bp = Blueprint('v1', __name__, url_prefix='/v1')

posts = {}
post_number = 1


@dataclass
class BlogPost:
    title: str  # 제목
    contents: str  # 내용
    date: str  # 작성/마지막 업데이트 날짜


@bp.route('/posts', methods=['POST'])
def write_post():
    request_json = request.get_json()
    title = request_json.get('title', '')
    contents = request_json.get('contents', '')

    if len(title) == 0 or len(contents) == 0:
        return 'Bad request', 400

    global post_number  # 전역 변수를 명시하는 코드
    # 실제 시간을 외부 설정에 영향받지 않는 고정된 날짜 규격으로 변환해 사용합니다.
    now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    print('title={0}, contents={1}, date={2}, post_number={3}'.format(
        title, contents, now, post_number))

    # 실무에서는 SQLITE, MySQL 등을 이용해 데이터베이스에 저장하게 될 것입니다.
    posts[post_number] = BlogPost(title=title, contents=contents, date=now)
    post_number = post_number + 1

    return 'OK', 200


@bp.route('/posts', methods=['GET'])
def get_posts():
    posts_size = request.args.get('size', '-1')
    posts_size = int(posts_size)

    posts_json = []
    posts_acquired = 0
    # 글을 가져옵니다.
    for number in posts:
        post = posts[number]
        posts_json.append({'title': post.title,
                           'contents': post.contents,
                           'date': post.date,
                           'number': number})
        # 글 개수가 지정 개수를 넘었을 경우 더 이상 가져오지 않습니다.
        posts_acquired = posts_acquired + 1
        if 0 <= posts_size <= posts_acquired:
            break

    response_json = {'posts': posts_json}

    try:
        # ensure_ascii=False 로 지정하여 유니코드가 포함된다는 것을 명시합니다.
        return json.dumps(response_json, ensure_ascii=False)
    except json.JSONDecodeError:
        return 'Internal Server Error', 500


@bp.route('/posts/<number>', methods=['GET'])
def get_post(number):
    post = posts.get(int(number), None)
    if not post:
        return 'Bad Request', 400

    posts_json = [{'title': post.title,
                   'contents': post.contents,
                   'date': post.date,
                   'number': number}]
    response_json = {'post': posts_json}

    try:
        # ensure_ascii=False 로 지정하여 유니코드가 포함된다는 것을 명시합니다.
        return json.dumps(response_json, ensure_ascii=False)
    except json.JSONDecodeError:
        return 'Internal Server Error', 500


@bp.route('/posts/<number>', methods=['PUT'])
def update_post(number):
    number = int(number)
    post = posts.get(number, None)
    if not post:
        return 'Bad Request', 400

    # 변경할 제목과 내용을 가져옵니다.
    request_json = request.get_json()
    title = request_json.get('title', '')
    contents = request_json.get('contents', '')

    if len(title) == 0 or len(contents) == 0:
        return 'Bad request', 400

    # 마지막 수정 날짜를 업데이트합니다.
    now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    print('title={0}, contents={1}, date={2}, number={3}'.format(
        title, contents, now, number))

    # 변경된 내용으로 전체 데이터를 덮어씁니다.
    posts[number] = BlogPost(title=title, contents=contents, date=now)
    return 'OK', 200


@bp.route('/posts/<number>', methods=['DELETE'])
def delete_post(number):
    post = posts.get(int(number), None)
    if not post:
        return 'Bad Request', 400

    del posts[int(number)]
    return 'OK', 200


app = Flask(__name__)
app.register_blueprint(bp)
app.url_map.strict_slashes = False
app.run()
