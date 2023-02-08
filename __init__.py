from flask import Flask, render_template, request, redirect, url_for
from Cart import *
from Cart_Form import *

app = Flask(__name__)
app.debug = True

@app.route('/')
def home():
    with shelve.open('product.db') as db:
        db2 = db['Product']
        print(db2)
    return render_template('home.html')

@app.route('/displayCart/<int:id>', methods = ["POST"])
def display_cart():
    cart_id = id
    cart_db = shelve.open('shopping_cart.db', 'c')
    print(cart_db)
    item_list = Cart.get_items(cart_db(id))
    return render_template('displayCart.html', count=len(item_list), item_list = item_list)

@app.route('/addCart/<id>', methods = ["GET", "POST"])
def add_to_cart():
    quantity_form = QuantityForm(request.form)
    quantity = quantity_form.quantity.data
    product_key = str(id)
    product_db = shelve.open("products.db", flag="r")
    Cart.product = product_db['product_key']

    item = get_product(product_key)

    cartItem = CartItem(item, quantity)
    Cart.set_item(cartItem=cartItem)



# @app.route('/add_to_cart', methods=['POST'])
# def add_to_cart():
#     product_key = request.form.get("product_key")
#     db = shelve.open("products.db", flag='r')
#     product = get_product(product_key)
#     if product_key in db:
#         product = db[product_key]
#     id = "123"
#     cart = get_cart(id)
#     cart = cart_db['Cart']
#     if product['key'] in cart:
#         cart[product['key']]['quantity'] += 1
#     else:
#         cart[product['key']] = {'name': product['name'], 'category': product['category'], 'price': product['price'], 'quantity': 1}
#         cart_db['Cart'] = cart
#         cart_db.close()
#         db.close()
#         return "Product added to cart successfully"
#     else:
#         db.close()
#         return "Error: Invalid product key"


# @app.route('/displayCart', methods=['GET', 'POST'])
# def display_cart():
#     cart_db = shelve.open('shopping_cart.db', 'c')
#     print(cart_db)
#     cart_list = []
#     for key in cart_db:
#         item = cart_db.get(key)
#         cart_list.append(item)
#     cart_db.close()
#     return render_template('displayCart.html', count=len(cart_list), cart_list=cart_list)
#
#
# @app.route('/addQuantity/<int:id>', methods=['POST', 'GET'])
# def add_quantity(id):
#     product_key = str(id)
#     cart_db = shelve.open("shopping_cart.db", flag='c')
#     cart = cart_db['Cart'] if 'Cart' in cart_db else {}
#     if product_key in cart:
#         cart[product_key][int('quantity')] += 1
#         cart_db['Cart'] = cart
#         cart_db.close()
#         return "Cart updated successfully"
#     else:
#         cart_db.close()
#         return "Error: Invalid product key"
#
# @app.route('/subtractQuantity/<int:id>', methods=['POST', 'GET'])
# def subtract_quantity(id):
#     product_key = str(id)
#     cart_db = shelve.open("shopping_cart.db", flag='c')
#     cart = cart_db['Cart'] if 'Cart' in cart_db else {}
#     if product_key in cart:
#         cart[product_key][int('quantity')] -= 1
#         cart_db['Cart'] = cart
#         cart_db.close()
#         return "Cart updated successfully"
#     else:
#         cart_db.close()
#         return "Error: Invalid product key"
#
# @app.route('/delete_cart/<int:id>', methods = ["POST", "GET"])
# def remove_from_cart(id):
#     product_key = str(id)
#     print(product_key)
#     cart_db = shelve.open("shopping_cart.db", flag='c')
#     if product_key in cart_db.keys():
#         print(cart_db.keys())
#         del cart_db[product_key]
#         cart_db.close()
#         return redirect(url_for("display_cart"))
#     else:
#         cart_db.close()
#         return "Error: Invalid product key"
#
# @app.route('/invoice', methods=['GET', 'POST'])
# def invoice():
#     form = PaymentForm()
#     cart_db = shelve.open('shopping_cart.db', 'r')
#     cart = cart_db['Cart'] if 'Cart' in cart_db else {}
#     cart_db.close()
#     total_cost = sum(item['price'] * item['quantity'] for item in cart.values())
#     if form.validate_on_submit():
#         cart_db = shelve.open('shopping_cart.db', 'w')
#         cart_db['Cart'] = {}
#         cart_db.close()
#         return redirect(url_for('success'))
#     return render_template('invoice.html', form=form, cart=cart, total_cost=total_cost)

if __name__ == '__main__':
    app.run()
