from Product import *
import shelve

class Cart:
    def __init__(self, id):
        self.__id = id
        self.__items = [] # Contains product and quanitty

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

class CartItem:
    def __init__(self, product, quantity):
        self.__product = product # Stores all product information here
        self.__quantity = quantity

# get.name from product from Khansa's class.
    def set_product(self, product):
        self.__product = product

    def get_product(self):
        return self.__product

    def set_quantity(self, quantity):
        self.__quantity = quantity

    def get_quantity(self):
        return self.__quantity

def get_product(product_key):
    product = Product("Milk", 200, "Food", 3.99, 4.3, "")
    return product

def get_cart(id):
    db = shelve.open("cart.db", flag='r')
