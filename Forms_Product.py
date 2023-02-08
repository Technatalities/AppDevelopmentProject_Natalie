from wtforms import Form, StringField, RadioField, SelectField, TextAreaField, validators, ValidationError, IntegerField, DecimalField


# from flask_wtf.file import FileField, FileRequired, FileAllowed
# have to install (pip install Flask-WTF)


def validate_price_range(min_value, max_value):
    def _validate_price_range(form, field):
        if not min_value <= field.data <= max_value:
            raise ValidationError(f'Price must be between {min_value} and {max_value}.')
    return _validate_price_range


def validate_stock_range(min_value, max_value):
    def _validate_stock_range(form, field):
        if not min_value <= field.data <= max_value:
            raise ValidationError(f'Stock must be between {min_value} and {max_value}.')
    return _validate_stock_range


def validate_quantity_warning(form, field):
    if field.data <= 50:
        raise ValidationError("Warning: Quantity is low.")


def name_validator(form, field):
    if not field.data.isalpha():
        raise validators.ValidationError("Name can only contain letters.")


class CreateProductForm(Form):
    name = StringField('Product Name', [validators.InputRequired(), name_validator])
    stock = IntegerField('Stock', validators=[validate_stock_range(1, 500), validators.DataRequired(), validate_quantity_warning])
    category = SelectField('Category', [validators.DataRequired()],
                           choices=[("", 'Select'), ('F', 'Food'), ('D', 'Drinks'), ('C', 'Clothes')], default='')
    price = DecimalField('Price($)', validators=[validate_price_range(1, 100), validators.DataRequired()])

    rating = RadioField('Rating', choices=[('5', '5'), ('4', '4'), ('3', '3'), ('2', '2'), ('1', '1')], default='5')
    picture = TextAreaField('Picture', [validators.Optional()])
    # picture = FileField('Picture', validators=[FileRequired(), FileAllowed(['jpg', 'png', 'Images only!'])])

