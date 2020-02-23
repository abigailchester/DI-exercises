import json

def load_database(src_file='stock.json'):
    with open(src_file, 'r') as f:
        data = json.load(f)
    return data

def create_order(dst_file='orders.json'):
    with open(dst_file, 'w') as f:
        json.dump(data, f)



# import flask_wtf
# import wtforms
# from wtforms import validators

# class OrderForm(flask_wtf.FlaskForm):
#
#     brandname     = wtforms.StringField("Brand Name")
#     productname      = wtforms.StringField("Product Name")
#     quantity      = wtforms.IntegerField("Quantity")
#     submit   = wtforms.SubmitField("Submit")

# my_form = OrderForm()