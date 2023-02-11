from wtforms import Form, StringField, IntegerField, validators, ValidationError
from wtforms.fields import EmailField, DateField
import datetime


def expiry_date_validate(form, field):
    if field.data < datetime.date.today():
        raise ValidationError("Card Already Expired.")
    elif field.data.year - datetime.date.today().year >= 5:
        raise ValidationError("Ivalid Expiry Date")  # Cards have maximum time of 3-5 years.


def card_no_validate(min_value, max_value):
    def _card_no_validate(form, field):
        if not min_value <= field.data <= max_value:
            raise ValidationError("Invalid Card no.")

    return _card_no_validate # Card number has to be 16 Digits


def cvv_validate(min_value, max_value):
    def _cvv_validate(form, field):
        if not min_value <= field.data <= max_value:
            raise ValidationError("Invalid CVV.")

    return _cvv_validate # CVV has to be 3 digits


class MakePaymentForm(Form):
    first_name = StringField('First Name', [validators.Length(min=1, max=150), validators.DataRequired()])
    last_name = StringField('Last Name', [validators.Length(min=1, max=150), validators.DataRequired()])
    email = EmailField("Email", [validators.DataRequired("Please enter your email address."), validators.Email()])
    card_no = IntegerField("Credit Card Number:",
                           validators=[card_no_validate(1000000000000000, 9999999999999999), validators.DataRequired()])
    cvv = IntegerField("CVV", validators=[cvv_validate(100, 900), validators.DataRequired()])
    expiry_date = DateField("Expiry Date:", [expiry_date_validate])
