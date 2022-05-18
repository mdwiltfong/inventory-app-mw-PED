from flask_wtf import FlaskForm
from wtforms import StringField,IntegerField,FloatField,SelectField
from wtforms.validators import InputRequired

class CreateItem(FlaskForm):
  ''' WTForms class for creating an inventory item '''
  name=StringField('Name',validators=[InputRequired()])
  price=FloatField('Price',validators=[InputRequired()])
  quantity=IntegerField('Quantity',validators=[InputRequired()])
  sku=IntegerField('SKU',validators=[InputRequired()])
  warehouse=SelectField('Warehouse')



  
class CreateWarehouse(FlaskForm):
  ''' WTforms class for creating a Warehouse '''
  name=StringField('Name',validators=[InputRequired()])
  