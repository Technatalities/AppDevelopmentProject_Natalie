import shelve
import uuid

class Product:
    def __init__(self, name, stock, category, price, rating, picture):
        self.__product_id = str(uuid.uuid4())
        self.__name = name
        self.__stock = stock
        self.__category = category
        self.__price = price
        self.__rating = rating
        self.__picture = picture


    def get_product_id(self):
        return self.__product_id

    def get_name(self):
        return self.__name

    def get_stock(self):
        return self.__stock

    def get_category(self):
        return self.__category

    def get_price(self):
        return self.__price

    def get_rating(self):
        return self.__rating

    def get_picture(self):
        return self.__picture

    def set_product_id(self, product_id):
        self.__product_id = product_id

    def set_name(self, name):
        self.__name = name

    def set_stock(self, stock):
        self.__stock = stock

    def set_category(self, category):
        self.__category = category

    def set_price(self, price):
        self.__price = price

    def set_rating(self, rating):
        self.__rating = rating

    def set_picture(self, picture):
        self.__picture = picture

# key - product id, value - product object


def create_product(product):
    products = shelve.open('product')
    # this function does not check for existing product
    products[product.get_product_id()] = product
    products.close()

def get_product(id):
    products = shelve.open('product')
    if id in products:
        return products[id]
    products.close()

def get_products():
    products = shelve.open('product')
    # return a list of products
    key_list = list(products.keys())
    x = []
    for i in key_list:
        x.append(products[i])
    products.close()
    return x


def clear_products():
    products = shelve.open('product')
    key_list = list(products.keys())
    x = []
    for i in key_list:
        del products[i]
    products.close()

def init_products():
    products = shelve.open('product')
    for i in range(1,5):
        p = Product("p"+str(i), 10, "cat"+str(i), 1.5+i, 5, "")
        create_product(p)
    products.close()