from Product import *
import shelve

class Cart:
    def __init__(self, id):
        self.__id = id
        self.__items = []  # Contains product IDs and quantity

    def set_id(self, id):
        self.__id = id

    def get_id(self):
        return self.__id

    def set_items(self, items):
        self.__items = items

    def get_items(self):
        return self.__items

    def set_item(self, cartItem):
        self.__items.append(cartItem)

    def get_count(self):
        return len(self.__items)

    def add_item(self, product):
        found = False
        for item in self.__items:
            if item.get_product().get_product_id() == product.get_product_id():
                item.add_count()
                found = True
        if not found:
            i = CartItem(product, 1)
            self.__items.append(i)

    def add_quantity(self, product):
        found = False
        for item in self.__items:
            if item.get_product().get_product_id() == product.get_product_id():
                item.add_count()
                found = True
        if not found:
            print("Product not found in Cart.")

    def sub_quantity(self, product):
        found = False
        for item in self.__items:
            if item.get_product().get_product_id() == product.get_product_id():
                item.sub_count()
                found = True
            if not found:
                print("Product not found in Cart.")

class CartItem:
    def __init__(self, product, quantity):
        self.__product = product
        self.__quantity = quantity

    def set_product(self, product):
        self.__product = product

    def get_product(self):
        return self.__product

    def set_quantity(self, quantity):
        self.__quantity = quantity

    def get_quantity(self):
        return self.__quantity

    def add_count(self):
        self.__quantity = self.__quantity + 1
    def sub_count(self):
        self.__quantity = self.__quantity - 1


carts = shelve.open('cart')
def get_cart(id):
    if id in carts:
        return carts[id]
    else:
        cart = Cart(id)
        carts[id] = cart
        return cart


def delete_cart(id):
    if id in carts:
        del carts[id]

# def del_cart(cart):
#     carts[cart.get_id()] = cart

def clear_cart():
    list = carts.keys()
    for i in list:
        del carts[i]

def save_cart(cart):
    carts[cart.get_id()] = cart
    print(cart.get_id())
    print(cart.get_items())