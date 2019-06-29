import os
from flask import Flask, redirect, render_template, request
from random import choice
import json

app = Flask(__name__)

welcome_message = ["Hi", "Hello", 'Bonjour', "Ciao"]

items = [
        "Sugar",
        "Milk"
    ]

# if including variables in the link, must be included in function as arguements

@app.route("/")
def get_index():
    welcome = choice(welcome_message)
    return render_template("index.html", msg=welcome, tasks = items)  #tasks in HTML matches items in PY

@app.route("/new_task", methods = ['POST'])
def create_a_task():
    task = request.form['task_to_do']
    items.append(task)
    
    with open("data/list.json", "w") as f: #sinilar code as previous example, except file auto closes
        data = json.dumps(items)    #dump our items data into a string
        f.write(data)
    return redirect('/')







if __name__ == '__main__':
    app.run(host=os.getenv('IP'), port=int(os.getenv('PORT')), debug=True)