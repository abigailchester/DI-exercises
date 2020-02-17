from datetime import datetime

from flask import Flask
from flask import request
from flask import render_template, render_template_string
import datetime
import random

app = Flask(__name__)

@app.route('/')
def display_countdown():
    return 'here is the countdown'

@app.route('/abby')
def display_this():
    html = render_template('gold.html')
    return html

dt = datetime.datetime.now()
futuredate = datetime.datetime.strptime('Jan 1 2021  13:33', '%b %d %Y %H:%M')
count = int((futuredate - dt).total_seconds())
days = count // 86400
hours = (count - days * 86400) // 3600
minutes = (count - days * 86400 - hours * 3600) // 60
seconds = count - days * 86400 - hours * 3600 - minutes * 60


# @app.route('/time/<int:n>')
@app.route('/time')
def countdown():
    return f"current date and time is: {dt} and the countdown until January 1st, 2021 is: {days} days, {hours} hours, {minutes} minutes, and {seconds} seconds, as of the time of running this program."

@app.route('/luckgame/<int:number>')
def choose_number(number):
    n = random.randint(1,100)
    if number == n:
        return "success"
    else:
        return f"nope, the number was {n}"


if __name__ == "__main__":
    app.run()