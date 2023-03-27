from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, IntegerField
from wtforms.validators import DataRequired, Email

class CustomerForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])

class InvoiceForm(FlaskForm):
    amount = FloatField('Amount', validators=[DataRequired()])
    customer_id = IntegerField('Customer ID', validators=[DataRequired()])
    item_name = StringField('Item Name', validators=[DataRequired()])
    item_quantity = IntegerField('Item Quantity', validators=[DataRequired()])
    item_price = FloatField('Item Price', validators=[DataRequired()])
