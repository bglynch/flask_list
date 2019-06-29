import os
from flask import Flask, redirect, render_template, request
from random import choice
import json

app = Flask(__name__)

welcome_message = ["Hi", "Hello", 'Bonjour', "Ciao"]


def load_list(filename):
    if os.path.exists(filename):
        with open(filename, "r") as f: 
            data = f.read()
            items = json.loads(data)   #json.loads task string and turns it into a list
    else:
        items = []
        
    return items
 
def save_list(items, filename):
    with open("data/list.json", "w") as f: #sinilar code as previous example, except file auto closes
        data = json.dumps(items)    #dump our items data into a string
        f.write(data)

# if including variables in the link, must be included in function as arguements

@app.route("/")
def get_index():
    items = load_list("data/list.json")
    welcome = choice(welcome_message)
    return render_template("index.html", msg=welcome, tasks = items)  #tasks in HTML matches items in PY

@app.route("/new_task", methods = ['POST'])
def create_a_task():
    task = {
        'name': request.form['task_to_do'],
        'done': False
    }
    
    items = load_list("data/list.json")    
    items.append(task)
    save_list(items, "data/list.json")
    
    return redirect('/')

@app.route("/toggle", methods = ['POST'])
def toggle_status():
    task = request.form['toggle']
    return "You clicked" + task


if __name__ == '__main__':
    app.run(host=os.getenv('IP'), port=int(os.getenv('PORT')), debug=True)