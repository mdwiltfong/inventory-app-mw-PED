from flask_sqlalchemy import SQLAlchemy

db=SQLAlchemy()

def connect_db(app):
  db.app=app
  db.init_app(app)

class Item(db.Model):
  __tablename__='items'
  id=db.Column(
    db.Integer,
    primary_key=True,
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
  quantity=db.Column(
    db.Integer,
    nullable=False
  )
  sku=db.Column(
    db.Integer,
    nullable=False
  )
  warehouse_id=db.Column(
    db.Text,
    db.ForeignKey('warehouses.name')
  )
  warehouse=db.relationship('Warehouse')
 
  def __repr__(self):
    return f'<Item #{self.id} {self.name} {self.price}>'

class Warehouse(db.Model):
  __tablename__='warehouses'
  name=db.Column(
      db.Text,
      nullable=False,
    primary_key=True
    )
  items=db.relationship('Item')

