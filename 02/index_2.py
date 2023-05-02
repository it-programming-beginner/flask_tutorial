from flask import Flask
from flask import render_template
import sqlite3

app = Flask(__name__)

@app.route('/', methods=["GET"])
def list():
    con = sqlite3.connect('test.db')
    cur = con.execute("select * from todos")
    todos={}
    for row in cur:
        todos[row[0]]=row[1]
    return render_template("view_2.html", todos=todos)

if __name__ == "__main__":
    app.run(debug=True, port=80)