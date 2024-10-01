from flask import Flask, request, render_template
from flask import Flask, request
from markupsafe import escape

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/2')
def index2():
    return render_template('index2.html')
