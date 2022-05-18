"""Seed file to make sample data for pets db."""

from models import Item,Warehouse,db
from app import app

# Create all tables
db.drop_all()
db.create_all()
# Add Warehouses
warehouse1=Warehouse(name='Frisco')
warehouse2=Warehouse(name='Las Vegas')
warehouse3=Warehouse(name='Riyadh')
db.session.add_all([warehouse1,warehouse2,warehouse3])
db.session.commit()
# Add items
item1=Item(name="Shirt",price=12.45, quantity=45,sku=123456,warehouse_id="Frisco")
item2=Item(name="Red Shirt",price=15, quantity=85,sku=753159,warehouse_id="Las Vegas")
item3=Item(name="Green Shirt",price=85, quantity=45,sku=456789,warehouse_id="Riyadh")


# Add new objects to session, so they'll persist
db.session.add_all([item1,item2,item3])



warehouse1.items.append(item1)
warehouse2.items.append(item2)
warehouse3.items.append(item3)

db.session.add_all([warehouse1,warehouse2,warehouse3])
db.session.commit()

# Commit--otherwise, this never gets saved!
db.session.commit()