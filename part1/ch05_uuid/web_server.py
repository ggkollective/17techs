#!/usr/bin/python3

import uuid
from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello():
    request_id = uuid.uuid4()
    print('API 요청 ID={0}'.format(request_id))
    return 'Hello World'


if __name__ == '__main__':
    app.run()
