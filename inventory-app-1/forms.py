from flask_wtf import FlaskForm
from wtforms import StringField,IntegerField,FloatField,SelectField
from wtforms.validators import InputRequired, Email, Optional,Length,url

class CreateItem(FlaskForm):
  name=StringField('Name',validators=[InputRequired()])
  price=FloatField('Price',validators=[InputRequired()])
  quantity=IntegerField('Quantity',validators=[InputRequired()])
  sku=IntegerField('SKU',validators=[InputRequired()])
  warehouse=SelectField('Warehouse')



  
class CreateWarehouse(FlaskForm):
  name=StringField('Name',validators=[InputRequired()])
  