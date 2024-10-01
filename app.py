from flask import Flask, request, render_template
from flask import Flask, request
from markupsafe import escape

app = Flask(__name__)

if __name__ == '__main__':
    app.run(debug=True)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/hello')
def hello():
    return "Hello, World!"
