from flask import Flask, render_template, request, redirect, url_for
from Cart import *
from Wishlist import *
from Receipt import *
from PaymentForm import *
from PaymentInfo import *

app = Flask(__name__)
app.debug = True


@app.route('/')
def home():
    init_products()  # this creates 5 dummy product
    clear_cart()  # this is to clear cart
    product_list = get_products()
    return render_template('home.html', products=product_list)


@app.route('/displayCart/<string:id>')
def display_cart(id):
    cart = get_cart('xxx')
    receipt = get_receipt('xxx')
    receipt.add_to_receipt(cart.get_items())
    receipt.add_to_receipt_history(receipt.get_receipt())
    save_receipt(receipt)
    tot_price = cart.calc_total_price()
    return render_template('displayCart.html', count=cart.get_count(), cart=cart, tot_price=tot_price)


@app.route('/add_cart/<string:id>')
def add_cart(id):
    cart = get_cart('xxx')
    product = get_product(id)
    cart.add_item(product)
    save_cart(cart)
    return redirect(url_for('display_cart', id="xxx"))


@app.route('/remove_from_cart/<string:id>')
def remove_from_cart(id):
    cart = get_cart("xxx")
    product = get_product(id)
    cart.remove_item(product)
    save_cart(cart)
    return redirect(url_for('display_cart', id="xxx"))


@app.route('/add_quantity/<string:id>')
def add_quantity(id):
    cart = get_cart("xxx")
    product = get_product(id)
    cart.add_quantity(product)
    save_cart(cart)
    return redirect(url_for('display_cart', id="xxx"))


@app.route('/sub_quantity/<string:id>')
def sub_quantity(id):
    cart = get_cart("xxx")
    product = get_product(id)
    cart.sub_quantity(product)
    save_cart(cart)
    return redirect(url_for('display_cart', id="xxx"))


@app.route('/displayWishlist/<string:id>')
def display_wishlist(id):
    wishlist = get_wishlist('xxx')
    return render_template('displayWishlist.html', count=wishlist.get_count(), wishlist=wishlist)


@app.route('/add_wishlist/<string:id>')
def add_wishlist(id):
    wishlist = get_wishlist('xxx')
    wl_product = get_product(id)
    wishlist.add_wl_item(wl_product)
    save_wishlist(wishlist)
    return redirect(url_for('display_wishlist', id="xxx"))


@app.route('/remove_from_wishlist/<string:id>')
def remove_from_wishlist(id):
    wishlist = get_wishlist("xxx")
    product = get_product(id)
    wishlist.remove_wl_item(product)
    save_wishlist(wishlist)
    return redirect(url_for('display_wishlist', id="xxx"))


@app.route('/transfer_to_cart/<string:id>')
def transfer_to_cart(id):
    cart = get_cart("xxx")
    wishlist = get_wishlist("xxx")
    product = get_product(id)
    wishlist.remove_wl_item(product)
    cart.add_item(product)
    save_cart(cart)
    save_wishlist(wishlist)
    return redirect(url_for('display_cart', id="xxx"))


@app.route('/createPayment', methods=['GET', 'POST'])
def create_payment():
    payment_form = PaymentForm(request.form)
    if request.method == 'POST' and payment_form.validate():
        payment_info_dict = {}
        db = shelve.open('payment_info.db', 'c')
        try:
            payment_info_dict = db['PaymentInfo']
        except:
            print("Error in retreiving Database.")

        payment_info = PaymentInfo(PaymentInfo.get_payment_id(), payment_form.first_name.data,
                                   payment_form.last_name.data,
                                   payment_form.email.data, payment_form.card_no.data,
                                   payment_form.cvv.data, payment_form.expiry_date.data)
        payment_info_dict[payment_info.get_payment_id()] = payment_info
        db['PaymentInfo'] = payment_info_dict
        db.close()
        return render_template('PaymentForm.html', form=payment_form)
    return render_template('PaymentForm.html', form=payment_form)


if __name__ == '__main__':
    app.run()
