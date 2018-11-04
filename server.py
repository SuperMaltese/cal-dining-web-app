from flask import Flask
import read
import json
app = Flask(__name__)


@app.route('/')
def hello():
    return "Hello World!"


@app.route('/<name>')
def hello_name(name):
    return "Hello {}!".format(name)

@app.route('/<hall>/<meal>')
def test(hall, meal=''):
	return json.dumps(read.read(hall, meal))

# if __name__ == '__main__':
#     app.run()