from flask import Flask
from flask import Flask
from flask import request
from flask import render_template


app = Flask(__name__, static_url_path='', static_folder='frontscript', template_folder="templates")
@app.route("/")
def index():
    return render_template("index.html") 

def results():
     return render_template("results.html")

if __name__ == "__main__":
    app.run(port=4000)
    print("webside gesterted")