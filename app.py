from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)



@app.route("/")
def index():
    return "Hello world!"

@app.route("/data")
def data():
    date = str(datetime.now())
    return render_template("data.html", date=date)

if __name__ == '__main__':
    app.run(debug=True)