from flask_wtf import FlaskForm
from wtforms import StringField,IntegerField,FloatField,SelectField,SelectMultipleField
from wtforms.validators import InputRequired, Email, Optional,Length,url

class CreateItem(FlaskForm):
  ''' This form is used both to UPDATE and CREATE items. All fields are required in order to process a submission. '''    
  name=StringField('Name',validators=[InputRequired()])
  price=FloatField('Price',validators=[InputRequired()])
  total_quantity=IntegerField('Total Quantity',validators=[InputRequired()])
  sku=IntegerField('SKU',validators=[InputRequired()])

class CreateWarehouse(FlaskForm):
  ''' This form will handle the creation of warehouses '''    
  name=StringField('Name',validators=[InputRequired()])


class CreateAssignment(FlaskForm):
  ''' This form will update as well as create inventory assignments  '''    
  warehouse_name=SelectField('Warehouse')
  quantity=IntegerField('Quantity',validators=[InputRequired()])
