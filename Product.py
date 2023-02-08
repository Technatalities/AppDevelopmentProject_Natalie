class Product:
    #count_id = 0

    def __init__(self, count_id, name, stock, category, price, rating, picture):
        #Product.count_id += 1
        #self.__product_id = Product.count_id
        self.__product_id = count_id
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