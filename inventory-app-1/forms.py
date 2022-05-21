from flask_wtf import FlaskForm
from wtforms import StringField,IntegerField,FloatField,SelectField,SelectMultipleField
from wtforms.validators import InputRequired, Email, Optional,Length,url

class CreateItem(FlaskForm):
  name=StringField('Name',validators=[InputRequired()])
  price=FloatField('Price',validators=[InputRequired()])
  total_quantity=IntegerField('Total Quantity',validators=[InputRequired()])
  sku=IntegerField('SKU',validators=[InputRequired()])

class CreateWarehouse(FlaskForm):
  name=StringField('Name',validators=[InputRequired()])


class CreateAssignment(FlaskForm):
  warehouse_name=SelectField('Warehouse')
  quantity=IntegerField('Quantity',validators=[InputRequired()])
class EditAssignment(FlaskForm):
  warehouse_name=SelectField('Warehouse')
  quantity=IntegerField('Quantity',validators=[InputRequired()])
