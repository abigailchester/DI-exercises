from flask import Flask, render_template, request, redirect
import form

app = Flask(__name__)
app.config['SECRET_KEY'] = 'you-will-never-guess'

@app.route('/')
def location_color():
    return render_template('home.html')

@app.route("/formpage")
def form_page():
    shoe_stock = form.load_database()
    return render_template('form.html', shoe_stock=shoe_stock)


@app.route('/formresult', methods=['POST', 'GET'])
def result():

    if request.method == 'POST':
        result = request.form


    return render_template("formresult.html", result=result)



@app.route('/signup', methods = ['POST'])
def signup():
    email = request.form['email']
    print("The email address is '" + email + "'")
    return redirect('/')

if __name__ == ("__main__"):
    app.run()






# Our client has already one file to store the products.
#
# Here are the functionalities that the client wants for his website.
# 1. Be able to ask the customer for the location of the wanted store (1 possibility)
# 2. Be able to ask the customer for the color wanted (1 possibility)
# 3. Be able to inform the user of the name, brand, price, and number of shoes in the particular store, in the particular color. (Note: the number is the number of pair)

# 4. Be able to ask the customer for his order (brand, name, quantity) and sum it up. All the orders have to be saved permanently. A customer can have more than one order.
# 5. Be able to change permanently the number of pair of shoes available in the store, depending on the quantity ordered.
# 6. If the user doesn’t give a quantity (and in order to not get stuck), the quantity ordered should be one by default.
# 7. Be able to see the customers’ orders only if the status of the user of the website is “Administrator”.

# One of our clients, liked the functionalities we created for the Shoe Store Website. They want the same, but they also want special functionalities:
# 1. They want their customers to be able to search for a brand and/or name, and then inform them of the available shoes for the word typed.
# 2. Even if their customers, don’t type the whole name of a brand and/or name, they still want to be able to inform them of the available shoes for the word typed.
# 3. They want their customers to be able to give a review on their order and to save it permanently. The result has to be translated into stars, depending on the amount of positive or negative words used by the customer.
# Example: “Very nice shoes, very pretty, very comfortable” will be translated by 3 stars (***)
# Example: “Very nice shoes, very pretty, but not comfortable” will be translated by 2 stars (**)