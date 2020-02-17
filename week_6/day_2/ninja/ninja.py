from flask import Flask
import datetime
from flask import render_template

def dark_mode():
    now = datetime.datetime.now()
    hour = now.hour
    now_list = now_str.split()

    if hour >= 20 or hour < 8:
        html = render_template("dark_mode.html",now=now, time_list=time_list)
    else:
        html = f"""
            <html>
                <body><h1>the current time is: {now_list[1]}</h1><p>you are in light mode!</p></body>
            </html>
            """
    return html