"""Seed file to make sample data for pets db."""

from models import Item,Warehouse,db,ItemWarehouse
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
item1=Item(name="Shirt",price=12.45, total_quantity=45,sku=123456)
item2=Item(name="Red Shirt",price=15, total_quantity=85,sku=753159)
item3=Item(name="Green Shirt",price=85, total_quantity=45,sku=456789)
db.session.add_all([item1,item2,item3])
db.session.commit()



item1.assignments.append(ItemWarehouse(warehouse_name='Frisco', quantity=45))
item1.assignments.append(ItemWarehouse(warehouse_name='Las Vegs', quantity=55))
item1.assignments.append(ItemWarehouse(warehouse_name='Riyadh', quantity=65))

item2.assignments.append(ItemWarehouse(warehouse_name='Frisco', quantity=125))
item2.assignments.append(ItemWarehouse(warehouse_name='Las Vegs', quantity=355))
item2.assignments.append(ItemWarehouse(warehouse_name='Riyadh', quantity=698))

item3.assignments.append(ItemWarehouse(warehouse_name='Frisco', quantity=25))
item3.assignments.append(ItemWarehouse(warehouse_name='Las Vegs', quantity=35))
item3.assignments.append(ItemWarehouse(warehouse_name='Riyadh', quantity=98))



db.session.add(item1)
db.session.commit()
