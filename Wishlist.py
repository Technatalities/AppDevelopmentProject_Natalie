from Product import *
import shelve
class Wishlist:
    def __init__(self, id):
        self.__id = id
        self.__wl_items = []  # Contains product IDs and quantity

    def set_id(self, id):
        self.__id = id

    def get_id(self):
        return self.__id

    def set_wl_items(self, wl_items):
        self.__wl_items = wl_items

    def get_wl_items(self):
        return self.__wl_items

    def set_wl_item(self, wishlistItem):
        self.__wl_items.append(wishlistItem)

    def get_count(self):
        return len(self.__wl_items)

    def add_wl_item(self, product):
        found = False
        for wl_item in self.__wl_items:
            if wl_item.get_product().get_product_id() == product.get_product_id():
                print("Wishlist Item already there.")
                found = True
        if not found:
            i = WishlistItem(product)
            self.__wl_items.append(i)

class WishlistItem:
    def __init__(self, product):
        self.__product = product

    def set_product(self, product):
        self.__product = product

    def get_product(self):
        return self.__product

wishlists = shelve.open('wishlist')
def get_wishlist(id):
    if id in wishlists:
        return wishlists[id]
    else:
        wishlist = Wishlist(id)
        wishlists[id] = wishlist
        return wishlist

def delete_wishlist(id):
    if id in wishlists:
        del wishlists[id]

def clear_wishlist():
    list = wishlists.keys()
    for i in list:
        del wishlists[i]

def save_wishlist(wishlist):
    wishlists[wishlist.get_id()] = wishlist
    print(wishlist.get_id())
    print(wishlist.get_wl_items())