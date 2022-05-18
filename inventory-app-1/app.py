from flask import Flask, render_template,flash,redirect
from sqlalchemy.exc import IntegrityError
from models import Item, db, connect_db,Warehouse
from forms import CreateItem, CreateWarehouse
db_name='inventory-app-test'

app = Flask(__name__)
app.config['SECRET_KEY']="it's a secret"
app.config ['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///inventory-app-test'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = False
app.config['WTF_CSRF_ENABLED'] = False
connect_db(app)
db.create_all()
@app.route('/')
def load_index():
    """ Returns homepage and an entire list of items in the db"""
    items=Item.query.all()
    warehouses=Warehouse.query.all()
    return render_template("index.html", items=items,warehouses=warehouses)

@app.route('/create_item', methods=["POST","GET"])
def create_item():
    """Creates inventory item or renders create inventory item form"""
    try:
            form=CreateItem()
            warehouses=Warehouse.query.all()
            form.warehouse.choices=[(w.name) for w in warehouses]
            if form.validate_on_submit():
                new_item = Item(name=form.name.data,
                                    price=form.price.data,
                                    quantity=form.quantity.data,
                                    sku=form.sku.data,
                                    warehouse_id=form.warehouse.data
                               )
                db.session.add(new_item)
                db.session.commit()
                flash('Item Created',"success")
                return redirect('/')  
    except IntegrityError:
            flash("SKU already exists","danger")
            return redirect('/')
          
    return render_template('create_item_form.html',form=form,warehouses=warehouses)
@app.route('/create_warehouse', methods=["POST","GET"])
def create_warehouse():
    """Creates Warehouse Location or renders create inventory warehouse location"""
    try:  
      form=CreateWarehouse()
      if form.validate_on_submit():
          new_warehouse = Warehouse(name=form.name.data)
          db.session.add(new_warehouse)
          db.session.commit()
          flash('Warehouse Created',"success")
          return redirect('/')
    except IntegrityError:
      flash("Warehouse Already Exists","danger")
      return redirect('/')
    
    return render_template('create_warehouse_form.html',form=form)
@app.route('/edit_item/<int:sku>/edit',methods=['GET','POST'])
def edit_item(sku):
    """Edit a specific item by it'sku
     or renders the edit item form with fields pre-populated with pre-existing daata"""
    try:
        item=Item.query.get_or_404(sku)
        form=CreateItem(obj=item) 
        warehouses=Warehouse.query.all()
        form.warehouse.choices=[(w.name) for w in warehouses]
        if form.validate_on_submit():
          item.name=form.name.data
          item.price=form.price.data
          item.quantity=form.quantity.data
          item.sku=form.sku.data
          item.warehouse_id=form.warehouse.data
          db.session.commit()    
          flash(f"Item {sku} updated!","success")
          return redirect('/')
    except IntegrityError:
        flash(f"Item {sku} already exists","danger")
        return redirect('/')
    return render_template("edit_item_form.html", form=form,item=item)

@app.route('/delete_item/<int:sku>',methods=['POST','GET'])
def delete_item(sku):
  ''' Deletes a specific item by it's SKU '''
  Item.query.filter_by(sku=sku).delete()
  db.session.commit()
  flash(f"Item {sku} deleted!","success")
  return redirect('/')
    
# This function is solely for running the application on replit's built in browser. If running locally, it will have to commented out.
''' app.run(
  host = "0.0.0.0", # or 127.0.0.1
  port = 8080, # make sure this is a non privileged port
  debug = True # this will allow us to easily fix problems and bugs
) '''