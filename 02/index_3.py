from flask import Flask
from flask import render_template
from flask import request
from flask import redirect
import sqlite3

app = Flask(__name__)

@app.route('/', methods=["GET"])
def list():
    con = sqlite3.connect('test.db')
    cur = con.execute("select * from todos")
    todos={}
    for row in cur:
        todos[row[0]]=row[1]
    return render_template("view_3.html", todos=todos)

@app.route('/add', methods=["POST"])
def add():
    if not request.form['name']:
        return redirect("/")
    con = sqlite3.connect('test.db')
    con.execute("insert into todos(todo) values (?)", (request.form['name'],))
    con.commit()
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True, port=80)