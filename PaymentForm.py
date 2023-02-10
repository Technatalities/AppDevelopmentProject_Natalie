from wtforms import Form, StringField, RadioField, SelectField, TextAreaField, IntegerField, validators
from wtforms.fields import EmailField, DateField

class PaymentForm(Form):
    first_name = StringField('First Name', [validators.Length(min=1, max=150), validators.DataRequired()])
    last_name = StringField('Last Name', [validators.Length(min=1, max=150), validators.DataRequired()])
    email = EmailField()
    card_no = IntegerField()
    cvv = IntegerField()
    expiry_date = DateField()
