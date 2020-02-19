import json


def load_database(src_file='my_file.json'):
    with open(src_file, 'r') as f:
        data = json.load(f)
    return data

def added_products(src_file='added.json'):
    with open(src_file, 'w') as f:
        json.dump(added_products, f)
    return added_products

import flask_wtf
import wtforms

class AddProduct(flask_wtf.FlaskForm):
    name     = wtforms.StringField("Name")
    price    = wtforms.StringField("Price")
    submit   = wtforms.SubmitField("Submit")