from flask_wtf import FlaskForm
from wtforms import StringField,IntegerField,FloatField,SelectField,SelectMultipleField
from wtforms.validators import InputRequired, Email, Optional,Length,url

class CreateItem(FlaskForm):
  name=StringField('Name',validators=[InputRequired()])
  price=FloatField('Price',validators=[InputRequired()])
  quantity=IntegerField('Quantity',validators=[InputRequired()])
  sku=IntegerField('SKU',validators=[InputRequired()])
  warehouse_id=SelectField('Warehouse')

class CreateWarehouse(FlaskForm):
  name=StringField('Name',validators=[InputRequired()])


class CreateAssignment(FlaskForm):
  items_sku=IntegerField('Items SKU',validators=[InputRequired()])
  warehouse_name=StringField('Warehouse Name',validators=[InputRequired()])
  quantity=IntegerField('Quantity',validators=[InputRequired()])
class EditAssignment(FlaskForm):
  warehouse_name=StringField('Warehouse Name',validators=[InputRequired()])
  quantity=IntegerField('Quantity',validators=[InputRequired()])
