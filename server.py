import os
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
    name = 'maevekenny210'
    return render_template('index.html', title='Welcome', username=name)
        
app.run(host='0.0.0.0', port=81)
