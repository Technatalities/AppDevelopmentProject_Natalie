import shelve
from wtforms import Form, SelectField

class PaymentForm(Form):
    payment_method = SelectField('Payment Method', choices=[('credit_card', 'Credit Card'), ('paypal', 'Paypal')])
