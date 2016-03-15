from flask import Response
from flask import Flask
from random import random
app = Flask(__name__)

@app.route("/")
def index():
    return "Index"

@app.route('/term/<term>')
def term(term):
    return term

@app.route('/stream')
def generate_stream():
    def generate():
        while True:
            yield str(random())+'<br>'.decode('utf-8')
    return Response(generate())#, mimetype='text/csv')

if __name__ == "__main__":
    app.run(debug=True)
