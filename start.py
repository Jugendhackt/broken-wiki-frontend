from flask import Flask
from flask import Flask
from flask import request
from flask import render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html") 

@app.route("/credits")
def credits():
    return render_template("credits.html") 

if __name__ == "__main__":
    app.run(port=4000)
    print("webside gesterted")