from flask import Flask, render_template, redirect, request
from jsondb import JsonDB


"""
import from jsondb import JsonDB
db = JsonDB('db.json')
db.load()
x = db.get('x', 0)
x += 1
db.set('x', x)
db.save()
"""

dictionary = {1:1}







app = Flask(__name__)
db = JsonDB('db.json')
db.load()

@app.route('/', methods=['GET', 'POST'])

def index():
    from book import pyble

    to_do = db.get('todos')
    if request.method == 'POST':
        new_task = request.form['input_text']
        priority = request.form['button']
        print(priority, new_task)
        task_dict = {'text': new_task, 'priority': priority}
        to_do.append(task_dict)
        db.set("todos", to_do)
        db.save()
        return redirect('/')
    return render_template("index.html", bible=bible)


app.run(debug=True)

# https://avocado-jc.github.io/ 