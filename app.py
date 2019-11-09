import json
from base64 import b64decode, b64encode
from urllib.parse import urlencode

from flask import Flask

from process_image import get_brightness

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


TEST_NAMES = {
    'test1': 'normal/standard',
    'test2': 'bright',
    'test3': 'dark'
}

ALT_CHARS = b'+-'


def get_test_image(path):
    with open(f'test_images/{path}.jpg', 'rb') as f:
        return f.read()


@app.route('/test/list')
def get_test_names():
    return ''.join(map(lambda s: f'<p>{s}</p>', [f'- "{k}": "{v}"' for k, v in TEST_NAMES.items()]))


@app.route('/test/b64/<path>')
def get_test_img_b64(path):
    try:
        return b64encode(get_test_image(path), altchars=ALT_CHARS)
    except Exception as e:
        return f'Error: {e}'


@app.route('/test/img/<path>')
def process_test_img(path):
    try:
        return f'<p>Test Return: {str(get_brightness(get_test_image(path)))}</p>' \
            f'<p>Test Name: {TEST_NAMES[path]}</p>'
    except Exception as e:
        return f'Error: {e}'


@app.route('/img/<blob>')
def process_binary_img(blob):
    try:
        data = b64decode(blob, altchars=ALT_CHARS)
        return json.dumps({
            'data': get_brightness(data)
        })
    except Exception as e:
        return json.dumps({
            'data': -1,
            'error': str(e)
        })


if __name__ == '__main__':
    app.run()
    # app.run(debug=True)
