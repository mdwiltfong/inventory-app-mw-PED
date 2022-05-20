from email.policy import default
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import ForeignKey

db=SQLAlchemy()

def connect_db(app):
  db.app=app
  db.init_app(app)

class Item(db.Model):
  __tablename__='items'
  id=db.Column(
    db.Integer,
    autoincrement=True
  )
  name=db.Column(
    db.Text,
    nullable=False
  )
  price=db.Column(
    db.Integer,
    nullable=False
  )
  total_quantity=db.Column(
    db.Integer,
    nullable=False
  )
  sku=db.Column(
    db.Integer,
    primary_key=True,
    nullable=False
  )
  warehouses=db.relationship(
    'Warehouse',
    secondary='items_warehouses',
    backref='item'
  )
  assignments=db.relationship(
   'ItemWarehouse',
   backref='item'
 )
  def __repr__(self):
    return f'<Item #{self.id} {self.name} {self.price}>'

class Warehouse(db.Model):
  __tablename__='warehouses'
  name=db.Column(
      db.Text,
      nullable=False,
    primary_key=True
    )

class ItemWarehouse(db.Model):
  __tablename__='items_warehouses'

  id=db.Column(
    db.Integer,
    autoincrement=True
  )
  items_sku=db.Column(
    db.Integer,
    db.ForeignKey('items.sku',ondelete='cascade'),
    primary_key=True
  )
  warehouse_name=db.Column(
     db.Text,
    db.ForeignKey('warehouses.name',ondelete='cascade'),
    primary_key=True
  )
  quantity=db.Column(
    db.Integer,
    nullable=False,
    default=0
  )