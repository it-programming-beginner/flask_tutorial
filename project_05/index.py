from flask import Blueprint
from flask import render_template
from flask import request
from flask import redirect, url_for
from flask_login import login_required
import sqlite3

# app = Flask(__name__)
index = Blueprint('index', __name__)

@index.route('/', methods=["GET"])
@login_required
def list():
    selected_tab = request.args.get('selected_tab') if request.args.get('selected_tab') else 'all'
    con = sqlite3.connect('test.db')
    cur = con.execute("select * from todos")
    todos=[]
    for row in cur:
        todo ={'idx': row[0], 'todo': row[1], 'status':row[2]}
        todos.append(todo)
    return render_template("view.html", todos=todos, selected_tab=selected_tab)

@index.route('/add', methods=["POST"])
@login_required
def add():
    if not request.form['name']:
        return redirect("/")
    con = sqlite3.connect('test.db')
    con.execute("insert into todos(todo) values (?)", (request.form['name'],))
    con.commit()
    return redirect(url_for('index.list'))
    
@index.route('/delete', methods=["POST"])
@login_required
def delete():
    con = sqlite3.connect('test.db')
    for e in request.form.getlist('target'):
        con.execute("delete from todos where id = ?", (e,))
    con.commit()
    return redirect(url_for('index.list', selected_tab=request.form['selected_tab']))

@index.route('/complete', methods=["POST"])
@login_required
def complete():
    con = sqlite3.connect('test.db')
    for e in request.form.getlist('target'):
        con.execute("update todos set status = '1' where id = ?", (e,))
    con.commit()
    return redirect(url_for('index.list', selected_tab=request.form['selected_tab']))

@index.route('/undo', methods=["POST"])
@login_required
def undo():
    con = sqlite3.connect('test.db')
    for e in request.form.getlist('target'):
        con.execute("update todos set status = '0' where id = ?", (e,))
    con.commit()
    return redirect(url_for('index.list', selected_tab=request.form['selected_tab']))

# if __name__ == "__main__":
#     app.run(debug=True, port=80)