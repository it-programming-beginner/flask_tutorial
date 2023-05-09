from flask import Flask
from flask import render_template
from flask import request
from flask import redirect
import sqlite3
import os

app = Flask(__name__)

@app.route('/', methods=["GET"])
def list():
    con = sqlite3.connect('test.db')
    cur = con.execute("select * from todos")
    todos=[]
    for row in cur:
        todo ={'idx': row[0], 'todo': row[1], 'status':row[2]}
        todos.append(todo)
    return render_template("view_1.html", todos=todos)

@app.route('/add', methods=["POST"])
def add():
    if not request.form['name']:
        return redirect("/")
    con = sqlite3.connect('test.db')
    con.execute("insert into todos(todo) values (?)", (request.form['name'],))
    con.commit()
    return redirect("/")
    
@app.route('/delete', methods=["POST"])
def delete():
    con = sqlite3.connect('test.db')
    for e in request.form.getlist('target'):
        con.execute("delete from todos where id = ?", (e,))
    con.commit()
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True, port=80)