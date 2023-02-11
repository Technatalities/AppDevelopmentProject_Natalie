import shelve

import Cart
class PaymentItems:
    def __init__(self, id):
        self.__id = id
        self.__payment_items = []  # Contains Payment Items

    def set_id(self, id):
        self.__id = id

    def get_id(self):
        return self.__id

    def set_payment_items(self, payment_items):
        self.__payment_items = payment_items

    def get_payment_items(self):
        return self.__payment_items

    def get_count(self):
        return len(self.__items)

    def add_payment_items(self, payment_items):
        self.__payment_items = payment_items.append(Cart.get_cart(id).get_items())