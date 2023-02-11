import uuid
class PaymentInfo:
    def __init__(self, first_name, last_name, email, card_no, cvv, expiry_date):
        self.__payment_id = str(uuid.uuid4())
        self.__first_name = first_name
        self.__last_name = last_name
        self.__email = email
        self.__card_no = card_no
        self.__cvv = cvv
        self.__expiry_date = expiry_date

    def get_payment_id(self):
        return self.__payment_id
    def set_first_name(self, first_name):
        self.__first_name = first_name
    def get_fisrt_name(self):
        return self.__first_name

    def set_last_name(self, last_name):
        self.__last_name = last_name

    def get_last_name(self):
        return self.__last_name

    def set_email(self, email):
        self.__email = email

    def get_email(self):
        return self.__email

    def set_card_no(self, card_no):
        self.__card_no = card_no

    def get_card_no(self):
        return self.__card_no

    def set_cvv(self, cvv):
        self.__cvv = cvv

    def get_cvv(self):
        return self.__cvv

    def set_expiry_date(self, expiry_date):
        self.__expiry_date = expiry_date

    def get_expiry_date(self):
        return self.__expiry_date
