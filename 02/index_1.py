from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/', methods=["GET"])
def list():
    todos={0: "Pythonを勉強する", 1: "ランニングをする", 2: "レポート課題を提出する"}
    return render_template("view_1.html", todos=todos)

if __name__ == "__main__":
    app.run(debug=True, port=80)