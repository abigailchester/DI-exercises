from flask import Flask, redirect
from flask import render_template

import database

app = Flask(__name__)


@app.route('/')
def home():
    return render_template("home.html")

@app.route('/add_product')
def login_add_product():
    return render_template("vendor_login.html")

@app.route('/vendor_add_product')
def add_product():
    return render_template("add_product.html")


from flask import request

@app.route('/vendor_add_product', methods=['POST'])
def testing():
    product_name = request.forms.get('product-name')
    price = request.forms.get('price')

    message = "Recieved! Pending approval: product name- " + product_name + ", price: " + price

    return render_template("add_product.html", message=message)

@app.route('/vendor_login')
def vendor_login():
    return render_template("vendor_login.html")

@app.route('/vendor_create_account')
def vendor_create_account():
    return render_template("vendor_create_account.html")

@app.route('/contact')
def contact_us():
    return render_template("contact.html")

@app.route('/products')
def product_page():
    products = database.load_database()
    return render_template("product_page.html", products=products)


@app.route('/coming_soon')
def updated_products():
    added = AddProduct()
    added_products = added.added_products()
    return redirect('/products')
# will finish the forms part tomorrow

@app.route('/product_details/<int:product_id>')
def product_details(product_id):
    products = database.load_database()
    return render_template("product_details.html", product=products[product_id])

if __name__ == "__main__":
    app.run()