import shelve
class Receipt:
    def __init__(self, id):
        self.__id = id
        self.__receipt = []
        self.__receipt_history = []

    def set_id(self, id):
        self.__id = id

    def get_id(self):
        return self.__id

    def set_receipt(self, receipt):
        self.__receipt = receipt

    def get_receipt(self):
        return self.__receipt

    def set_receipt_history(self, receipt_history):
        self.__receipt_history = receipt_history

    def get_receipt_history(self):
        return self.__receipt_history

    def set_receipt_item(self, receiptItem):
        self.__receipt.append(receiptItem)

    def set_receipt_history_item(self, receipt):
        self.__receipt_history.append(receipt)

    def add_to_receipt(self, items):
        i = ReceiptItem(items)
        self.__receipt.append(i)

    def clear_receipt(self, receipt):
        receipt.clear()

    def add_to_receipt_history(self, items):
        i = ReceiptItem(items)
        self.__receipt_history.append(i)

    def calc_tot_price(self):
        for receipt_item in self.__receipt:
            tot_price = 0
            tot_price += receipt_item.get_price() * receipt_item.get_quantity()
            return tot_price


class ReceiptItem:
    def __init__(self, items):
        self.__items = items

    def set_items(self, items):
        self.__items = items

    def get_items(self):
        return self.__items


receipts = shelve.open('receipt')
def get_receipt(id):
    if id in receipts:
        return receipts[id]
    else:
        receipt = Receipt(id)
        receipts[id] = receipt
        return receipt

def clear_receipt():
    receipt_list = receipts.keys()
    for i in receipt_list:
        del receipts[i]


def save_receipt(receipt):
    receipts[receipt.get_id()] = receipt