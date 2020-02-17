from flask import Flask
from flask import render_template
import ninja

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/ninja')
def ninja_ex():
    return ninja.dark_mode()


if __name__ == "__main__":
    app.run()