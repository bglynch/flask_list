import os
from flask import Flask, render_template, request, redirect
from datetime import *

app = Flask(__name__)


tasks = [
    {'time': '12.54','name':'do shopping'},
    {'time': '12.54','name':'make lunch'}
    ]

@app.route('/')
def get_index():
    return render_template('test.html', tasks = tasks)

@app.route('/new_to_do', methods = ['POST'])
def add_task():
    task = request.form['add_to_do']
    date = datetime.today().strftime('%y.%m.%d')
    tasks.append({'time': date,'name':task})
    return redirect('/')



if __name__ == '__main__':
    app.run(host=os.getenv('IP'), port=int(os.getenv('PORT')), debug=True)