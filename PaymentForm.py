from wtforms import Form, StringField, IntegerField, validators, ValidationError
from wtforms.fields import EmailField, DateField
import datetime


def expiry_date_validate(form, field):
    if field.data < datetime.date.today():
        raise ValidationError("Card Already Expired.")
    elif field.data.year - datetime.date.today().year >= 5:
        raise ValidationError("Ivalid Expiry Date")  # Cards have maximum time of 3-5 years.


class MakePaymentForm(Form):
    first_name = StringField('First Name', [validators.Length(min=1, max=150), validators.DataRequired()])
    last_name = StringField('Last Name', [validators.Length(min=1, max=150), validators.DataRequired()])
    email = EmailField("Email", [validators.DataRequired("Please enter your email address."), validators.Email()])
    card_no = IntegerField("Credit Card Number:", [validators.DataRequired()])
    cvv = IntegerField("CVV", [validators.DataRequired()])
    expiry_date = DateField("Expiry Date:", [expiry_date_validate])
