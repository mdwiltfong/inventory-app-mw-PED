from unittest import TestCase
from app import app

from flask import request,session
from app import app

from models import db,connect_db,Warehouse,Item

from dotenv import load_dotenv, find_dotenv

class test_crud(TestCase):
    def setUp(self):
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
    
        
    def test_view(self):
        """Get request should return HTML with all items from test db"""
        with app.test_client() as client:
            resp = client.get('/')
            html = resp.get_data(as_text=True)
            self.assertEqual(resp.status_code, 200)
            self.assertIn('<td style="text-align: center">123456</td>', html)
            self.assertIn('<td style="text-align: center">456789</td>', html)
            self.assertIn('<td style="text-align: center">753159</td>', html)
    def test_create(self):
        ''' post request to create_item should return 302 
        (a redirect) with a banner saying 'Item Created'''
        with app.test_client() as client:
            data={
                "name":'cheese',
                'price':123,
                'quantity': 43,
                'sku':375159,
                'warehouse':'Frisco'
            }
        
            resp=client.post('/create_item',data=data,follow_redirects=True)
            html = resp.get_data(as_text=True)
            new_item=Item.query.filter(Item.sku == data['sku']).first()
            self.assertEqual(resp.status_code,200)
            self.assertIn('Item Created',html)
            self.assertEqual(new_item.sku,data['sku'])
    def test_create_error(self):
        """post request with an already existing SKU should be rejected and raise an alert banner"""
        with app.test_client() as client:
            data={
                "name":'cheese',
                'price':123,
                'quantity': 43,
                'sku':123456,
                'warehouse':'Frisco'
            }
            resp=client.post('/create_item',data=data,follow_redirects=True)
            html = resp.get_data(as_text=True)
            failed_created_item=Item.query.filter(Item.sku == data['sku']).all()
            self.assertEqual(len(failed_created_item),1)
            self.assertEqual(resp.status_code,200)
            self.assertIn('SKU already exists',html)
    def test_create_warehouse(self):
        """post request to /create_warehouse will return a 200 
        http response with a banner saying 'warehouse created"""
        with app.test_client() as client:
            data={
                    "name":'cheese'
                }
        
            resp=client.post('/create_warehouse',data=data,follow_redirects=True)
            html = resp.get_data(as_text=True)
            new_warehouse=Warehouse.query.filter(Warehouse.name == data['name']).first()
            self.assertEqual(resp.status_code,200)
            self.assertIn('Warehouse Created',html)
            self.assertEqual(new_warehouse.name,data['name'])

    def test_edit_item(self):
        """Post request to /edit_item will do the following:
            - Edit an item.
            - Return HTTP status 200 (meaning a successful redirect occured)
            - Change the warehouse location, which will assign the inventory. 
            - Render a banner with a success message
         """
        with app.test_client() as client:
            data={
                "name":'Cheese',
                'price':999,
                'quantity':445,
                'sku':123456,
                'warehouse':'Las Vegas'
            }
            resp=client.post('/edit_item/123456/edit',data=data,follow_redirects=True)

            html=resp.get_data(as_text=True)
            updated_item=Item.query.filter(Item.sku==123456).first()

            self.assertEqual(resp.status_code,200)
            self.assertIn('Item 123456 updated!',html)
            self.assertEqual(updated_item.name,data['name'])
            self.assertEqual(updated_item.price,data['price'])
            self.assertEqual(updated_item.quantity,data['quantity'])
            self.assertEqual(updated_item.warehouse.name,data['warehouse'])
            self.assertEqual(updated_item.sku,data['sku'])
    def test_edit_item_error(self):
        """Updating an item to an already existing SKU will raise an error"""
        with app.test_client() as client:
            data={
                "name":'Cheese',
                'price':999,
                'quantity':445,
                'sku':456789,
                'warehouse':'Las Vegas'
            }
            resp=client.post('/edit_item/123456/edit',data=data,follow_redirects=True)

            html=resp.get_data(as_text=True)
            updated_item=Item.query.filter(Item.sku==123456).first()

            self.assertEqual(resp.status_code,200)
            self.assertIn('Item 123456 already exists',html)
            self.assertNotEqual(updated_item.name,data['name'])
            self.assertNotEqual(updated_item.price,data['price'])
            self.assertNotEqual(updated_item.quantity,data['quantity'])

    def test_delete_item(self):
        """Sending a post request to the /delete_item route will delete an item from the db"""
        with app.test_client() as client:
            resp=client.post('/delete_item/123456',follow_redirects=True)
            html=resp.get_data(as_text=True)

            self.assertEqual(resp.status_code,200)
            self.assertIn('Item 123456 deleted!',html)


