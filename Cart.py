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

    def remove_item(self, product):
        found = False
        for item in self.__items:
            if item.get_product().get_product_id() == product.get_product_id():
                self.__items.remove(item)
                found = True
        if not found:
            print("Item does not exist in cart.")

    def add_quantity(self, product):
        found = False
        for item in self.__items:
            if item.get_product().get_product_id() == product.get_product_id():
                item.add_count()
                found = True
        if not found:
            return False

    def sub_quantity(self, product):
        found = False
        for item in self.__items:
            if item.get_product().get_product_id() == product.get_product_id():
                if item.get_quantity() == 1:
                    self.__items.remove(item)
                    found = True
                elif item.get_quantity() >= 1:
                    item.sub_count()
                    found = True
        if not found:
            return False

    def calc_total_price(self):
        total_price = 0
        for item in self.__items:
            total_price += item.get_product().get_price() * item.get_quantity()
        return total_price

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


def get_cart(id):
    carts = shelve.open('cart')
    if id in carts:
        return carts[id]
    else:
        cart = Cart(id)
        carts[id] = cart
        return cart
    carts.close()


def delete_cart(id):
    carts = shelve.open('cart')
    if id in carts:
        del carts[id]
    carts.close()

def clear_cart():
    carts = shelve.open('cart')
    list = carts.keys()
    for i in list:
        del carts[i]
    carts.close()

def save_cart(cart):
    carts = shelve.open('cart')
    carts[cart.get_id()] = cart
    carts.close()