import shelve
class PaymentInfo:
    def __init__(self, id):
        self.__id = id
        self.__payment_info = []

    def set_id(self, id):
        self.__id = id

    def get_id(self):
        return self.__id

    def set_payment_info(self, payment_info):
        self.__payment_info = payment_info

    def get_payment_info(self):
        return self.__payment_info

    def set_payment(self, paymentItem):
        self.__payment_info.append(paymentItem)

class PaymentItem:
    def __init__(self, payment_info_data):
        self.__payment_info_data = payment_info_data

    def set_payment_info_data(self, payment_info_data):
        self.__payment_info_data = payment_info_data

    def get_ppayment_info_data(self):
        return self.__payment_info_data

paymentinfo = shelve.open('payment')
def get_payment(id):
    if id in paymentinfo:
        return paymentinfo[id]
    else:
        payment = PaymentInfo(id)
        paymentinfo[id] = payment
        return payment

def save_payment_info(payment):
    paymentinfo[payment.get_id()] = payment
    print(payment.get_id())
    print(payment.get_items())