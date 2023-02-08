from wtforms import Form, validators, ValidationError
from wtforms.fields import IntegerField

def validate_quantity(min_value, max_value):
    def _validate_quantity(form, field):
        if not min_value <= field.data <= max_value:
            raise ValidationError(f'Price must be between {min_value} and {max_value}.')
    return _validate_quantity
def validate_quantity_warning(form, field):
    if field.data <= 0:
        raise ValidationError("Quantity cannot be less than 1.")
class QuantityForm(Form):
    quantity = IntegerField('Quantity', [validators.DataRequired()])
    stock = IntegerField('Stock', validators=[validate_quantity(1, 50), validators.DataRequired(),
                                              validate_quantity_warning])